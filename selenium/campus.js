const { Builder, By, Key, until } = require('selenium-webdriver');

(async function example() {

    let driver = await new Builder().forBrowser('chrome').build();
  
    try {
      await driver.get('https://campusvirtualunillanos.co/');
      let searchBox = await driver.findElements(By.css('div.h-100 > h3'));
      console.log('Búsqueda realizada con éxito del primer numero',await searchBox[0].getText());
      console.log('Búsqueda realizada con éxito del segundo numero',await searchBox[1].getText());
    } catch (error) {
      console.error(error);
    } finally {
    
      await driver.quit();
    }
  })();