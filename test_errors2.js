const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({ args: ['--no-sandbox'] });
    const page = await browser.newPage();
    
    page.on('console', msg => console.log('PAGE LOG:', msg.text()));
    page.on('pageerror', err => {
        console.log('PAGE ERROR:', err.name, err.message, err.stack);
    });
    
    await page.goto('file:///home/jass/education/projects/portfolio/portfolio.html', { waitUntil: 'load' });
    
    // Wait for 2 seconds to see if there are any runtime errors
    await new Promise(r => setTimeout(r, 2000));
    
    await browser.close();
})();
