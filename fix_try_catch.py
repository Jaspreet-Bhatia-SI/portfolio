import re

with open('portfolio.html', 'r') as f:
    html = f.read()

html = html.replace('try {\n        // --- POCHINKI ARCHITECTURE', 'try { (() => {\n        // --- POCHINKI ARCHITECTURE')
html = html.replace('} catch(e) { \n    const errDiv', '})(); } catch(e) { \n    const errDiv')

with open('portfolio.html', 'w') as f:
    f.write(html)
print("done")
