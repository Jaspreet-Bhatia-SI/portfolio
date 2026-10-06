import re

with open('portfolio.html', 'r') as f:
    html = f.read()

# 1. Remove btn-contacts from HTML
html = re.sub(r'<button id="btn-contacts".*?</button>', '', html, flags=re.DOTALL)

# 2. Fix the wrapper by adding an ID and removing the inline style
old_wrapper = '<div class="flex items-center justify-center w-full h-full pointer-events-none" style="transform: scale(min(1, calc(95vw / 340), calc(90vh / 680)));">'
new_wrapper = '<div id="phone-scale-wrapper" class="flex items-center justify-center w-full h-full pointer-events-none">'
html = html.replace(old_wrapper, new_wrapper)

# 3. Add JS to handle robust scaling, remove btnContacts logic
# Remove references to btnContacts
html = html.replace("const btnContacts = document.getElementById('btn-contacts');", "")
html = html.replace("btnContacts.addEventListener('click', togglePhone);", "")
html = html.replace("document.getElementById('btn-contacts').classList.remove('hidden');", "")

# Add resize logic to togglePhone
js_scale_logic = """
        function resizePhone() {
            const wrapper = document.getElementById('phone-scale-wrapper');
            if (wrapper) {
                const scale = Math.min(1, (window.innerWidth * 0.95) / 350, (window.innerHeight * 0.9) / 680);
                wrapper.style.transform = `scale(${scale})`;
            }
        }
        window.addEventListener('resize', resizePhone);
        
        function togglePhone() {
            resizePhone();
"""
html = html.replace("        function togglePhone() {", js_scale_logic)

with open('portfolio.html', 'w') as f:
    f.write(html)
print("Fixes applied")
