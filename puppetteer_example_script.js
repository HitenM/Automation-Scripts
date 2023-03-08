const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  // Navigate to the website
  await page.goto('https://www.classcentral.com/', {waitUntil: 'networkidle2'});

  // Wait for the menu button to appear and hover over it
  const coursesButton = await page.waitForSelector('button[data-name="LARGE_UP_MAIN_NAV_TRIGGER"]');
  await coursesButton.hover();

  // Move the mouse out of the menu to trigger it to close
  await page.mouse.move(0, 0);

  // Click on a blank area of the page to simulate a mouse click event
  await page.mouse.click(0, 0);

  // Wait for the page to settle and save the HTML
  await page.waitForTimeout(5000); // adjust wait time as needed
  const html = await page.content();

  // Save the HTML to a file
  const fs = require('fs');
  fs.writeFileSync('classcentral.html', html);

  // Close the browser
  await browser.close();
})();
