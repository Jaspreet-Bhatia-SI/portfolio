import re

with open('portfolio.html', 'r') as f:
    html = f.read()

# 1. HTML Overlay
html_injection = """
    <!-- Contacts Toggle Button -->
    <button id="btn-contacts" class="hidden pointer-events-auto absolute bottom-32 right-6 md:right-8 bg-slate-900/90 backdrop-blur border border-indigo-500/30 p-4 rounded-full shadow-[0_0_30px_rgba(79,70,229,0.4)] text-white hover:bg-slate-800 transition-all hover:scale-110 active:scale-95 z-[90]">
        <iconify-icon icon="solar:phone-calling-bold" width="28" class="text-indigo-400"></iconify-icon>
    </button>

    <!-- Phone UI Overlay -->
    <div id="phone-ui" class="hidden fixed inset-0 z-[150] bg-black/60 backdrop-blur-sm flex items-center justify-center p-4 opacity-0 pointer-events-none transition-opacity duration-300">
        <div class="relative w-full max-w-[320px] h-[640px] bg-black rounded-[40px] border-[8px] border-slate-800 shadow-[0_0_50px_rgba(79,70,229,0.5)] flex flex-col transform scale-95 transition-transform duration-300 pointer-events-auto" id="phone-frame">
            <!-- Notch -->
            <div class="absolute top-0 left-1/2 -translate-x-1/2 w-32 h-7 bg-slate-800 rounded-b-xl z-20 flex justify-center items-center gap-2">
                <div class="w-1.5 h-1.5 rounded-full bg-blue-900/50"></div>
                <div class="w-12 h-1.5 rounded-full bg-slate-900"></div>
            </div>
            
            <!-- Screen Content -->
            <div class="flex-1 bg-gradient-to-b from-indigo-950 to-black rounded-[32px] overflow-hidden flex flex-col items-center pt-16 p-6 relative">
                <button id="btn-close-phone" class="absolute top-6 right-6 text-white/50 hover:text-white transition-colors cursor-pointer z-30">
                    <iconify-icon icon="solar:close-circle-bold" width="26"></iconify-icon>
                </button>
                
                <!-- Avatar & Status -->
                <div class="relative">
                    <div class="w-24 h-24 rounded-full bg-gradient-to-br from-indigo-500 to-purple-600 border-4 border-slate-900 mb-4 flex items-center justify-center shadow-2xl overflow-hidden">
                        <img src="profile.jpg" class="w-full h-full object-cover opacity-90 mix-blend-luminosity" onerror="this.style.display='none'">
                        <span class="absolute text-3xl font-bold text-white tracking-widest">JB</span>
                    </div>
                    <div class="absolute bottom-4 right-1 w-5 h-5 bg-green-500 border-4 border-slate-900 rounded-full animate-pulse"></div>
                </div>
                
                <h2 class="text-2xl font-bold text-white mb-1">Jaspreet Bhatia</h2>
                <p class="text-indigo-400 text-sm mb-6 font-mono font-medium tracking-wide bg-indigo-500/10 px-3 py-1 rounded-full border border-indigo-500/20">Software Engineer</p>

                <!-- Social Links -->
                <div class="w-full flex flex-col gap-3 z-30">
                    <a href="mailto:bhatiajaspreet161@gmail.com" target="_blank" class="flex items-center gap-4 bg-slate-800/50 hover:bg-slate-700/80 p-4 rounded-2xl transition-all border border-white/5 hover:border-red-400/30 group">
                        <div class="w-10 h-10 rounded-xl bg-red-500/20 flex items-center justify-center group-hover:scale-110 transition-transform">
                            <iconify-icon icon="solar:letter-bold" width="22" class="text-red-400"></iconify-icon>
                        </div>
                        <div class="flex flex-col">
                            <span class="font-bold text-white text-sm">Email</span>
                            <span class="text-xs text-slate-400 font-mono line-clamp-1">bhatiajaspreet161@...</span>
                        </div>
                    </a>
                    
                    <a href="https://linkedin.com/in/jaspreet-bhatia-si" target="_blank" class="flex items-center gap-4 bg-slate-800/50 hover:bg-slate-700/80 p-4 rounded-2xl transition-all border border-white/5 hover:border-blue-400/30 group">
                        <div class="w-10 h-10 rounded-xl bg-blue-500/20 flex items-center justify-center group-hover:scale-110 transition-transform">
                            <iconify-icon icon="mdi:linkedin" width="24" class="text-blue-400"></iconify-icon>
                        </div>
                        <div class="flex flex-col">
                            <span class="font-bold text-white text-sm">LinkedIn</span>
                            <span class="text-xs text-slate-400 font-mono">jaspreet-bhatia-si</span>
                        </div>
                    </a>
                    
                    <a href="https://instagram.com/jass_bhatia.si" target="_blank" class="flex items-center gap-4 bg-slate-800/50 hover:bg-slate-700/80 p-4 rounded-2xl transition-all border border-white/5 hover:border-pink-400/30 group">
                        <div class="w-10 h-10 rounded-xl bg-pink-500/20 flex items-center justify-center group-hover:scale-110 transition-transform">
                            <iconify-icon icon="mdi:instagram" width="24" class="text-pink-400"></iconify-icon>
                        </div>
                        <div class="flex flex-col">
                            <span class="font-bold text-white text-sm">Instagram</span>
                            <span class="text-xs text-slate-400 font-mono">@jass_bhatia.si</span>
                        </div>
                    </a>
                    
                    <a href="https://github.com/Jaspreet-Bhatia-SI" target="_blank" class="flex items-center gap-4 bg-slate-800/50 hover:bg-slate-700/80 p-4 rounded-2xl transition-all border border-white/5 hover:border-slate-300/30 group">
                        <div class="w-10 h-10 rounded-xl bg-slate-600/30 flex items-center justify-center group-hover:scale-110 transition-transform">
                            <iconify-icon icon="mdi:github" width="24" class="text-slate-300"></iconify-icon>
                        </div>
                        <div class="flex flex-col">
                            <span class="font-bold text-white text-sm">GitHub</span>
                            <span class="text-xs text-slate-400 font-mono">Jaspreet-Bhatia-SI</span>
                        </div>
                    </a>
                </div>
            </div>
        </div>
    </div>
"""

target_html = "<!-- Virtual Joystick -->"
if target_html in html and "id=\"phone-ui\"" not in html:
    html = html.replace(target_html, html_injection + "\n    " + target_html)


# 2. JS Logic (Variables & Event Listeners)
js_injection = """
        let hasContact = false;
        const btnContacts = document.getElementById('btn-contacts');
        const phoneUI = document.getElementById('phone-ui');
        const phoneFrame = document.getElementById('phone-frame');
        
        function togglePhone() {
            const isHidden = phoneUI.classList.contains('pointer-events-none');
            if(isHidden) {
                phoneUI.classList.remove('hidden');
                requestAnimationFrame(() => {
                    phoneUI.classList.remove('opacity-0', 'pointer-events-none');
                    phoneFrame.classList.remove('scale-95');
                    phoneFrame.classList.add('scale-100');
                });
            } else {
                phoneUI.classList.add('opacity-0', 'pointer-events-none');
                phoneFrame.classList.remove('scale-100');
                phoneFrame.classList.add('scale-95');
                setTimeout(() => phoneUI.classList.add('hidden'), 300);
            }
        }
        btnContacts.addEventListener('click', togglePhone);
        document.getElementById('btn-close-phone').addEventListener('click', togglePhone);
"""
target_js = "window.addEventListener('resize', () => {"
if target_js in html and "let hasContact = false;" not in html:
    html = html.replace(target_js, js_injection + "\n        " + target_js)


# 3. Animation Completion Logic
completion_injection = """
                        if (!hasContact) {
                            hasContact = true;
                            btnContacts.classList.remove('hidden');
                            setTimeout(() => { togglePhone(); }, 800);
                        }
"""
target_loop = "if (state.wasDrivingBeforeShare) {"
if target_loop in html and "!hasContact" not in html:
    html = html.replace(target_loop, completion_injection + "\n                        " + target_loop)

with open('portfolio.html', 'w') as f:
    f.write(html)
print("Injected phone UI")
