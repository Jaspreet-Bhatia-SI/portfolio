import sys

with open('portfolio.html', 'r') as f:
    html = f.read()

# 1. REPLACE HTML OVERLAY
start_html_tag = '<!-- Contacts Toggle Button -->'
end_html_tag = '<!-- Virtual Joystick -->'

new_html = """<!-- Contacts Toggle Button -->
    <button id="btn-contacts" class="hidden pointer-events-auto absolute bottom-32 right-6 md:right-8 bg-white/20 backdrop-blur-md border border-white/40 p-4 rounded-full shadow-[0_4px_30px_rgba(0,0,0,0.1)] text-white hover:bg-white/30 transition-all hover:scale-110 active:scale-95 z-[90]">
        <iconify-icon icon="solar:smartphone-bold" width="28"></iconify-icon>
    </button>

    <!-- Phone UI Overlay (iOS Style) -->
    <div id="phone-ui" class="hidden fixed inset-0 z-[150] bg-black/40 backdrop-blur-md flex items-center justify-center p-4 opacity-0 pointer-events-none transition-opacity duration-500">
        <!-- Phone Frame -->
        <div class="relative w-full max-w-[340px] h-[680px] bg-black rounded-[50px] border-[12px] border-black shadow-[0_20px_50px_rgba(0,0,0,0.5)] flex flex-col transform scale-[0.2] translate-y-32 opacity-0 transition-all duration-500 pointer-events-auto overflow-hidden" id="phone-frame">
            
            <!-- Dynamic Island / Notch -->
            <div class="absolute top-2 left-1/2 -translate-x-1/2 w-28 h-7 bg-black rounded-full z-30 flex justify-between items-center px-2">
                <div class="w-2 h-2 rounded-full bg-blue-900/50"></div>
                <div class="w-1.5 h-1.5 rounded-full bg-emerald-500/50"></div>
            </div>

            <!-- Screen Content (iOS Wallpaper) -->
            <div class="flex-1 bg-gradient-to-br from-[#2E3192] to-[#1BFFFF] relative flex flex-col font-sans">
                
                <!-- Status Bar -->
                <div class="w-full h-12 pt-2 px-6 flex justify-between items-center text-white text-[13px] font-semibold z-20">
                    <span id="phone-time">9:41</span>
                    <div class="flex items-center gap-1.5">
                        <iconify-icon icon="solar:check-circle-bold" width="14"></iconify-icon>
                        <iconify-icon icon="solar:wifi-bold" width="14"></iconify-icon>
                        <iconify-icon icon="solar:battery-charge-bold" width="16"></iconify-icon>
                    </div>
                </div>
                
                <button id="btn-close-phone" class="absolute top-14 right-4 bg-black/20 hover:bg-black/40 text-white rounded-full p-2 backdrop-blur-md transition-colors z-40">
                    <iconify-icon icon="solar:close-circle-bold" width="22"></iconify-icon>
                </button>

                <!-- Search Widget -->
                <div class="mt-6 mx-4 relative z-30">
                    <div class="bg-white/20 backdrop-blur-xl border border-white/30 rounded-2xl p-3 flex items-center gap-3 cursor-text shadow-lg hover:bg-white/30 transition-colors" id="search-widget-btn">
                        <iconify-icon icon="solar:magnifer-linear" width="20" class="text-white"></iconify-icon>
                        <span class="text-white/80 text-sm font-medium flex-1 text-left">Search or ask...</span>
                        <iconify-icon icon="solar:microphone-2-bold" width="20" class="text-white"></iconify-icon>
                    </div>
                </div>

                <!-- Apps Grid -->
                <div class="mt-10 px-6 grid grid-cols-4 gap-y-8 gap-x-4 z-20">
                    <!-- Mail -->
                    <a href="mailto:bhatiajaspreet161@gmail.com" target="_blank" class="flex flex-col items-center gap-1.5 group">
                        <div class="w-[60px] h-[60px] rounded-[14px] bg-gradient-to-b from-[#5ac8fa] to-[#007aff] flex items-center justify-center shadow-md group-hover:scale-105 transition-transform">
                            <iconify-icon icon="solar:letter-bold" width="34" class="text-white"></iconify-icon>
                        </div>
                        <span class="text-white text-[11px] font-medium drop-shadow-md">Mail</span>
                    </a>
                    
                    <!-- LinkedIn -->
                    <a href="https://linkedin.com/in/jaspreet-bhatia-si" target="_blank" class="flex flex-col items-center gap-1.5 group">
                        <div class="w-[60px] h-[60px] rounded-[14px] bg-[#0077b5] flex items-center justify-center shadow-md group-hover:scale-105 transition-transform">
                            <iconify-icon icon="mdi:linkedin" width="40" class="text-white"></iconify-icon>
                        </div>
                        <span class="text-white text-[11px] font-medium drop-shadow-md">LinkedIn</span>
                    </a>
                    
                    <!-- Instagram -->
                    <a href="https://instagram.com/jass_bhatia.si" target="_blank" class="flex flex-col items-center gap-1.5 group">
                        <div class="w-[60px] h-[60px] rounded-[14px] bg-gradient-to-tr from-[#f09433] via-[#dc2743] to-[#bc1888] flex items-center justify-center shadow-md group-hover:scale-105 transition-transform">
                            <iconify-icon icon="mdi:instagram" width="38" class="text-white"></iconify-icon>
                        </div>
                        <span class="text-white text-[11px] font-medium drop-shadow-md">Instagram</span>
                    </a>
                    
                    <!-- GitHub -->
                    <a href="https://github.com/Jaspreet-Bhatia-SI" target="_blank" class="flex flex-col items-center gap-1.5 group">
                        <div class="w-[60px] h-[60px] rounded-[14px] bg-white flex items-center justify-center shadow-md group-hover:scale-105 transition-transform">
                            <iconify-icon icon="mdi:github" width="40" class="text-[#181717]"></iconify-icon>
                        </div>
                        <span class="text-white text-[11px] font-medium drop-shadow-md">GitHub</span>
                    </a>
                    
                    <!-- Curator AI (Custom App) -->
                    <a href="https://portfolio.foodzie.store" target="_blank" class="flex flex-col items-center gap-1.5 group">
                        <div class="w-[60px] h-[60px] rounded-[14px] bg-gradient-to-br from-slate-800 to-black border border-white/20 flex items-center justify-center shadow-md group-hover:scale-105 transition-transform">
                            <iconify-icon icon="solar:cpu-bold" width="36" class="text-purple-400"></iconify-icon>
                        </div>
                        <span class="text-white text-[11px] font-medium drop-shadow-md">Curator AI</span>
                    </a>
                </div>
                
                <!-- Bottom Dock -->
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
                </div>

                <!-- Spotlight Search Overlay -->
                <div id="spotlight-overlay" class="absolute inset-0 bg-white/40 backdrop-blur-3xl z-50 transform translate-y-full transition-transform duration-300 flex flex-col pt-12">
                    <div class="px-4 pb-4">
                        <div class="flex items-center gap-3 bg-white/60 rounded-xl p-2 px-3 shadow-sm border border-white/50">
                            <iconify-icon icon="solar:magnifer-linear" width="20" class="text-slate-500"></iconify-icon>
                            <input type="text" id="spotlight-input" class="bg-transparent flex-1 outline-none text-slate-800 font-medium placeholder-slate-500" placeholder="Search Jaspreet...">
                            <button id="btn-cancel-search" class="text-blue-600 font-medium text-sm px-1">Cancel</button>
                        </div>
                    </div>
                    <div class="flex-1 overflow-y-auto px-4 pb-10" id="spotlight-results">
                        <!-- Default Suggestions -->
                        <div class="text-xs font-bold text-slate-500 uppercase tracking-wider mb-2 ml-1">Suggestions</div>
                        <div class="bg-white/60 rounded-2xl overflow-hidden border border-white/50 flex flex-col">
                            <div class="search-item p-3 border-b border-white/50 flex items-center gap-3 cursor-pointer hover:bg-white/80 transition-colors" data-url="https://linkedin.com/in/jaspreet-bhatia-si">
                                <div class="bg-blue-500 text-white p-1.5 rounded-lg"><iconify-icon icon="mdi:linkedin" width="18"></iconify-icon></div>
                                <span class="font-medium text-slate-800 text-sm">Jaspreet's LinkedIn</span>
                            </div>
                            <div class="search-item p-3 border-b border-white/50 flex items-center gap-3 cursor-pointer hover:bg-white/80 transition-colors" data-url="https://instagram.com/jass_bhatia.si">
                                <div class="bg-gradient-to-tr from-[#f09433] to-[#bc1888] text-white p-1.5 rounded-lg"><iconify-icon icon="mdi:instagram" width="18"></iconify-icon></div>
                                <span class="font-medium text-slate-800 text-sm">Jaspreet's Instagram</span>
                            </div>
                            <div class="search-item p-3 border-b border-white/50 flex items-center gap-3 cursor-pointer hover:bg-white/80 transition-colors" data-url="mailto:bhatiajaspreet161@gmail.com">
                                <div class="bg-red-500 text-white p-1.5 rounded-lg"><iconify-icon icon="solar:letter-bold" width="18"></iconify-icon></div>
                                <span class="font-medium text-slate-800 text-sm">Email Jaspreet</span>
                            </div>
                            <div class="search-item p-3 flex items-center gap-3 cursor-pointer hover:bg-white/80 transition-colors" data-url="https://github.com/Jaspreet-Bhatia-SI">
                                <div class="bg-slate-800 text-white p-1.5 rounded-lg"><iconify-icon icon="solar:cpu-bold" width="18"></iconify-icon></div>
                                <span class="font-medium text-slate-800 text-sm">Curator AI Project</span>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>
    <!-- Virtual Joystick -->"""

start_idx = html.find(start_html_tag)
end_idx = html.find(end_html_tag)
html = html[:start_idx] + new_html + html[end_idx + len(end_html_tag):]


# 2. REPLACE btnShare listener block (Remove 3D card creation)
btn_start = "btnShare.addEventListener('click', () => {"
btn_end = "window.addEventListener('keydown', (e) => {"
new_btn_logic = """btnShare.addEventListener('click', () => {
            if(!state.activeNPC || state.mode === 'SHARING') return;
            state.wasDrivingBeforeShare = (state.mode === 'DRIVING');
            if(state.wasDrivingBeforeShare) {
                // Exit car
                state.mode = 'WALKING'; modeText.innerText = 'SURVIVOR [SHARING]';
                const npcSideX = state.activeNPC.grp.position.x > carGroup.position.x ? 3 : -3;
                const npcSideZ = state.activeNPC.grp.position.z > carGroup.position.z ? 3 : -3;
                playerGroup.position.set(carGroup.position.x + npcSideX, 0, carGroup.position.z + npcSideZ);
                playerGroup.visible = true;
            } else {
                modeText.innerText = 'SURVIVOR [SHARING]';
            }
            state.mode = 'SHARING';
            state.shareTimer = 0;
            state.activeNPC.state = 'sharing';
            
            // Show phones
            playerGroup.userData.rArm.children.forEach(c => { if(c.geometry === phoneGeo) c.visible = true; });
            state.activeNPC.rArm.children.forEach(c => { if(c.geometry === phoneGeo) c.visible = true; });

            btnShare.classList.add('hidden', 'opacity-0');
            
            // Snap camera to side view
            const angleBetween = Math.atan2(state.activeNPC.grp.position.x - playerGroup.position.x, state.activeNPC.grp.position.z - playerGroup.position.z);
            camTheta = angleBetween + Math.PI/2;
            camPhi = Math.PI / 3;
        });

        """
idx1 = html.find(btn_start)
idx2 = html.find(btn_end)
html = html[:idx1] + new_btn_logic + html[idx2:]


# 3. REPLACE SHARING ANIMATION LOOP
loop_start = "else if (state.mode === 'SHARING') {"
loop_end = "else if (state.mode === 'TRANSITION') {"
new_loop_logic = """else if (state.mode === 'SHARING') {
                const npc = state.activeNPC;
                state.shareTimer += 0.02;
                const t = state.shareTimer;
                
                const pt = Math.atan2(playerGroup.position.x - npc.grp.position.x, playerGroup.position.z - npc.grp.position.z);
                const nt = Math.atan2(npc.grp.position.x - playerGroup.position.x, npc.grp.position.z - playerGroup.position.z);
                
                playerGroup.userData.lLeg.rotation.x = 0; playerGroup.userData.rLeg.rotation.x = 0;
                playerGroup.userData.lArm.rotation.x = 0; 
                npc.lLeg.rotation.x = 0; npc.rLeg.rotation.x = 0;
                npc.lArm.rotation.x = 0;

                const dpy = nt - playerGroup.rotation.y;
                playerGroup.rotation.y += Math.atan2(Math.sin(dpy), Math.cos(dpy)) * 0.1;
                const dny = pt - npc.grp.rotation.y;
                npc.grp.rotation.y += Math.atan2(Math.sin(dny), Math.cos(dny)) * 0.1;

                if(t < 1.5) {
                    playerGroup.userData.rArm.rotation.x += (-Math.PI/2 - playerGroup.userData.rArm.rotation.x) * 0.1;
                    npc.rArm.rotation.x += (-Math.PI/2 - npc.rArm.rotation.x) * 0.1;
                } else if (t >= 1.5 && t < 1.55) {
                    // Trigger the phone UI popout immediately!
                    if (!hasContact) {
                        hasContact = true;
                        document.getElementById('btn-contacts').classList.remove('hidden');
                        togglePhone(); 
                    }
                } else if (t > 2.5) {
                    playerGroup.userData.rArm.rotation.x += (0 - playerGroup.userData.rArm.rotation.x) * 0.1;
                    npc.rArm.rotation.x += (0 - npc.rArm.rotation.x) * 0.1;
                    
                    if(t > 3.5) {
                        playerGroup.userData.rArm.children.forEach(c => { if(c.geometry === phoneGeo) c.visible = false; });
                        npc.rArm.children.forEach(c => { if(c.geometry === phoneGeo) c.visible = false; });
                        npc.state = 'idle';
                        if (state.wasDrivingBeforeShare) {
                            state.mode = 'DRIVING'; modeText.innerText = 'SURVIVOR [DRIVING]';
                            playerGroup.visible = false;
                        } else {
                            state.mode = 'WALKING'; modeText.innerText = 'SURVIVOR [ON FOOT]';
                        }
                    }
                }
                
                const midX = (playerGroup.position.x + npc.grp.position.x) / 2;
                const midZ = (playerGroup.position.z + npc.grp.position.z) / 2;
                const target = new THREE.Vector3(midX, playerGroup.position.y + 1.5, midZ);
                
                const radius = 6;
                const idealCamera = target.clone().add(new THREE.Vector3(
                    Math.sin(camTheta) * Math.sin(camPhi) * radius,
                    Math.cos(camPhi) * radius,
                    Math.cos(camTheta) * Math.sin(camPhi) * radius
                ));
                camera.position.lerp(idealCamera, 0.1);
                camera.lookAt(target);
            }
            """
lidx1 = html.find(loop_start)
lidx2 = html.find(loop_end)
html = html[:lidx1] + new_loop_logic + html[lidx2:]


# 4. REPLACE togglePhone & add Spotlight logic
js_start = "let hasContact = false;"
js_end = "document.getElementById('btn-close-phone').addEventListener('click', togglePhone);"
new_js_logic = """let hasContact = false;
        const btnContacts = document.getElementById('btn-contacts');
        const phoneUI = document.getElementById('phone-ui');
        const phoneFrame = document.getElementById('phone-frame');
        const timeEl = document.getElementById('phone-time');
        
        setInterval(() => {
            const d = new Date();
            timeEl.innerText = d.getHours() + ':' + d.getMinutes().toString().padStart(2, '0');
        }, 1000);
        
        function togglePhone() {
            const isHidden = phoneUI.classList.contains('pointer-events-none');
            if(isHidden) {
                phoneUI.classList.remove('hidden');
                requestAnimationFrame(() => {
                    phoneUI.classList.remove('opacity-0', 'pointer-events-none');
                    phoneFrame.classList.remove('scale-[0.2]', 'translate-y-32', 'opacity-0');
                    phoneFrame.classList.add('scale-100', 'translate-y-0', 'opacity-100');
                });
            } else {
                phoneUI.classList.add('opacity-0', 'pointer-events-none');
                phoneFrame.classList.remove('scale-100', 'translate-y-0', 'opacity-100');
                phoneFrame.classList.add('scale-[0.2]', 'translate-y-32', 'opacity-0');
                setTimeout(() => phoneUI.classList.add('hidden'), 500);
                document.getElementById('spotlight-overlay').classList.add('translate-y-full');
            }
        }
        btnContacts.addEventListener('click', togglePhone);
        document.getElementById('btn-close-phone').addEventListener('click', togglePhone);
        phoneFrame.addEventListener('mousedown', e => e.stopPropagation());
        phoneFrame.addEventListener('touchstart', e => e.stopPropagation());

        // Spotlight Search Logic
        const spotlightBtn = document.getElementById('search-widget-btn');
        const spotlightOverlay = document.getElementById('spotlight-overlay');
        const spotlightInput = document.getElementById('spotlight-input');
        const btnCancelSearch = document.getElementById('btn-cancel-search');
        const spotlightResults = document.getElementById('spotlight-results');
        
        spotlightBtn.addEventListener('click', () => {
            spotlightOverlay.classList.remove('translate-y-full');
            setTimeout(() => spotlightInput.focus(), 300);
        });
        btnCancelSearch.addEventListener('click', () => {
            spotlightOverlay.classList.add('translate-y-full');
            spotlightInput.value = '';
            resetSearch();
        });

        const defaultSuggestionsHtml = spotlightResults.innerHTML;
        
        function resetSearch() {
            spotlightResults.innerHTML = defaultSuggestionsHtml;
            document.querySelectorAll('.search-item').forEach(item => {
                item.addEventListener('click', () => { window.open(item.dataset.url, '_blank'); });
            });
        }
        resetSearch();

        spotlightInput.addEventListener('input', (e) => {
            const val = e.target.value.toLowerCase();
            if(!val) { resetSearch(); return; }
            
            const aiResponses = [
                { match: ['who', 'about', 'info'], text: 'Jaspreet Bhatia (JBSI) is a Software Engineer building highly interactive web apps and 3D experiences.' },
                { match: ['skills', 'tech', 'stack'], text: 'Proficient in modern web (React, Tailwind), 3D (Three.js), and AI agents.' },
                { match: ['hire', 'contact', 'reach'], text: 'You can reach out via Email or LinkedIn (see icons below)!' },
                { match: ['curator', 'ai'], text: 'Curator AI is a flagship project utilizing LLMs for automated content discovery.' }
            ];
            
            let found = false;
            for(const res of aiResponses) {
                if(res.match.some(m => val.includes(m))) {
                    spotlightResults.innerHTML = `
                        <div class="bg-white/60 rounded-2xl p-4 border border-white/50 shadow-sm mb-4">
                            <div class="flex items-center gap-2 mb-2">
                                <iconify-icon icon="solar:magic-stick-3-bold" class="text-purple-500"></iconify-icon>
                                <span class="text-xs font-bold text-slate-500 uppercase tracking-wider">AI Answer</span>
                            </div>
                            <p class="text-sm text-slate-800 font-medium leading-relaxed">${res.text}</p>
                        </div>
                        <div class="flex gap-2">
                            <button onclick="window.open('https://linkedin.com/in/jaspreet-bhatia-si')" class="flex-1 bg-blue-500 text-white p-2 rounded-xl text-xs font-bold shadow-sm">LinkedIn</button>
                            <button onclick="window.open('mailto:bhatiajaspreet161@gmail.com')" class="flex-1 bg-red-500 text-white p-2 rounded-xl text-xs font-bold shadow-sm">Email</button>
                        </div>
                    `;
                    found = true; break;
                }
            }
            if(!found) {
                spotlightResults.innerHTML = `
                    <div class="text-center text-slate-500 mt-8 font-medium">
                        <iconify-icon icon="solar:magnifer-linear" width="32" class="mb-2 opacity-50"></iconify-icon>
                        <p class="text-sm">Press Enter to search Web for "${val}"</p>
                    </div>
                `;
            }
        });
        
        spotlightInput.addEventListener('keydown', (e) => {
            if(e.key === 'Enter') {
                const val = e.target.value;
                window.open('https://google.com/search?q=' + encodeURIComponent(val + ' Jaspreet Bhatia'), '_blank');
            }
        });
"""
jidx1 = html.find(js_start)
# we need to find the end of the previous togglePhone block, I added stopPropagation in the previous patch.
jidx2 = html.find("phoneFrame.addEventListener('touchstart', e => e.stopPropagation());") + len("phoneFrame.addEventListener('touchstart', e => e.stopPropagation());")

html = html[:jidx1] + new_js_logic + html[jidx2:]

with open('portfolio.html', 'w') as f:
    f.write(html)
print("Updated iOS Phone")
