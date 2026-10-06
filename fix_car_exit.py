import re
with open('portfolio.html', 'r') as f: html = f.read()

old_logic = "playerGroup.position.set(carGroup.position.x - 3, 0, carGroup.position.z);"
new_logic = """const npcSideX = state.activeNPC.grp.position.x > carGroup.position.x ? 3 : -3;
                const npcSideZ = state.activeNPC.grp.position.z > carGroup.position.z ? 3 : -3;
                playerGroup.position.set(carGroup.position.x + npcSideX, 0, carGroup.position.z + npcSideZ);"""

html = html.replace(old_logic, new_logic)
with open('portfolio.html', 'w') as f: f.write(html)
