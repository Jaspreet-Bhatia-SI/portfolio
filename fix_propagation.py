with open('portfolio.html', 'r') as f:
    html = f.read()

target = "document.getElementById('btn-close-phone').addEventListener('click', togglePhone);"
injection = target + """
        phoneFrame.addEventListener('mousedown', e => e.stopPropagation());
        phoneFrame.addEventListener('touchstart', e => e.stopPropagation());
"""
if target in html and "stopPropagation" not in html:
    html = html.replace(target, injection)

with open('portfolio.html', 'w') as f:
    f.write(html)
