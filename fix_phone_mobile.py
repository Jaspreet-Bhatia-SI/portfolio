import re

with open('portfolio.html', 'r') as f:
    html = f.read()

# 1. Fix Phone Frame dimensions to fit mobile screens
html = html.replace(
    'class="relative w-full max-w-[340px] h-[680px] bg-black rounded-[50px] border-[12px] border-black shadow-[0_20px_50px_rgba(0,0,0,0.5)] flex flex-col transform scale-[0.2] translate-y-32 opacity-0 transition-all duration-500 pointer-events-auto overflow-hidden" id="phone-frame"',
    'class="relative w-[90vw] max-w-[340px] h-[85vh] max-h-[680px] bg-black rounded-[36px] sm:rounded-[50px] border-[8px] sm:border-[12px] border-black shadow-[0_20px_50px_rgba(0,0,0,0.5)] flex flex-col transform scale-[0.2] translate-y-32 opacity-0 transition-all duration-500 pointer-events-auto overflow-hidden" id="phone-frame"'
)

# 2. Adjust margins for the Search Widget so it fits tighter vertically
html = html.replace(
    '<div class="mt-6 mx-4 relative z-30">',
    '<div class="mt-2 sm:mt-6 mx-4 relative z-30">'
)

# 3. Adjust Apps grid margins and gaps to fit shorter screens
html = html.replace(
    '<div class="mt-10 px-6 grid grid-cols-4 gap-y-8 gap-x-4 z-20">',
    '<div class="mt-4 sm:mt-8 px-4 sm:px-6 grid grid-cols-4 gap-y-4 sm:gap-y-8 gap-x-3 sm:gap-x-4 z-20">'
)

# 4. Add muted to the video tag (iOS requirement)
html = html.replace(
    '<video id="camera-feed" class="w-full h-full object-cover" autoplay playsinline></video>',
    '<video id="camera-feed" class="w-full h-full object-cover" autoplay playsinline muted></video>'
)

# 5. Update Camera JS Logic for better permissions and error handling
old_js = """        if(btnOpenCamera) {
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
        }"""
new_js = """        if(btnOpenCamera) {
            btnOpenCamera.addEventListener('click', async () => {
                cameraApp.classList.remove('translate-y-full');
                try {
                    window.cameraStream = await navigator.mediaDevices.getUserMedia({ 
                        video: { facingMode: { ideal: 'environment' } },
                        audio: false
                    });
                    cameraFeed.srcObject = window.cameraStream;
                    await cameraFeed.play();
                } catch (err) {
                    console.error("Camera access denied or unavailable", err);
                    alert("Camera permissions are required to take pictures. Please allow camera access in your browser settings and try again.");
                    cameraApp.classList.add('translate-y-full');
                }
            });
        }"""
html = html.replace(old_js, new_js)

with open('portfolio.html', 'w') as f:
    f.write(html)
print("Mobile layout and camera fixed")
