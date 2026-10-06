import re

with open('portfolio.html', 'r') as f:
    html = f.read()

# I will replace the entire drawMinimap function by finding its start and end
# Note that drawMinimap ends right before `const ACCELERATION = 0.04;`

old_draw_pattern = r'function drawMinimap\(\).*?minimapCtx\.restore\(\);\s*\}'
new_draw = """function drawMinimap() {
            if(!minimapCtx) return;
            const mw = minimapCanvas.width;
            const mh = minimapCanvas.height;
            minimapCtx.clearRect(0, 0, mw, mh);
            
            const px = state.mode === 'DRIVING' ? carGroup.position.x : playerGroup.position.x;
            const pz = state.mode === 'DRIVING' ? carGroup.position.z : playerGroup.position.z;
            const pAngle = state.mode === 'DRIVING' ? state.angle : state.playerAngle;

            if(!minimapExpanded) {
                mapPanX = px; mapPanY = pz; mapZoom = 1;
            }

            minimapCtx.save();
            minimapCtx.translate(mw / 2, mh / 2);
            let baseScale = (mw / 160) * (window.innerWidth < 768 ? 0.6 : 0.8);
            if(minimapExpanded) baseScale = (mw / 360); // Fits map roughly
            
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

            buildings.forEach(b => {
                const isHQ = b.id === 'about-hq';
                const bw = isHQ ? 24 : 18; const bd = isHQ ? 30 : 20;
                minimapCtx.save();
                minimapCtx.translate(b.x, b.z);
                minimapCtx.rotate(-b.angle);
                minimapCtx.fillStyle = isHQ ? '#6366f1' : '#' + b.color.toString(16).padStart(6,'0');
                minimapCtx.fillRect(-bw/2, -bd/2, bw, bd);
                minimapCtx.strokeStyle = '#ffffff'; minimapCtx.lineWidth = 1.5; minimapCtx.strokeRect(-bw/2, -bd/2, bw, bd);
                minimapCtx.restore();
            });

            // Player Blip
            minimapCtx.save();
            minimapCtx.translate(px, pz);
            minimapCtx.rotate(-pAngle);
            minimapCtx.fillStyle = '#f97316';
            minimapCtx.shadowColor = '#ea580c';
            minimapCtx.shadowBlur = 10;
            minimapCtx.beginPath();
            minimapCtx.moveTo(0, -6);
            minimapCtx.lineTo(4, 6);
            minimapCtx.lineTo(-4, 6);
            minimapCtx.closePath();
            minimapCtx.fill();
            minimapCtx.restore();

            minimapCtx.restore();
        }"""

html = re.sub(old_draw_pattern, new_draw, html, flags=re.DOTALL)
with open('portfolio.html', 'w') as f:
    f.write(html)
print("Updated successfully")
