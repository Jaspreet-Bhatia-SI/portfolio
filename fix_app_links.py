import re

with open('portfolio.html', 'r') as f:
    html = f.read()

# 1. Replace the entire Apps Grid
start_marker = '<!-- Apps Grid -->'
end_marker = '<!-- Bottom Dock -->'

new_apps_grid = """<!-- Apps Grid -->
                <div class="mt-4 sm:mt-8 px-4 sm:px-6 grid grid-cols-4 gap-y-4 sm:gap-y-8 gap-x-3 sm:gap-x-4 z-20">
                    <div onclick="window.open('mailto:bhatiajaspreet161@gmail.com', '_blank')" class="flex flex-col items-center gap-1.5 group cursor-pointer">
                        <div class="w-[60px] h-[60px] rounded-[14px] bg-gradient-to-b from-[#5ac8fa] to-[#007aff] flex items-center justify-center shadow-md group-hover:scale-105 transition-transform">
                            <iconify-icon icon="solar:letter-bold" width="34" class="text-white"></iconify-icon>
                        </div>
                        <span class="text-white text-[11px] font-medium drop-shadow-md">Mail</span>
                    </div>
                    
                    <div onclick="window.open('https://linkedin.com/in/jaspreet-bhatia-si', '_blank')" class="flex flex-col items-center gap-1.5 group cursor-pointer">
                        <div class="w-[60px] h-[60px] rounded-[14px] bg-[#0077b5] flex items-center justify-center shadow-md group-hover:scale-105 transition-transform">
                            <iconify-icon icon="mdi:linkedin" width="40" class="text-white"></iconify-icon>
                        </div>
                        <span class="text-white text-[11px] font-medium drop-shadow-md">LinkedIn</span>
                    </div>
                    
                    <div onclick="window.open('https://instagram.com/jass_bhatia.si', '_blank')" class="flex flex-col items-center gap-1.5 group cursor-pointer">
                        <div class="w-[60px] h-[60px] rounded-[14px] bg-gradient-to-tr from-[#f09433] via-[#dc2743] to-[#bc1888] flex items-center justify-center shadow-md group-hover:scale-105 transition-transform">
                            <iconify-icon icon="mdi:instagram" width="38" class="text-white"></iconify-icon>
                        </div>
                        <span class="text-white text-[11px] font-medium drop-shadow-md">Instagram</span>
                    </div>
                    
                    <div onclick="window.open('https://github.com/Jaspreet-Bhatia-SI', '_blank')" class="flex flex-col items-center gap-1.5 group cursor-pointer">
                        <div class="w-[60px] h-[60px] rounded-[14px] bg-white flex items-center justify-center shadow-md group-hover:scale-105 transition-transform">
                            <iconify-icon icon="mdi:github" width="40" class="text-[#181717]"></iconify-icon>
                        </div>
                        <span class="text-white text-[11px] font-medium drop-shadow-md">GitHub</span>
                    </div>
                    
                    <div onclick="window.open('https://curator-ai.foodzie.store', '_blank')" class="flex flex-col items-center gap-1.5 group cursor-pointer">
                        <div class="w-[60px] h-[60px] rounded-[14px] bg-gradient-to-br from-slate-800 to-black border border-white/20 flex items-center justify-center shadow-md group-hover:scale-105 transition-transform">
                            <iconify-icon icon="solar:cpu-bold" width="36" class="text-purple-400"></iconify-icon>
                        </div>
                        <span class="text-white text-[11px] font-medium drop-shadow-md">Curator AI</span>
                    </div>
                    
                    <div onclick="window.open('https://foodzie.store', '_blank')" class="flex flex-col items-center gap-1.5 group cursor-pointer">
                        <div class="w-[60px] h-[60px] rounded-[14px] bg-gradient-to-br from-orange-500 to-red-600 border border-white/20 flex items-center justify-center shadow-md group-hover:scale-105 transition-transform">
                            <iconify-icon icon="solar:shop-bold" width="36" class="text-white"></iconify-icon>
                        </div>
                        <span class="text-white text-[11px] font-medium drop-shadow-md">Foodzie</span>
                    </div>

                    <div id="btn-open-camera" class="flex flex-col items-center gap-1.5 group cursor-pointer">
                        <div class="w-[60px] h-[60px] rounded-[14px] bg-gradient-to-br from-gray-300 to-gray-400 border border-white/20 flex items-center justify-center shadow-md group-hover:scale-105 transition-transform">
                            <iconify-icon icon="solar:camera-bold" width="36" class="text-slate-800"></iconify-icon>
                        </div>
                        <span class="text-white text-[11px] font-medium drop-shadow-md">Camera</span>
                    </div>
                    
                    <div id="btn-open-gallery" class="flex flex-col items-center gap-1.5 group cursor-pointer">
                        <div class="w-[60px] h-[60px] rounded-[14px] bg-white border border-white/20 flex items-center justify-center shadow-md group-hover:scale-105 transition-transform overflow-hidden relative">
                            <div class="absolute inset-0 bg-gradient-to-tr from-yellow-400 via-orange-500 to-pink-500 opacity-20"></div>
                            <iconify-icon icon="solar:gallery-bold" width="36" class="text-transparent bg-clip-text bg-gradient-to-br from-yellow-400 via-red-500 to-indigo-500 relative z-10"></iconify-icon>
                        </div>
                        <span class="text-white text-[11px] font-medium drop-shadow-md">Photos</span>
                    </div>
                </div>
                
                """

idx1 = html.find(start_marker)
idx2 = html.find(end_marker)
html = html[:idx1] + new_apps_grid + html[idx2:]

# 2. Update Bottom Dock to use onclick
old_dock = """<!-- Bottom Dock -->
                <div class="absolute bottom-6 left-4 right-4 h-[84px] bg-white/20 backdrop-blur-2xl border border-white/30 rounded-[28px] flex items-center justify-around px-2 z-20">
                    <div class="w-[60px] h-[60px] rounded-[14px] bg-green-500 flex items-center justify-center cursor-pointer shadow-md">
                        <iconify-icon icon="solar:phone-bold" width="32" class="text-white"></iconify-icon>
                    </div>
                    <div class="w-[60px] h-[60px] rounded-[14px] bg-blue-500 flex items-center justify-center cursor-pointer shadow-md">
                        <iconify-icon icon="solar:chat-round-bold" width="32" class="text-white"></iconify-icon>
                    </div>
                    <a href="https://github.com/Jaspreet-Bhatia-SI" target="_blank" class="w-[60px] h-[60px] rounded-[14px] bg-indigo-500 flex items-center justify-center cursor-pointer shadow-md">
                        <iconify-icon icon="solar:safari-bold" width="36" class="text-white"></iconify-icon>
                    </a>
                </div>"""
new_dock = """<!-- Bottom Dock -->
                <div class="absolute bottom-6 left-4 right-4 h-[84px] bg-white/20 backdrop-blur-2xl border border-white/30 rounded-[28px] flex items-center justify-around px-2 z-20">
                    <div onclick="window.open('mailto:bhatiajaspreet161@gmail.com', '_blank')" class="w-[60px] h-[60px] rounded-[14px] bg-green-500 flex items-center justify-center cursor-pointer shadow-md hover:scale-105 transition-transform">
                        <iconify-icon icon="solar:phone-bold" width="32" class="text-white"></iconify-icon>
                    </div>
                    <div onclick="window.open('https://linkedin.com/in/jaspreet-bhatia-si', '_blank')" class="w-[60px] h-[60px] rounded-[14px] bg-blue-500 flex items-center justify-center cursor-pointer shadow-md hover:scale-105 transition-transform">
                        <iconify-icon icon="solar:chat-round-bold" width="32" class="text-white"></iconify-icon>
                    </div>
                    <div onclick="window.open('https://github.com/Jaspreet-Bhatia-SI', '_blank')" class="w-[60px] h-[60px] rounded-[14px] bg-indigo-500 flex items-center justify-center cursor-pointer shadow-md hover:scale-105 transition-transform">
                        <iconify-icon icon="solar:safari-bold" width="36" class="text-white"></iconify-icon>
                    </div>
                </div>"""
html = html.replace(old_dock, new_dock)

with open('portfolio.html', 'w') as f:
    f.write(html)
print("Updated app links to div onclick")
