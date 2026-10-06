const fs = require('fs');
let html = fs.readFileSync('portfolio.html', 'utf-8');

html = html.replace('} catch(e) { console.error(e); alert("FATAL ERROR: " + e.message); throw e; }',
`} catch(e) { 
    console.error(e); 
    const errDiv = document.createElement('div');
    errDiv.style = "position:fixed;top:0;left:0;width:100%;background:red;color:white;z-index:999999;padding:20px;font-size:16px;word-break:break-all;";
    errDiv.innerText = "FATAL ERROR: " + e.message;
    document.body.appendChild(errDiv);
    throw e; 
}`);

fs.writeFileSync('portfolio.html', html);
