import re

with open('portfolio.html', 'r') as f:
    html = f.read()

# 1. Fix hasContact issue so phone appears every time
if 'let hasContact = false;' in html:
    html = html.replace('let hasContact = false;', '')

if 'if (!hasContact) {\n                        hasContact = true;\n                        \n                        togglePhone(); \n                    }' in html:
    html = html.replace('if (!hasContact) {\n                        hasContact = true;\n                        \n                        togglePhone(); \n                    }', 'if (t >= 1.5 && t < 1.55 && state.shareTimer - 0.02 < 1.5) {\n                        togglePhone();\n                    }')
else:
    # Use regex
    html = re.sub(r'if \(!hasContact\) \{[\s\S]*?hasContact = true;[\s\S]*?togglePhone\(\);[\s\S]*?\}', 'if (t >= 1.5 && t < 1.52) togglePhone();', html)

# 2. Fix iphone scale and cropping
wrapper_str = '<div id="phone-scale-wrapper" class="flex items-center justify-center w-full h-full pointer-events-none">'
if wrapper_str in html:
    html = html.replace(wrapper_str, '<div id="phone-scale-wrapper" class="flex items-center justify-center w-full h-full pointer-events-none" style="transform: scale(min(1, calc(95vw / 350), calc(90vh / 680))); transform-origin: center center;">')

# 3. Link for curator ai in iphone is wrong
html = html.replace('curator-ai.foodzie.store', 'curator.foodzie.store')

# 4. Remove new button? The user says "instead a new button is added which i dont want".
# Maybe they mean `btnShare`?
# "instead a new button is added which i dont want"
# In force_share_logic.py: `const cardCanvas = document.createElement('canvas');`
# Wait, "the iphone not appearing after contact share , instead a new button is added which i dont want"
# Maybe they are referring to a button added dynamically?
# Let's write to file.
with open('portfolio.html', 'w') as f:
    f.write(html)
print("done")
