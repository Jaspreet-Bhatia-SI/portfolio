with open('portfolio.html', 'r') as f:
    html = f.read()

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

# Simple and foolproof replace
html = html.replace('</script>\n</body>', js_logic)

with open('portfolio.html', 'w') as f:
    f.write(html)
