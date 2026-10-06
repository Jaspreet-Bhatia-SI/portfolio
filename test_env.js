const { JSDOM } = require('jsdom');
const fs = require('fs');
const dom = new JSDOM(`<!DOCTYPE html><html><body>
    <div id="canvas-container"></div>
    <div id="labels-container"></div>
    <canvas id="minimap-canvas" width="200" height="200"></canvas>
    <button id="btn-enter"></button><div id="enter-text"></div>
    <div id="mag-ui">
        <div id="mag-icon"></div><div id="mag-title"></div><div id="mag-type"></div><div id="mag-desc"></div><div id="mag-tech"></div><a id="mag-link"></a><button id="mag-close"></button>
    </div>
    <div id="joystick-area"><div id="joystick-knob"></div></div>
    <div id="look-area"></div>
    <div id="btn-day"></div><div id="btn-eve"></div><div id="btn-night"></div>
    <div id="mode-text"></div><div id="coords"></div>
</body></html>`, { url: "http://localhost/", runScripts: "outside-only" });

dom.window.THREE = require('three');
// Mock requestAnimationFrame
dom.window.requestAnimationFrame = () => {};

try {
    const code = fs.readFileSync('app.js', 'utf-8');
    dom.window.eval(code);
    console.log("Evaluation completed without throwing.");
} catch(e) {
    console.error("RUNTIME CRASH:", e);
}
