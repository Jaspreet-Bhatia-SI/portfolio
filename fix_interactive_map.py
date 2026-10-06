import re

with open('portfolio.html', 'r') as f:
    html = f.read()

# 1. Remove the minimap-blip DOM element
blip_html_pattern = r'<div class="absolute top-1/2 left-1/2 w-4 h-4 -mt-2 -ml-2 pointer-events-none z-10 flex items-center justify-center">.*?</div>'
html = re.sub(blip_html_pattern, '', html, flags=re.DOTALL)

# 2. Remove old click listener logic
old_click_logic_pattern = r'const minimapWrapper = document\.getElementById\(\'minimap-wrapper\'\);\s*let minimapExpanded = false;\s*minimapWrapper\.addEventListener\(\'click\'.*?\}\);'
html = re.sub(old_click_logic_pattern, '', html, flags=re.DOTALL)

# 3. Add new Interactive Map logic
interactive_logic = """
        const minimapWrapper = document.getElementById('minimap-wrapper');
        const minimapCanvas = document.getElementById('minimap-canvas');
        const minimapCtx = minimapCanvas ? minimapCanvas.getContext('2d') : null;
        
        let minimapExpanded = false;
        let mapPanX = 0, mapPanY = 0, mapZoom = 1;
        let mapDragStartX = 0, mapDragStartY = 0, isMapDragging = false, didMapDrag = false;
        let initialPinchDist = null, initialPinchZoom = 1;

        function startMapDrag(x, y) {
            isMapDragging = true; didMapDrag = false;
            mapDragStartX = x; mapDragStartY = y;
        }
        function doMapDrag(x, y) {
            if(!isMapDragging) return;
            const dx = x - mapDragStartX;
            const dy = y - mapDragStartY;
            if(Math.hypot(dx, dy) > 5) didMapDrag = true;
            if(minimapExpanded && didMapDrag) {
                // Adjust pan speed based on zoom
                const panSpeed = 2.0 / mapZoom; 
                mapPanX -= dx * panSpeed;
                mapPanY -= dy * panSpeed;
                mapDragStartX = x; mapDragStartY = y;
            }
        }
        function endMapDrag(e) {
            isMapDragging = false; initialPinchDist = null;
            if(!didMapDrag && e && e.type && (e.type.includes('up') || e.type === 'touchend')) {
                minimapExpanded = !minimapExpanded;
                if (minimapExpanded) {
                    minimapWrapper.classList.remove('w-28', 'h-28', 'md:w-40', 'md:h-40', 'rounded-full');
                    minimapWrapper.classList.add('w-[90vw]', 'h-[90vh]', 'rounded-lg', 'fixed', 'top-1/2', 'left-1/2', '-translate-x-1/2', '-translate-y-1/2', 'z-[200]');
                    minimapCanvas.width = window.innerWidth * 0.9;
                    minimapCanvas.height = window.innerHeight * 0.9;
                    mapPanX = state.mode === 'DRIVING' ? carGroup.position.x : playerGroup.position.x;
                    mapPanY = state.mode === 'DRIVING' ? carGroup.position.z : playerGroup.position.z;
                    mapZoom = 1;
                } else {
                    minimapWrapper.classList.add('w-28', 'h-28', 'md:w-40', 'md:h-40', 'rounded-full');
                    minimapWrapper.classList.remove('w-[90vw]', 'h-[90vh]', 'rounded-lg', 'fixed', 'top-1/2', 'left-1/2', '-translate-x-1/2', '-translate-y-1/2', 'z-[200]');
                    minimapCanvas.width = 160;
                    minimapCanvas.height = 160;
                }
            }
        }

        minimapWrapper.addEventListener('mousedown', (e) => startMapDrag(e.clientX, e.clientY));
        minimapWrapper.addEventListener('mousemove', (e) => doMapDrag(e.clientX, e.clientY));
        minimapWrapper.addEventListener('mouseup', endMapDrag);
        minimapWrapper.addEventListener('mouseleave', endMapDrag);

        minimapWrapper.addEventListener('touchstart', (e) => {
            if(e.touches.length === 1) startMapDrag(e.touches[0].clientX, e.touches[0].clientY);
        }, {passive: false});
        
        minimapWrapper.addEventListener('touchmove', (e) => {
            if(minimapExpanded) e.preventDefault();
            if(e.touches.length === 2 && minimapExpanded) {
                const dist = Math.hypot(e.touches[0].clientX - e.touches[1].clientX, e.touches[0].clientY - e.touches[1].clientY);
                if(initialPinchDist === null) { initialPinchDist = dist; initialPinchZoom = mapZoom; }
                else {
                    mapZoom = initialPinchZoom * (dist / initialPinchDist);
                    mapZoom = Math.min(Math.max(0.3, mapZoom), 5);
                }
            } else if(e.touches.length === 1) {
                doMapDrag(e.touches[0].clientX, e.touches[0].clientY);
            }
        }, {passive: false});
        
        minimapWrapper.addEventListener('touchend', endMapDrag);

        minimapWrapper.addEventListener('wheel', (e) => {
            if(!minimapExpanded) return;
            e.preventDefault();
            mapZoom += e.deltaY * -0.002;
            mapZoom = Math.min(Math.max(0.3, mapZoom), 5);
        }, {passive: false});
"""
# Replace the old vars block:
old_vars_pattern = r'const minimapCanvas = document\.getElementById\(\'minimap-canvas\'\);\s*const minimapCtx = minimapCanvas \? minimapCanvas\.getContext\(\'2d\'\) : null;\s*const minimapBlip = document\.getElementById\(\'minimap-blip\'\);'
html = re.sub(old_vars_pattern, interactive_logic, html)


# 4. Modify drawMinimap to use mapPanX, mapPanY, mapZoom and draw blip
old_draw_func = r'function drawMinimap\(\).*?minimapCtx\.fillRect\(-12, -120, 24, 240\); // V\s*\}'
new_draw_func = """function drawMinimap() {
            if(!minimapCtx) return;
            const mw = minimapCanvas.width;
            const mh = minimapCanvas.height;
            minimapCtx.clearRect(0, 0, mw, mh);
            
            const px = state.mode === 'DRIVING' ? carGroup.position.x : playerGroup.position.x;
            const pz = state.mode === 'DRIVING' ? carGroup.position.z : playerGroup.position.z;
            const pAngle = state.mode === 'DRIVING' ? state.angle : state.playerAngle;

            // If not expanded, always track player
            if (!minimapExpanded) { mapPanX = px; mapPanY = pz; mapZoom = 1; }

            minimapCtx.save();
            minimapCtx.translate(mw / 2, mh / 2);
            let baseScale = (mw / 160) * (window.innerWidth < 768 ? 0.6 : 0.8);
            if(minimapExpanded) baseScale = (mw / 800); // Fit whole map loosely
            
            minimapCtx.scale(baseScale * mapZoom, baseScale * mapZoom);
            minimapCtx.translate(-mapPanX, -mapPanY);

            // Ring Road
            minimapCtx.fillStyle = '#594a36'; 
            minimapCtx.fillRect(-112, -132, 224, 24); // top
            minimapCtx.fillRect(-112, 108, 224, 24); // bot
            minimapCtx.fillRect(-112, -132, 24, 264); // left
            minimapCtx.fillRect(88, -132, 24, 264); // right
            // Inner Cross
            minimapCtx.fillRect(-100, -12, 200, 24); // H
            minimapCtx.fillRect(-12, -120, 24, 240); // V

            // Buildings
            buildings.forEach(b => {
                const isHQ = b.id === 'about-hq';
                const bw = isHQ ? 24 : 18; const bd = isHQ ? 30 : 20;
                minimapCtx.save();
                minimapCtx.translate(b.x, b.z);
                minimapCtx.rotate(-b.angle);
                minimapCtx.fillStyle = '#' + b.color.toString(16).padStart(6,'0');
                minimapCtx.fillRect(-bw/2, -bd/2, bw, bd);
                minimapCtx.restore();
            });

            // Draw Player Blip
            minimapCtx.save();
            minimapCtx.translate(px, pz);
            minimapCtx.rotate(-pAngle);
            minimapCtx.fillStyle = '#f97316';
            minimapCtx.shadowColor = '#ea580c';
            minimapCtx.shadowBlur = 10;
            minimapCtx.beginPath();
            minimapCtx.moveTo(0, -10);
            minimapCtx.lineTo(7, 10);
            minimapCtx.lineTo(-7, 10);
            minimapCtx.closePath();
            minimapCtx.fill();
            minimapCtx.restore();

            minimapCtx.restore();
        }"""
html = re.sub(old_draw_func, new_draw_func, html, flags=re.DOTALL)

with open('portfolio.html', 'w') as f:
    f.write(html)
print("Applied successfully.")
