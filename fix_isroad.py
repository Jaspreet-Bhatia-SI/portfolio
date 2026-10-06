import re
with open('portfolio.html', 'r') as f:
    html = f.read()

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
# Insert before `const treeGeo`
html = re.sub(r'(\s+const treeGeo = new THREE\.ConeGeometry)', is_road_func + r'\1', html)

with open('portfolio.html', 'w') as f:
    f.write(html)
