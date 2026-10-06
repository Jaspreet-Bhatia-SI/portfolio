import re

with open('portfolio.html', 'r') as f:
    html = f.read()

# 1. Update Apps Grid
target_grid = """                    <a href="https://portfolio.foodzie.store" target="_blank" class="flex flex-col items-center gap-1.5 group">
                        <div class="w-[60px] h-[60px] rounded-[14px] bg-gradient-to-br from-slate-800 to-black border border-white/20 flex items-center justify-center shadow-md group-hover:scale-105 transition-transform">
                            <iconify-icon icon="solar:cpu-bold" width="36" class="text-purple-400"></iconify-icon>
                        </div>
                        <span class="text-white text-[11px] font-medium drop-shadow-md">Curator AI</span>
                    </a>
                </div>"""

new_grid = """                    <a href="https://portfolio.foodzie.store" target="_blank" class="flex flex-col items-center gap-1.5 group">
                        <div class="w-[60px] h-[60px] rounded-[14px] bg-gradient-to-br from-slate-800 to-black border border-white/20 flex items-center justify-center shadow-md group-hover:scale-105 transition-transform">
                            <iconify-icon icon="solar:cpu-bold" width="36" class="text-purple-400"></iconify-icon>
                        </div>
                        <span class="text-white text-[11px] font-medium drop-shadow-md">Curator AI</span>
                    </a>
                    
                    <!-- Camera App -->
                    <div id="btn-open-camera" class="flex flex-col items-center gap-1.5 group cursor-pointer">
                        <div class="w-[60px] h-[60px] rounded-[14px] bg-gradient-to-br from-gray-300 to-gray-400 border border-white/20 flex items-center justify-center shadow-md group-hover:scale-105 transition-transform">
                            <iconify-icon icon="solar:camera-bold" width="36" class="text-slate-800"></iconify-icon>
                        </div>
                        <span class="text-white text-[11px] font-medium drop-shadow-md">Camera</span>
                    </div>
                    
                    <!-- Gallery App -->
                    <div id="btn-open-gallery" class="flex flex-col items-center gap-1.5 group cursor-pointer">
                        <div class="w-[60px] h-[60px] rounded-[14px] bg-white border border-white/20 flex items-center justify-center shadow-md group-hover:scale-105 transition-transform overflow-hidden relative">
                            <div class="absolute inset-0 bg-gradient-to-tr from-yellow-400 via-orange-500 to-pink-500 opacity-20"></div>
                            <iconify-icon icon="solar:gallery-bold" width="36" class="text-transparent bg-clip-text bg-gradient-to-br from-yellow-400 via-red-500 to-indigo-500 relative z-10"></iconify-icon>
                        </div>
                        <span class="text-white text-[11px] font-medium drop-shadow-md">Photos</span>
                    </div>
                </div>"""

html = html.replace(target_grid, new_grid)

# 2. Add App Overlays
target_spotlight = "<!-- Spotlight Search Overlay -->"
new_overlays = """<!-- Camera App Overlay -->
                <div id="camera-app" class="absolute inset-0 bg-black z-50 transform translate-y-full transition-transform duration-300 flex flex-col">
                    <div class="h-16 flex items-center px-4 pt-4 bg-gradient-to-b from-black/80 to-transparent absolute top-0 w-full z-10">
                        <button id="btn-close-camera" class="text-white hover:text-slate-300 transition-colors"><iconify-icon icon="solar:alt-arrow-left-linear" width="28"></iconify-icon></button>
                    </div>
                    <video id="camera-feed" class="w-full h-full object-cover" autoplay playsinline></video>
                    <div id="camera-flash" class="absolute inset-0 bg-white opacity-0 pointer-events-none transition-opacity duration-100 z-20"></div>
                    <div class="h-32 bg-black/80 absolute bottom-0 w-full flex items-center justify-center z-10">
                        <button id="btn-capture" class="w-16 h-16 rounded-full border-[4px] border-white flex items-center justify-center cursor-pointer active:scale-95 transition-transform">
                            <div class="w-[52px] h-[52px] bg-white rounded-full"></div>
                        </button>
                    </div>
                </div>

                <!-- Gallery App Overlay -->
                <div id="gallery-app" class="absolute inset-0 bg-white z-50 transform translate-y-full transition-transform duration-300 flex flex-col">
                    <div class="h-16 flex items-center justify-between px-4 pt-4 bg-white/90 backdrop-blur border-b border-slate-200 z-10">
                        <button id="btn-close-gallery" class="text-blue-500 flex items-center font-medium active:opacity-50"><iconify-icon icon="solar:alt-arrow-left-linear" width="24" class="mr-1"></iconify-icon> Home</button>
                        <span class="font-bold text-slate-800 text-[15px]">Photos</span>
                        <div class="w-[70px]"></div>
                    </div>
                    <div id="gallery-grid" class="flex-1 overflow-y-auto grid grid-cols-3 gap-1 content-start bg-white p-1">
                        <!-- photos will appear here -->
                    </div>
                </div>

                <!-- Spotlight Search Overlay -->"""
html = html.replace(target_spotlight, new_overlays)

# 3. Add JS Logic at the end of the script (before </script>)
js_logic = """
        // --- Camera & Gallery Logic ---
        window.galleryImages = [];
        window.cameraStream = null;

        const btnOpenCamera = document.getElementById('btn-open-camera');
        const btnOpenGallery = document.getElementById('btn-open-gallery');
        const cameraApp = document.getElementById('camera-app');
        const galleryApp = document.getElementById('gallery-app');
        const btnCloseCamera = document.getElementById('btn-close-camera');
        const btnCloseGallery = document.getElementById('btn-close-gallery');
        const cameraFeed = document.getElementById('camera-feed');
        const btnCapture = document.getElementById('btn-capture');
        const cameraFlash = document.getElementById('camera-flash');
        const galleryGrid = document.getElementById('gallery-grid');

        if(btnOpenCamera) {
            btnOpenCamera.addEventListener('click', async () => {
                cameraApp.classList.remove('translate-y-full');
                try {
                    window.cameraStream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } });
                    cameraFeed.srcObject = window.cameraStream;
                } catch (err) {
                    console.error("Camera access denied or unavailable", err);
                    alert("Camera access denied or device has no camera.");
                }
            });
        }

        if(btnCloseCamera) {
            btnCloseCamera.addEventListener('click', () => {
                cameraApp.classList.add('translate-y-full');
                if(window.cameraStream) {
                    window.cameraStream.getTracks().forEach(t => t.stop());
                    window.cameraStream = null;
                }
            });
        }

        if(btnCapture) {
            btnCapture.addEventListener('click', () => {
                if(!window.cameraStream) return;
                
                // Flash effect
                cameraFlash.classList.remove('opacity-0');
                cameraFlash.classList.add('opacity-100');
                setTimeout(() => {
                    cameraFlash.classList.remove('opacity-100');
                    cameraFlash.classList.add('opacity-0');
                }, 100);

                // Capture logic
                const canvas = document.createElement('canvas');
                canvas.width = cameraFeed.videoWidth || 480;
                canvas.height = cameraFeed.videoHeight || 640;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(cameraFeed, 0, 0, canvas.width, canvas.height);
                
                const dataUrl = canvas.toDataURL('image/png');
                window.galleryImages.unshift(dataUrl); 
            });
        }

        if(btnOpenGallery) {
            btnOpenGallery.addEventListener('click', () => {
                galleryApp.classList.remove('translate-y-full');
                galleryGrid.innerHTML = '';
                if (window.galleryImages.length === 0) {
                    galleryGrid.innerHTML = '<div class="col-span-3 text-center text-slate-400 mt-12 font-medium text-sm">No Photos or Videos</div>';
                } else {
                    window.galleryImages.forEach(src => {
                        const img = document.createElement('img');
                        img.src = src;
                        img.className = 'w-full aspect-square object-cover bg-slate-200';
                        galleryGrid.appendChild(img);
                    });
                }
            });
        }

        if(btnCloseGallery) {
            btnCloseGallery.addEventListener('click', () => {
                galleryApp.classList.add('translate-y-full');
            });
        }
    </script>
</body>"""

html = html.replace("    </script>\n</body>", js_logic)

# 4. Modify togglePhone to stop camera on general phone close
old_toggle_close = """                setTimeout(() => phoneUI.classList.add('hidden'), 500);
                document.getElementById('spotlight-overlay').classList.add('translate-y-full');
            }"""
new_toggle_close = """                setTimeout(() => phoneUI.classList.add('hidden'), 500);
                document.getElementById('spotlight-overlay').classList.add('translate-y-full');
                const cApp = document.getElementById('camera-app');
                if(cApp) cApp.classList.add('translate-y-full');
                const gApp = document.getElementById('gallery-app');
                if(gApp) gApp.classList.add('translate-y-full');
                if(window.cameraStream) {
                    window.cameraStream.getTracks().forEach(t => t.stop());
                    window.cameraStream = null;
                }
            }"""
html = html.replace(old_toggle_close, new_toggle_close)

with open('portfolio.html', 'w') as f:
    f.write(html)
print("Apps added")
