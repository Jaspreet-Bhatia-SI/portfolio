with open('portfolio.html', 'r') as f:
    html = f.read()

# 1. Add T in controls
controls_target = '<div class="flex items-center justify-end gap-2 mb-2"><span class="text-xs font-bold text-slate-400">Read</span>'
controls_share = '<div class="flex items-center justify-end gap-2 mb-2"><span class="text-xs font-bold text-slate-400">Share</span><div class="w-7 h-7 rounded bg-[#2c352a] border border-white/10 flex items-center justify-center text-[10px] font-bold text-white key-cap" id="key-t">T</div></div>\n                '
if controls_target in html and "Share</span>" not in html:
    html = html.replace(controls_target, controls_share + controls_target)

# 2. Add SHARING animation logic inside animate()
target_transition = "else if (state.mode === 'TRANSITION') {"
if target_transition in html and "state.shareTimer +=" not in html:
    sharing_logic = """else if (state.mode === 'SHARING') {
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
                        if (state.wasDrivingBeforeShare) {
                            state.mode = 'DRIVING'; modeText.innerText = 'SURVIVOR [DRIVING]';
                            playerGroup.visible = false;
                        } else {
                            state.mode = 'WALKING'; modeText.innerText = 'SURVIVOR [ON FOOT]';
                        }
                    }
                }
                
                // Camera logic: allow user to rotate view during sharing!
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
    html = html.replace(target_transition, sharing_logic + target_transition)

# 3. Add cam snapping to button listener
btn_event = "state.activeNPC.state = 'sharing';"
snap_logic = btn_event + """
            // Snap camera to side view
            const angleBetween = Math.atan2(state.activeNPC.grp.position.x - playerGroup.position.x, state.activeNPC.grp.position.z - playerGroup.position.z);
            camTheta = angleBetween + Math.PI/2;
            camPhi = Math.PI / 3;
"""
if btn_event in html and "angleBetween" not in html:
    html = html.replace(btn_event, snap_logic)

with open('portfolio.html', 'w') as f:
    f.write(html)
print("Updated sharing animations and controls")
