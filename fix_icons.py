import re

with open('portfolio.html', 'r') as f:
    html = f.read()

target = '<script src="https://code.iconify.design/3/3.1.0/iconify.min.js"></script>'
replacement = '<script src="https://code.iconify.design/iconify-icon/1.0.7/iconify-icon.min.js"></script>'

if target in html:
    html = html.replace(target, replacement)

with open('portfolio.html', 'w') as f:
    f.write(html)
print("Fixed icons script")
