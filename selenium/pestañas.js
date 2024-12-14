const { Builder, By, Key } = require('selenium-webdriver');

(async function manageTabs() {
    // Configurar el navegador (en este caso Chrome)
    let driver = await new Builder().forBrowser('chrome').build();

    try {
        // Abrir la primera pestaña y cargar una URL
        await driver.get('https://npm.com');
        console.log("Primera pestaña abierta con Example.com");

        // Abrir una segunda pestaña
        await driver.switchTo().newWindow('tab');
        await driver.get('https://google.com');
        console.log("Segunda pestaña abierta con Google.com");

        // Abrir una tercera pestaña
        await driver.switchTo().newWindow('tab');
        await driver.get('https://github.com');
        console.log("Tercera pestaña abierta con GitHub.com");

        // Obtener todos los identificadores de las pestañas
        let tabs = await driver.getAllWindowHandles();

        // Navegar entre las pestañas
        console.log("Navegando a la primera pestaña...");
        await driver.switchTo().window(tabs[0]); // Primera pestaña
        console.log("Estamos en la primera pestaña");

        console.log("Navegando a la segunda pestaña...");
        await driver.switchTo().window(tabs[1]); // Segunda pestaña
        console.log("Estamos en la segunda pestaña");

        console.log("Navegando a la tercera pestaña...");
        await driver.switchTo().window(tabs[2]); // Tercera pestaña
        console.log("Estamos en la tercera pestaña");

    } finally {
        // Cerrar el navegador después de 5 segundos
        setTimeout(async () => {
            await driver.quit();
        }, 5000);
    }
})();
