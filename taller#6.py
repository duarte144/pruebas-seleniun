from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep

OPTIONS: list[str] = [
    "--disable-extensions",
    "--disable-gpu",
    "start-maximized",
]

def get_driver(options: list[str] = []) -> WebDriver:
    opt = webdriver.ChromeOptions()
    for option in options:
        opt.add_argument(option)

    driver = webdriver.Chrome(options=opt)
    driver.get("https://demoqa.com/login")
    return driver

def llenar_formulario(driver: WebDriver) -> None:
    campos_texto: dict[str, str] = {
        "firstname": "JoseLuis",
        "lastname": "Duarte",
        "userName": "joseluis123",
        "password": "Password123!"
    }
    
    


    for field_id, valor in campos_texto.items():
        campo = driver.find_element(By.ID, field_id)
        campo.send_keys(valor)
        sleep(3)

    register_button = driver.find_element(By.ID, "register")
    register_button.click()
    sleep(3)


def main():
    driver = get_driver(OPTIONS)
    sleep(2)

    driver.find_element(By.ID, "newUser").click()
    sleep(2)

    llenar_formulario(driver)
    driver.quit()
if __name__ == "__main__":
    main()






