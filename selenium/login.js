const { Builder, By, Key } = require('selenium-webdriver');

(async function example() {
  let driver = await new Builder().forBrowser('chrome').build();

  try {
    await driver.get('https://demo.guru99.com/test/login.html');

    // Realizar una búsqueda
    let email = await driver.findElement(By.id('email'));
    await email.sendKeys('wew', Key.TAB);

    let password = await driver.findElement(By.id('passwd'));
    await password.sendKeys('1234', Key.RETURN);

    // Pausar la ejecución por 5 segundos
    console.log('Esperando 5 segundos...');
    await driver.sleep(5000);

    console.log('Reanudando después de 5 segundos');
  } catch (error) {
    console.error(error);
  } finally {
    await driver.quit();
  }
})();