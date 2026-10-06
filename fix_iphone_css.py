import sys

with open('portfolio.html', 'r') as f:
    html = f.read()

# Replace phone-scale-wrapper and phone-frame to use better mobile responsive scaling
old_wrapper = '<div id="phone-scale-wrapper" class="flex items-center justify-center w-full h-full pointer-events-none" style="transform: scale(min(1, calc(95vw / 350), calc(90vh / 680))); transform-origin: center center;">'
new_wrapper = '<div id="phone-scale-wrapper" class="flex items-center justify-center w-full h-full pointer-events-none" style="transform: scale(min(1, calc(100vw / 350), calc(100svh / 700))); transform-origin: center center;">'

html = html.replace(old_wrapper, new_wrapper)

with open('portfolio.html', 'w') as f:
    f.write(html)
