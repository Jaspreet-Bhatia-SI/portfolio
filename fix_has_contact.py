with open('portfolio.html', 'r') as f:
    html = f.read()

old_code = """                    if(t > 3.5) {
                        playerGroup.userData.rArm.children.forEach(c => { if(c.geometry === phoneGeo) c.visible = false; });
                        npc.rArm.children.forEach(c => { if(c.geometry === phoneGeo) c.visible = false; });
                        npc.state = 'idle';
                        state.mode = state.wasInCar ? 'DRIVING' : 'WALKING';
                        showHUD();
                    }"""

new_code = """                    if(t > 3.5) {
                        playerGroup.userData.rArm.children.forEach(c => { if(c.geometry === phoneGeo) c.visible = false; });
                        npc.rArm.children.forEach(c => { if(c.geometry === phoneGeo) c.visible = false; });
                        npc.state = 'idle';
                        state.mode = state.wasInCar ? 'DRIVING' : 'WALKING';
                        hasContact = false; // Reset so they can trigger it again
                        showHUD();
                    }"""

html = html.replace(old_code, new_code)
with open('portfolio.html', 'w') as f:
    f.write(html)
