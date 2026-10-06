const fs = require('fs');
let html = fs.readFileSync('portfolio.html', 'utf-8');

html = html.replace('window.onerror = function(msg, url, line, col, error) { alert("GLOBAL ERROR: " + msg + " at line " + line); };',
`window.onerror = function(msg, url, line, col, error) { 
    const errDiv = document.createElement('div');
    errDiv.style = "position:fixed;top:0;left:0;width:100%;background:red;color:white;z-index:999999;padding:20px;font-size:16px;word-break:break-all;";
    errDiv.innerText = "GLOBAL ERROR: " + msg + " at line " + line;
    document.body.appendChild(errDiv);
};`);

html = html.replace('} catch(e) { alert("INIT ERROR: " + e.stack); }',
`} catch(e) { 
    const errDiv = document.createElement('div');
    errDiv.style = "position:fixed;top:0;left:0;width:100%;background:red;color:white;z-index:999999;padding:20px;font-size:16px;word-break:break-all;";
    errDiv.innerText = "INIT ERROR: " + e.stack;
    document.body.appendChild(errDiv);
}`);

fs.writeFileSync('portfolio.html', html);
