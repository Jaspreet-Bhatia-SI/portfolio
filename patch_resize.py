import re

with open('portfolio.html', 'r') as f:
    html = f.read()

old_resize = r"window\.addEventListener\('resize', \(\) => \{(.*?renderer\.setSize.*?)\}\);"
new_resize = """window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight; camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
            if (typeof minimapExpanded !== 'undefined' && minimapExpanded) {
                minimapCanvas.width = window.innerWidth * 0.9;
                minimapCanvas.height = window.innerHeight * 0.9;
            }
        });"""

html = re.sub(old_resize, new_resize, html, flags=re.DOTALL)
with open('portfolio.html', 'w') as f:
    f.write(html)
print("Updated resize")
