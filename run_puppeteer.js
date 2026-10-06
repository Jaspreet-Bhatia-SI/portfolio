const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: true, args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-web-security'] });
  const page = await browser.newPage();
  
  page.on('console', msg => console.log('BROWSER LOG:', msg.text()));
  page.on('pageerror', error => console.log('BROWSER ERROR:', error.message));
  page.on('requestfailed', request => console.log('BROWSER REQ FAIL:', request.failure().errorText, request.url()));

  await page.goto('file://' + __dirname + '/portfolio.html', { waitUntil: 'networkidle0', timeout: 10000 }).catch(e => console.log(e));
  
  await browser.close();
})();
