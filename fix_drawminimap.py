import re

with open('portfolio.html', 'r') as f:
    html = f.read()

old_func_pattern = r"function drawMinimap\(\).*?minimapCtx\.fillRect\(94, -126, 12, 252\); // right"

new_func = """function drawMinimap() {
            if(!minimapCtx) return;
            const mw = minimapCanvas.width;
            const mh = minimapCanvas.height;
            minimapCtx.clearRect(0, 0, mw, mh);
            
            const px = state.mode === 'DRIVING' ? carGroup.position.x : playerGroup.position.x;
            const pz = state.mode === 'DRIVING' ? carGroup.position.z : playerGroup.position.z;
            const pAngle = state.mode === 'DRIVING' ? state.angle : state.playerAngle;

            if(minimapBlip) minimapBlip.style.transform = `rotate(${-pAngle * (180/Math.PI)}deg)`;

            minimapCtx.save();
            minimapCtx.translate(mw / 2, mh / 2);
            const scale = (mw / 160) * (window.innerWidth < 768 ? 0.6 : 0.8);
            minimapCtx.scale(scale, scale);
            minimapCtx.translate(-px, -pz);

            // Ring Road
            minimapCtx.fillStyle = '#594a36'; 
            minimapCtx.fillRect(-112, -132, 224, 24); // top
            minimapCtx.fillRect(-112, 108, 224, 24); // bot
            minimapCtx.fillRect(-112, -132, 24, 264); // left
            minimapCtx.fillRect(88, -132, 24, 264); // right
            // Inner Cross
            minimapCtx.fillRect(-100, -12, 200, 24); // H
            minimapCtx.fillRect(-12, -120, 24, 240); // V"""

html = re.sub(old_func_pattern, new_func, html, flags=re.DOTALL)

with open('portfolio.html', 'w') as f:
    f.write(html)
