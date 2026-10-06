const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-web-security']});
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 720 });
  await page.goto('file://' + __dirname + '/portfolio.html');
  await new Promise(r => setTimeout(r, 2000));
  await page.screenshot({ path: 'portfolio_screenshot.png' });
  await browser.close();
})();
