const fs = require('fs');
let html = fs.readFileSync('portfolio.html', 'utf-8');

// Replace the first <script> occurrence with <script>try {
html = html.replace('<script>', '<script>\nwindow.onerror = function(msg, url, line, col, error) { alert("GLOBAL ERROR: " + msg + " at line " + line); };\ntry {');

// Replace the last </script> with } catch(e) { alert("INIT ERROR: " + e.message); }</script>
html = html.replace('</script>\n</body>', '} catch(e) { alert("INIT ERROR: " + e.stack); }\n</script>\n</body>');

fs.writeFileSync('portfolio.html', html);
