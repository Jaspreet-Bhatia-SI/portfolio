import re

with open('portfolio.html', 'r') as f:
    html = f.read()

# 1. Add JS element setup
html = re.sub(r"(const btnReadMag = document\.getElementById\('btn-read-mag'\);)", r"\1\n        const btnShare = document.getElementById('btn-share');", html)

# 2. Add phone geometry before createNPC
phone_vars = """
        const phoneGeo = new THREE.BoxGeometry(0.12, 0.25, 0.02);
        const phoneMat = new THREE.MeshStandardMaterial({color: 0x111111, emissive: 0x444444});
"""
html = re.sub(r'(function createNPC\(x, z, color, patrolRadius\) \{)', phone_vars + r'\n\1', html)

# 3. Attach phone to NPCs
npc_phone_logic = r'\1\n            const phone = new THREE.Mesh(phoneGeo, phoneMat); phone.position.set(0, -0.7, 0.1); phone.visible = false; rArm.add(phone);'
html = re.sub(r'(const rArmMesh = new THREE\.Mesh\(new THREE\.BoxGeometry\(0\.2, 0\.8, 0\.2\), skinMat\); rArmMesh\.position\.y = -0\.3; rArmMesh\.castShadow = true; rArm\.add\(rArmMesh\);)', npc_phone_logic, html)

# 4. Attach phone to Player
player_phone_logic = r'\1\n        const pPhone = new THREE.Mesh(phoneGeo, phoneMat); pPhone.position.set(0, -1.0, 0.15); pPhone.visible = false; rArm.add(pPhone);'
html = re.sub(r'(const rArm = createLimb\(skinMat, 0, 1\.1\); rArm\.position\.set\(0\.55, 2\.5, 0\); playerGroup\.add\(rArm\);)', player_phone_logic, html)

# 5. Button logic & Event Listeners (before animate)
share_event_logic = """
        // SHARING LOGIC
        btnShare.addEventListener('click', () => {
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

        window.addEventListener('keydown', (e) => {
            if(e.key.toLowerCase() === 't' && !btnShare.classList.contains('hidden')) {
                btnShare.click();
            }
        });
"""
html = re.sub(r'(function animate\(\) \{)', share_event_logic + r'\n\1', html)

# 6. Distance checking in animate
global_npc_dist_logic = r"""
                // Nearest NPC logic
                if (state.mode === 'WALKING' || state.mode === 'DRIVING') {
                    let nearestNPC = null; let minDist = 12;
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
\1"""
html = re.sub(r'(if \(state\.mode === \'DRIVING\'\) \{)', global_npc_dist_logic, html)

# 7. SHARING state logic
sharing_loop_logic = r"""\1 else if (state.mode === 'SHARING') {
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

                // Turn to face each other
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
                camera.position.lerp(new THREE.Vector3(midX - 4, target.y + 2, midZ + 6), 0.05);
                camera.lookAt(target);
            }"""
html = re.sub(r'(\} else if \(state\.mode === \'INSIDE\'\) \{)', sharing_loop_logic, html)

with open('portfolio.html', 'w') as f:
    f.write(html)
print("Implemented share reliably")
