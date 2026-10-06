import re

with open('portfolio.html', 'r') as f:
    html = f.read()

# Fix the button logic
old_btn_logic = r"if\(state\.mode === 'DRIVING'\) \{\s*// Exit car\s*state\.mode = 'WALKING'; modeText\.innerText = 'SURVIVOR \[ON FOOT\]';\s*playerGroup\.position\.set\(carGroup\.position\.x - 3, 0, carGroup\.position\.z\);\s*playerGroup\.visible = true;\s*\}"
new_btn_logic = """state.wasDrivingBeforeShare = (state.mode === 'DRIVING');
            if(state.wasDrivingBeforeShare) {
                // Exit car for animation
                state.mode = 'WALKING'; modeText.innerText = 'SURVIVOR [SHARING]';
                playerGroup.position.set(carGroup.position.x - 3, 0, carGroup.position.z);
                playerGroup.visible = true;
            } else {
                modeText.innerText = 'SURVIVOR [SHARING]';
            }"""
html = re.sub(old_btn_logic, new_btn_logic, html)

# Fix the end sharing logic
old_end_sharing = r"npc\.state = 'idle';\s*state\.mode = 'WALKING';"
new_end_sharing = """npc.state = 'idle';
                        if (state.wasDrivingBeforeShare) {
                            state.mode = 'DRIVING'; modeText.innerText = 'SURVIVOR [DRIVING]';
                            playerGroup.visible = false;
                        } else {
                            state.mode = 'WALKING'; modeText.innerText = 'SURVIVOR [INDOORS]';
                        }"""
html = re.sub(old_end_sharing, new_end_sharing, html)

with open('portfolio.html', 'w') as f:
    f.write(html)
print("Fixed sharing return to car")
