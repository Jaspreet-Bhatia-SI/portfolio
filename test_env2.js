const { JSDOM } = require('jsdom');
const fs = require('fs');
const html = fs.readFileSync('portfolio.html', 'utf-8');

const virtualConsole = new (require("jsdom")).VirtualConsole();
virtualConsole.on("error", (e) => {
    console.error("JSDOM ERROR:", e);
});
virtualConsole.on("jsdomError", (e) => {
    console.error("JSDOM jsdomError:", e);
});
virtualConsole.on("log", (m) => {
    console.log("JSDOM LOG:", m);
});

const dom = new JSDOM(html, { 
    runScripts: "dangerously", 
    virtualConsole,
    pretendToBeVisual: true
});

setTimeout(() => {
    console.log("Finished 2 seconds evaluation.");
}, 2000);
