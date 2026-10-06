import re

with open('portfolio.html', 'r') as f:
    html = f.read()

# 1. Add the scaling wrapper and fix the phone frame size
old_frame_start = '<!-- Phone Frame -->\n        <div class="relative w-[90vw] max-w-[340px] h-[85vh] max-h-[680px] bg-black rounded-[36px] sm:rounded-[50px] border-[8px] sm:border-[12px] border-black shadow-[0_20px_50px_rgba(0,0,0,0.5)] flex flex-col transform scale-[0.2] translate-y-32 opacity-0 transition-all duration-500 pointer-events-auto overflow-hidden" id="phone-frame">'

new_frame_start = """<!-- Phone Frame Wrapper for perfect scaling -->
        <div class="flex items-center justify-center w-full h-full pointer-events-none" style="transform: scale(min(1, calc(95vw / 340), calc(90vh / 680)));">
            <!-- Phone Frame -->
            <div class="relative w-[320px] h-[640px] shrink-0 bg-black rounded-[44px] border-[10px] border-black shadow-[0_20px_50px_rgba(0,0,0,0.5)] flex flex-col transform scale-[0.2] translate-y-32 opacity-0 transition-all duration-500 pointer-events-auto overflow-hidden" id="phone-frame">"""

if old_frame_start in html:
    html = html.replace(old_frame_start, new_frame_start)
else:
    print("Could not find phone frame start")

# We must also close the new wrapper div. 
# It goes right before `<!-- Virtual Joystick -->`
old_closing = """        </div>
    </div>
    <!-- Virtual Joystick -->"""

new_closing = """        </div>
            </div>
        </div>
    </div>
    <!-- Virtual Joystick -->"""

if "        </div>\n    </div>\n    <!-- Virtual Joystick -->" in html:
    html = html.replace("        </div>\n    </div>\n    <!-- Virtual Joystick -->", "        </div>\n            </div>\n        </div>\n    <!-- Virtual Joystick -->")
else:
    print("Could not find closing tags")

# 2. Fix the inner grid and margins to remove sm: classes since it's a fixed size now
html = html.replace('mt-4 sm:mt-8 px-4 sm:px-6 grid grid-cols-4 gap-y-4 sm:gap-y-8 gap-x-3 sm:gap-x-4', 'mt-8 px-5 grid grid-cols-4 gap-y-8 gap-x-3')
html = html.replace('mt-2 sm:mt-6 mx-4 relative', 'mt-5 mx-4 relative')

with open('portfolio.html', 'w') as f:
    f.write(html)
print("Applied scaling fix")
