import re

with open('portfolio.html', 'r') as f:
    html = f.read()

# Fix Curator AI link
html = html.replace("curator-ai.foodzie.store", "curator.foodzie.store")

# Add Foodzie App and Camera App to Apps Grid
# Let's find the closing tag of the apps grid.
# The grid starts at <div class="mt-8 px-5 grid grid-cols-4 gap-y-8 gap-x-3 z-20">
# The last app is Curator AI... let's replace the last app block to append new ones.

apps_grid_pattern = r'(<span class="text-white text-\[11px\] font-medium drop-shadow-md">Curator AI</span>\s*</div>)'

new_apps = r'''\1
                    
                    <div onclick="event.stopPropagation(); window.open('https://foodzie.store', '_blank')" class="flex flex-col items-center gap-1.5 group cursor-pointer">
                        <div class="w-[60px] h-[60px] rounded-[14px] bg-gradient-to-tr from-[#ff9a9e] to-[#fecfef] flex items-center justify-center shadow-md group-hover:scale-105 transition-transform overflow-hidden relative">
                            <iconify-icon icon="solar:hamburger-menu-bold" width="34" class="text-rose-500"></iconify-icon>
                        </div>
                        <span class="text-white text-[11px] font-medium drop-shadow-md">Foodzie</span>
                    </div>

                    <div onclick="event.stopPropagation(); openCameraApp()" class="flex flex-col items-center gap-1.5 group cursor-pointer">
                        <div class="w-[60px] h-[60px] rounded-[14px] bg-[#d1d5db] flex items-center justify-center shadow-md group-hover:scale-105 transition-transform relative">
                            <div class="absolute inset-0 bg-gradient-to-b from-transparent to-black/10 rounded-[14px]"></div>
                            <iconify-icon icon="solar:camera-bold" width="36" class="text-[#374151] z-10"></iconify-icon>
                        </div>
                        <span class="text-white text-[11px] font-medium drop-shadow-md">Camera</span>
                    </div>
'''

html = re.sub(apps_grid_pattern, new_apps, html)

# Add Camera App Modal & Logic
camera_modal = '''
    <!-- Camera App Modal -->
    <div id="camera-modal" class="hidden fixed inset-0 z-[200] bg-black flex flex-col items-center justify-center pointer-events-none opacity-0 transition-opacity duration-300">
        <div class="relative w-full h-full max-w-md bg-black pointer-events-auto flex flex-col">
            <!-- Header -->
            <div class="absolute top-0 inset-x-0 h-24 bg-gradient-to-b from-black/80 to-transparent z-10 flex items-start justify-between px-6 pt-12">
                <button onclick="closeCameraApp()" class="text-white hover:bg-white/20 p-2 rounded-full transition-colors">
                    <iconify-icon icon="solar:arrow-left-outline" width="28"></iconify-icon>
                </button>
            </div>
            
            <!-- Viewfinder -->
            <div class="flex-1 relative bg-gray-900 w-full overflow-hidden flex items-center justify-center">
                <video id="camera-feed" class="w-full h-full object-cover" autoplay playsinline></video>
                <canvas id="camera-canvas" class="hidden"></canvas>
                <!-- Flash Effect -->
                <div id="camera-flash" class="absolute inset-0 bg-white opacity-0 pointer-events-none"></div>
            </div>

            <!-- Controls -->
            <div class="h-40 bg-black w-full flex items-center justify-center gap-12 pb-6">
                <!-- Shutter -->
                <button onclick="takePicture()" class="w-20 h-20 rounded-full border-4 border-white flex items-center justify-center p-1 hover:scale-95 transition-transform focus:outline-none">
                    <div class="w-full h-full bg-white rounded-full"></div>
                </button>
            </div>
            
            <!-- Result preview -->
            <div id="camera-preview-container" class="hidden absolute bottom-44 left-6 border-2 border-white rounded-xl overflow-hidden w-20 h-28 shadow-lg cursor-pointer hover:scale-105 transition-transform" onclick="downloadPicture()">
                <img id="camera-preview" class="w-full h-full object-cover" src="" />
                <div class="absolute inset-0 flex items-center justify-center bg-black/40 opacity-0 hover:opacity-100 transition-opacity">
                    <iconify-icon icon="solar:download-minimalistic-bold" class="text-white" width="24"></iconify-icon>
                </div>
            </div>
        </div>
    </div>
'''

if 'id="camera-modal"' not in html:
    # insert before <script>
    html = html.replace('<script>', camera_modal + '\n<script>')

camera_script = '''
        // --- CAMERA APP LOGIC ---
        let cameraStream = null;
        async function openCameraApp() {
            const modal = document.getElementById('camera-modal');
            const video = document.getElementById('camera-feed');
            modal.classList.remove('hidden');
            // Give time for layout
            setTimeout(() => modal.classList.remove('opacity-0'), 10);
            
            try {
                cameraStream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' }, audio: false });
                video.srcObject = cameraStream;
            } catch (err) {
                console.error("Camera access denied or failed", err);
                alert("Camera access is required. Please grant permissions.");
            }
        }
        window.openCameraApp = openCameraApp;

        function closeCameraApp() {
            const modal = document.getElementById('camera-modal');
            modal.classList.add('opacity-0');
            setTimeout(() => {
                modal.classList.add('hidden');
                if (cameraStream) {
                    cameraStream.getTracks().forEach(t => t.stop());
                    cameraStream = null;
                }
            }, 300);
        }
        window.closeCameraApp = closeCameraApp;

        function takePicture() {
            const video = document.getElementById('camera-feed');
            const canvas = document.getElementById('camera-canvas');
            const flash = document.getElementById('camera-flash');
            
            if (!video.videoWidth) return;
            
            // Flash effect
            flash.style.transition = 'none';
            flash.style.opacity = '1';
            setTimeout(() => {
                flash.style.transition = 'opacity 0.4s ease-out';
                flash.style.opacity = '0';
            }, 50);

            // Capture
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
            
            // Preview
            const imgUrl = canvas.toDataURL('image/jpeg');
            const preview = document.getElementById('camera-preview');
            const container = document.getElementById('camera-preview-container');
            
            preview.src = imgUrl;
            container.classList.remove('hidden');
        }
        window.takePicture = takePicture;

        function downloadPicture() {
            const preview = document.getElementById('camera-preview');
            if (!preview.src) return;
            const a = document.createElement('a');
            a.href = preview.src;
            a.download = 'jbsi_portfolio_photo_' + Date.now() + '.jpg';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        }
        window.downloadPicture = downloadPicture;
'''

if 'function openCameraApp()' not in html:
    html = html.replace('// --- INPUT HANDLING ---', camera_script + '\n        // --- INPUT HANDLING ---')

with open('portfolio.html', 'w') as f:
    f.write(html)
