import re

with open('portfolio.html', 'r') as f:
    html = f.read()

# 1. Update PointerLock request logic
old_lock = """        document.body.addEventListener('click', (e) => {
            if (e.target.tagName !== 'BUTTON' && e.target.tagName !== 'A' && !e.target.closest('button') && !e.target.closest('a')) {
                if (window.innerWidth > 768) document.body.requestPointerLock();
            }
        });"""
new_lock = """        document.body.addEventListener('click', (e) => {
            const pUI = document.getElementById('phone-ui');
            if (pUI && !pUI.classList.contains('hidden')) return;
            if (e.target.tagName !== 'BUTTON' && e.target.tagName !== 'A' && !e.target.closest('button') && !e.target.closest('a') && !e.target.closest('input')) {
                if (window.innerWidth > 768) document.body.requestPointerLock();
            }
        });"""
html = html.replace(old_lock, new_lock)

# 2. Update togglePhone to exit pointer lock
old_toggle = """        function togglePhone() {
            const isHidden = phoneUI.classList.contains('pointer-events-none');
            if(isHidden) {"""
new_toggle = """        function togglePhone() {
            const isHidden = phoneUI.classList.contains('pointer-events-none');
            if(isHidden) {
                if(document.pointerLockElement) document.exitPointerLock();"""
html = html.replace(old_toggle, new_toggle)

# 3. Add click outside to close
old_listeners = """        btnContacts.addEventListener('click', togglePhone);
        document.getElementById('btn-close-phone').addEventListener('click', togglePhone);
        phoneFrame.addEventListener('mousedown', e => e.stopPropagation());
        phoneFrame.addEventListener('touchstart', e => e.stopPropagation());"""
new_listeners = old_listeners + """
        phoneUI.addEventListener('mousedown', (e) => {
            if (e.target === phoneUI) togglePhone();
        });
        phoneUI.addEventListener('touchstart', (e) => {
            if (e.target === phoneUI) togglePhone();
        });"""
html = html.replace(old_listeners, new_listeners)

with open('portfolio.html', 'w') as f:
    f.write(html)
print("Applied UX fixes")
