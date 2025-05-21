from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
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
    driver.get("https://demoqa.com/automation-practice-form")
    return driver


def llenar_texto_by_id(driver: WebDriver, id_element: str, texto: str) -> None:
    element: WebElement = driver.find_element(By.ID, id_element)
    element.send_keys(texto)


def llenar_formulario(driver: WebDriver) -> None:
    campos_texto: dict[str, str] = {
        "firstName": "joseluis",
        "lastName": "duarte",
        "userEmail": "jose@gmail.com",
        "userNumber": "1000023",
        "subjectsInput": "Maths",
        "currentAddress": "Calle Falsa 123, Bogotá, Colombia",
    }

    for key, value in campos_texto.items():
        llenar_texto_by_id(driver=driver, id_element=key, texto=value)
        sleep(1)


def main() -> None:
    driver: WebDriver = get_driver(options=OPTIONS)
    llenar_formulario(driver=driver)
    sleep(5)
    driver.quit()


if __name__ == "__main__":
    main()
