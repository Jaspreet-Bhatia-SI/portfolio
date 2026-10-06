import re

with open('portfolio.html', 'r') as f:
    html = f.read()

# Fix window.open clicks
html = html.replace("onclick=\"window.open('https://", "onclick=\"event.stopPropagation(); window.open('https://")
html = html.replace("onclick=\"window.location.href='mailto:", "onclick=\"event.stopPropagation(); window.location.href='mailto:")

# Fix camera permissions issue
old_cam = """            btnOpenCamera.addEventListener('click', async () => {
                cameraApp.classList.remove('translate-y-full');
                try {
                    window.cameraStream = await navigator.mediaDevices.getUserMedia({ """

new_cam = """            btnOpenCamera.addEventListener('click', async (e) => {
                e.stopPropagation();
                if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
                    alert("Camera requires HTTPS or a secure context (like localhost).");
                    return;
                }
                cameraApp.classList.remove('translate-y-full');
                try {
                    window.cameraStream = await navigator.mediaDevices.getUserMedia({ """

html = html.replace(old_cam, new_cam)

with open('portfolio.html', 'w') as f:
    f.write(html)
print("done")
