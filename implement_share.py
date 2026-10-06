import re

with open('portfolio.html', 'r') as f:
    html = f.read()

# 1. Add btn-share
btn_read_mag_pattern = r'(<button id="btn-read-mag".*?</button>)'
btn_share_html = """
            <button id="btn-share" class="pointer-events-auto hidden opacity-0 transition-all duration-300 transform scale-90 bg-indigo-600 text-white px-8 py-4 rounded-full text-sm font-bold tracking-widest uppercase flex items-center justify-center gap-3 shadow-[0_10px_40px_rgba(79,70,229,0.4)] hover:bg-indigo-500 active:scale-95 cursor-pointer border border-indigo-400/50">
                <iconify-icon icon="solar:smartphone-update-linear" width="22" class="animate-pulse"></iconify-icon>
                <span><span class="hidden md:inline">Press [T] to </span>Share Contact</span>
            </button>
"""
html = re.sub(btn_read_mag_pattern, r'\1' + btn_share_html, html, flags=re.DOTALL)


# 2. Add button js element setup
js_setup_pattern = r"const btnReadMag = document\.getElementById\('btn-read-mag'\);"
html = html.replace(js_setup_pattern, js_setup_pattern + "\n        const btnShare = document.getElementById('btn-share');")


# 3. Inject phone geometry and variables right before createNPC
create_npc_pattern = r'function createNPC\(x, z, color, patrolRadius\) \{'
phone_vars = """
        const phoneGeo = new THREE.BoxGeometry(0.12, 0.25, 0.02);
        const phoneMat = new THREE.MeshStandardMaterial({color: 0x111111, emissive: 0x444444});
"""
html = html.replace(create_npc_pattern, phone_vars + '\n' + create_npc_pattern)


# 4. Attach phone to NPCs inside createNPC
npc_r_arm_pattern = r'const rArmMesh = new THREE\.Mesh\(new THREE\.BoxGeometry\(0\.2, 0\.8, 0\.2\), skinMat\); rArmMesh\.position\.y = -0\.3; rArmMesh\.castShadow = true; rArm\.add\(rArmMesh\);'
npc_phone_logic = npc_r_arm_pattern + """
            const phone = new THREE.Mesh(phoneGeo, phoneMat); phone.position.set(0, -0.7, 0.1); phone.visible = false; rArm.add(phone);
"""
html = html.replace(npc_r_arm_pattern, npc_phone_logic)


# 5. Attach phone to Player
player_r_arm_pattern = r'const rArm = createLimb\(skinMat, 0, 1\.1\); rArm\.position\.set\(0\.55, 2\.5, 0\); playerGroup\.add\(rArm\);'
player_phone_logic = player_r_arm_pattern + """
        const pPhone = new THREE.Mesh(phoneGeo, phoneMat); pPhone.position.set(0, -1.0, 0.15); pPhone.visible = false; rArm.add(pPhone);
"""
html = html.replace(player_r_arm_pattern, player_phone_logic)

# 6. Button logic (Event Listener)
# We will inject this before the main animate loop
animate_pattern = r'function animate\(\) \{'
share_event_logic = """
        // SHARING LOGIC
        btnShare.addEventListener('click', () => {
            if(!state.activeNPC || state.mode === 'SHARING') return;
            if(state.mode === 'DRIVING') {
                // Exit car
                state.mode = 'WALKING'; modeText.innerText = 'SURVIVOR [ON FOOT]';
                playerGroup.position.set(carGroup.position.x - 3, 0, carGroup.position.z);
                playerGroup.visible = true;
            }
            state.mode = 'SHARING';
            state.shareTimer = 0;
            state.activeNPC.state = 'sharing';
            
            // Show phones
            playerGroup.userData.rArm.children.forEach(c => { if(c.geometry === phoneGeo) c.visible = true; });
            state.activeNPC.rArm.children.forEach(c => { if(c.geometry === phoneGeo) c.visible = true; });

            // Create Contact Card
            const cardCanvas = document.createElement('canvas'); cardCanvas.width = 512; cardCanvas.height = 256;
            const ctx = cardCanvas.getContext('2d');
            ctx.fillStyle = '#1e241c'; ctx.fillRect(0,0,512,256);
            ctx.fillStyle = '#4f46e5'; ctx.fillRect(0,0,512,16);
            ctx.strokeStyle = '#4f46e5'; ctx.lineWidth = 8; ctx.strokeRect(4,4,504,248);
            ctx.fillStyle = '#fff'; ctx.font = 'bold 36px "Courier New"'; ctx.fillText('Jaspreet Bhatia (JBSI)', 20, 60);
            ctx.fillStyle = '#94a3b8'; ctx.font = '28px "Courier New"'; ctx.fillText('Software Engineer', 20, 100);
            ctx.fillStyle = '#4ade80'; ctx.font = '22px "Courier New"'; 
            ctx.fillText('bhatiajaspreet161@gmail.com', 20, 150);
            ctx.fillText('linkedin.com/in/jaspreet-bhatia-si', 20, 190);
            ctx.fillText('Instagram: @jass_bhatia.si', 20, 230);
            
            const cardTex = new THREE.CanvasTexture(cardCanvas);
            const cardMat = new THREE.MeshBasicMaterial({map: cardTex, side: THREE.DoubleSide, transparent: true, opacity: 0});
            state.shareCard = new THREE.Mesh(new THREE.PlaneGeometry(3, 1.5), cardMat);
            
            const midX = (playerGroup.position.x + state.activeNPC.grp.position.x) / 2;
            const midZ = (playerGroup.position.z + state.activeNPC.grp.position.z) / 2;
            state.shareCard.position.set(midX, 1.5, midZ);
            scene.add(state.shareCard);
            btnShare.classList.add('hidden', 'opacity-0');
        });

        // Keybind T for share
        window.addEventListener('keydown', (e) => {
            if(e.key.toLowerCase() === 't' && !btnShare.classList.contains('hidden')) {
                btnShare.click();
            }
        });
"""
html = html.replace(animate_pattern, share_event_logic + '\n        ' + animate_pattern)

# 7. Add distance checking to WALKING / DRIVING loops in animate
# We can find `if (state.mode === 'WALKING') {` and just do this globally inside animate
global_npc_dist_pattern = r'if \(state\.mode === \'DRIVING\'\)'
global_npc_dist_logic = """
                // Nearest NPC logic
                if (state.mode === 'WALKING' || state.mode === 'DRIVING') {
                    let nearestNPC = null; let minDist = 4;
                    const pPos = state.mode === 'DRIVING' ? carGroup.position : playerGroup.position;
                    npcs.forEach(npc => {
                        const d = Math.hypot(npc.grp.position.x - pPos.x, npc.grp.position.z - pPos.z);
                        if(d < minDist) { minDist = d; nearestNPC = npc; }
                    });
                    if(nearestNPC) {
                        state.activeNPC = nearestNPC;
                        btnShare.classList.remove('hidden'); btnShare.classList.remove('opacity-0');
                    } else {
                        state.activeNPC = null;
                        btnShare.classList.add('hidden', 'opacity-0');
                    }
                }
"""
html = html.replace(global_npc_dist_pattern, global_npc_dist_logic + '\n                ' + global_npc_dist_pattern)


# 8. SHARING state logic inside animate()
end_driving_pattern = r'\} else if \(state\.mode === \'INSIDE\'\) \{'
sharing_loop_logic = """
            } else if (state.mode === 'SHARING') {
                const npc = state.activeNPC;
                state.shareTimer += 0.02;
                const t = state.shareTimer;
                
                const pt = Math.atan2(playerGroup.position.x - npc.grp.position.x, playerGroup.position.z - npc.grp.position.z);
                const nt = Math.atan2(npc.grp.position.x - playerGroup.position.x, npc.grp.position.z - playerGroup.position.z);
                
                // Keep players standing still
                playerGroup.userData.lLeg.rotation.x = 0; playerGroup.userData.rLeg.rotation.x = 0;
                playerGroup.userData.lArm.rotation.x = 0; 
                npc.lLeg.rotation.x = 0; npc.rLeg.rotation.x = 0;
                npc.lArm.rotation.x = 0;

                // Turn to face each other (shortest angle lerp approx)
                const dpy = nt - playerGroup.rotation.y;
                playerGroup.rotation.y += Math.atan2(Math.sin(dpy), Math.cos(dpy)) * 0.1;
                const dny = pt - npc.grp.rotation.y;
                npc.grp.rotation.y += Math.atan2(Math.sin(dny), Math.cos(dny)) * 0.1;

                if(t < 1.5) {
                    playerGroup.userData.rArm.rotation.x += (-Math.PI/2 - playerGroup.userData.rArm.rotation.x) * 0.1;
                    npc.rArm.rotation.x += (-Math.PI/2 - npc.rArm.rotation.x) * 0.1;
                } else if(t < 5) {
                    state.shareCard.material.opacity = Math.min(1, (t - 1.5) * 2);
                    state.shareCard.position.y += 0.005;
                    state.shareCard.rotation.y += 0.02;
                } else {
                    playerGroup.userData.rArm.rotation.x += (0 - playerGroup.userData.rArm.rotation.x) * 0.1;
                    npc.rArm.rotation.x += (0 - npc.rArm.rotation.x) * 0.1;
                    state.shareCard.material.opacity -= 0.05;
                    if(state.shareCard.material.opacity <= 0) {
                        scene.remove(state.shareCard);
                        state.shareCard.geometry.dispose();
                        state.shareCard.material.dispose();
                        playerGroup.userData.rArm.children.forEach(c => { if(c.geometry === phoneGeo) c.visible = false; });
                        npc.rArm.children.forEach(c => { if(c.geometry === phoneGeo) c.visible = false; });
                        npc.state = 'idle';
                        state.mode = 'WALKING';
                    }
                }
                
                const midX = (playerGroup.position.x + npc.grp.position.x) / 2;
                const midZ = (playerGroup.position.z + npc.grp.position.z) / 2;
                const target = new THREE.Vector3(midX, playerGroup.position.y + 1.5, midZ);
                camera.position.lerp(new THREE.Vector3(midX - 4, target.y + 2, midZ + 6), 0.05);
                camera.lookAt(target);
"""
html = html.replace(end_driving_pattern, sharing_loop_logic + '\n            ' + end_driving_pattern)

with open('portfolio.html', 'w') as f:
    f.write(html)
print("Implemented share")
