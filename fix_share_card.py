import re

with open('portfolio.html', 'r') as f:
    html = f.read()

# Remove the Contact Card generation from btnShare click
pattern = r"// Create Contact Card[\s\S]*?btnShare\.classList\.add\('hidden', 'opacity-0'\);"
replacement = "btnShare.classList.add('hidden', 'opacity-0');"

if re.search(pattern, html):
    html = re.sub(pattern, replacement, html)
else:
    print("Pattern not found for Contact Card creation")

# Remove any scene.remove(state.shareCard) later
html = html.replace("if(state.shareCard) { scene.remove(state.shareCard); state.shareCard = null; }", "")

with open('portfolio.html', 'w') as f:
    f.write(html)
