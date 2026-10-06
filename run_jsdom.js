const fs = require('fs');
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const html = fs.readFileSync('portfolio.html', 'utf-8');
const virtualConsole = new jsdom.VirtualConsole();
virtualConsole.on("error", (e) => {
    console.error("RUNTIME ERROR:", e);
});
virtualConsole.on("warn", (w) => {
    console.warn("RUNTIME WARN:", w);
});
virtualConsole.on("log", (l) => {
    console.log("RUNTIME LOG:", l);
});

const dom = new JSDOM(html, { runScripts: "dangerously", virtualConsole });
