import re

with open('portfolio.html', 'r') as f:
    html = f.read()

# 1. Update minimap container HTML to allow click
old_minimap_wrapper = '<div class="relative w-28 h-28 md:w-40 md:h-40 bg-[#1c221a]/80 backdrop-blur-md border-2 border-white/20 rounded-full overflow-hidden shadow-[0_0_15px_rgba(0,0,0,0.5)]">'
new_minimap_wrapper = '<div id="minimap-wrapper" class="relative w-28 h-28 md:w-40 md:h-40 bg-[#1c221a]/80 backdrop-blur-md border-2 border-white/20 rounded-full overflow-hidden shadow-[0_0_15px_rgba(0,0,0,0.5)] cursor-pointer transition-all duration-300">'
html = html.replace(old_minimap_wrapper, new_minimap_wrapper)

# 2. Add click logic near `const minimapCanvas = document.getElementById('minimap-canvas');`
minimap_js_target = "const minimapCanvas = document.getElementById('minimap-canvas');"
minimap_logic = minimap_js_target + """
        const minimapWrapper = document.getElementById('minimap-wrapper');
        let minimapExpanded = false;
        minimapWrapper.addEventListener('click', () => {
            minimapExpanded = !minimapExpanded;
            if (minimapExpanded) {
                minimapWrapper.classList.remove('w-28', 'h-28', 'md:w-40', 'md:h-40', 'rounded-full');
                minimapWrapper.classList.add('w-[80vw]', 'h-[80vw]', 'md:w-[600px]', 'md:h-[600px]', 'rounded-lg', 'fixed', 'top-1/2', 'left-1/2', '-translate-x-1/2', '-translate-y-1/2', 'z-[200]');
                minimapCanvas.width = 600;
                minimapCanvas.height = 600;
            } else {
                minimapWrapper.classList.add('w-28', 'h-28', 'md:w-40', 'md:h-40', 'rounded-full');
                minimapWrapper.classList.remove('w-[80vw]', 'h-[80vw]', 'md:w-[600px]', 'md:h-[600px]', 'rounded-lg', 'fixed', 'top-1/2', 'left-1/2', '-translate-x-1/2', '-translate-y-1/2', 'z-[200]');
                minimapCanvas.width = 160;
                minimapCanvas.height = 160;
            }
        });
"""
html = html.replace(minimap_js_target, minimap_logic)

# 3. Add `isRoad(x, z)` function
is_road_func = """
        function isRoad(x, z) {
            const hw = 16;
            if (Math.abs(x - -100) < hw && z > -135 && z < 135) return true;
            if (Math.abs(x - 100) < hw && z > -135 && z < 135) return true;
            if (Math.abs(z - -120) < hw && x > -115 && x < 115) return true;
            if (Math.abs(z - 120) < hw && x > -115 && x < 115) return true;
            if (Math.abs(x) < hw && Math.abs(z) < 135) return true; 
            if (Math.abs(z) < hw && Math.abs(x) < 115) return true; 
            return false;
        }
"""
html = html.replace('const treeGeo = new THREE.ConeGeometry(3, 8, 8);', is_road_func + '\n        const treeGeo = new THREE.ConeGeometry(3, 8, 8);')

# 4. Modify trees
html = html.replace('if(Math.abs(x) < 20 && Math.abs(z) < 200) continue;', 'if(isRoad(x, z)) continue;')
# 5. Modify haybales
html = html.replace('if (Math.abs(h.position.x) > 12)', 'if (!isRoad(h.position.x, h.position.z))')

# 6. Remove fences
html = re.sub(r'createFence\([^)]+\);\s*createFence\([^)]+\);', '', html)

# 7. Add visual cross roads
old_roads_pattern = r"const mainRoad = new THREE\.Mesh.*?envGroup\.add\(mainRoad4\);"
new_roads = """
            const r1 = new THREE.Mesh(new THREE.PlaneGeometry(240, 24), roadMat); r1.rotation.x = -Math.PI/2; r1.position.set(0, 0.1, -120); r1.receiveShadow = true;
            const r2 = new THREE.Mesh(new THREE.PlaneGeometry(240, 24), roadMat); r2.rotation.x = -Math.PI/2; r2.position.set(0, 0.1, 120); r2.receiveShadow = true;
            const r3 = new THREE.Mesh(new THREE.PlaneGeometry(24, 260), roadMat); r3.rotation.x = -Math.PI/2; r3.position.set(-100, 0.1, 0); r3.receiveShadow = true;
            const r4 = new THREE.Mesh(new THREE.PlaneGeometry(24, 260), roadMat); r4.rotation.x = -Math.PI/2; r4.position.set(100, 0.1, 0); r4.receiveShadow = true;
            const r5 = new THREE.Mesh(new THREE.PlaneGeometry(200, 24), roadMat); r5.rotation.x = -Math.PI/2; r5.position.set(0, 0.12, 0); r5.receiveShadow = true;
            const r6 = new THREE.Mesh(new THREE.PlaneGeometry(24, 240), roadMat); r6.rotation.x = -Math.PI/2; r6.position.set(0, 0.12, 0); r6.receiveShadow = true;
            envGroup.add(r1, r2, r3, r4, r5, r6);
"""
html = re.sub(old_roads_pattern, new_roads.strip(), html, flags=re.DOTALL)

# 8. Update minimap rendering coordinates
old_minimap_draw = r"// Simple map representation.*?ctx\.fillStyle = '#555';.*?ctx\.fillRect\(100 \- 10, 0, 20, 240\);"
new_minimap_draw = """
            // Simple map representation
            ctx.fillStyle = state.mode === 'NIGHT' ? '#111' : (state.mode === 'EVENING' ? '#543' : '#45603a');
            ctx.fillRect(0, 0, 200, 200);
            
            // Outer Ring
            ctx.fillStyle = '#555';
            ctx.fillRect(10, 10, 180, 20); ctx.fillRect(10, 170, 180, 20);
            ctx.fillRect(10, 10, 20, 180); ctx.fillRect(170, 10, 20, 180);
            // Inner Cross
            ctx.fillStyle = '#666';
            ctx.fillRect(30, 90, 140, 20); ctx.fillRect(90, 30, 20, 140);
"""
html = re.sub(old_minimap_draw, new_minimap_draw.strip(), html, flags=re.DOTALL)


with open('portfolio.html', 'w') as f:
    f.write(html)
print("Updated successfully.")
