from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_inicio_sesion():

    options = webdriver.ChromeOptions()

    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:

        driver.get(
            "https://the-internet.herokuapp.com/login"
        )

        usuario = driver.find_element(
            By.ID,
            "username"
        )

        password = driver.find_element(
            By.ID,
            "password"
        )

        usuario.send_keys(
            "tomsmith"
        )

        password.send_keys(
            "SuperSecretPassword!"
        )

        boton = driver.find_element(
            By.CSS_SELECTOR,
            "button[type='submit']"
        )

        boton.click()

        mensaje = WebDriverWait(
            driver,
            10
        ).until(
            EC.presence_of_element_located(
                (By.ID, "flash")
            )
        )

        assert (
            "You logged into a secure area!"
            in mensaje.text
        )

    finally:

        driver.quit()