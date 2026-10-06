const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ headless: true, args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  page.on('console', msg => console.log('BROWSER LOG:', msg.text()));
  page.on('pageerror', error => console.log('BROWSER ERROR:', error.message));
  page.on('requestfailed', request => console.log('BROWSER REQ FAIL:', request.failure().errorText, request.url()));

  try {
    await page.goto('https://portfolio.foodzie.store', { waitUntil: 'networkidle2', timeout: 10000 });
    console.log("Successfully loaded.");
    
    // Check if there is an alert
    page.on('dialog', async dialog => {
      console.log("DIALOG:", dialog.message());
      await dialog.dismiss();
    });

    // Wait a bit
    await new Promise(r => setTimeout(r, 2000));
  } catch(e) {
    console.log("GOTO ERROR:", e.message);
  }
  
  await browser.close();
})();
