from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from selenium.webdriver.common.keys import Keys

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

def seleccionar_hobby(driver: WebDriver, hobby: str) -> None:
    label = driver.find_element(By.XPATH, f"//label[contains(text(), '{hobby}')]")
    label.click()

def seleccionar_fecha_nacimiento(driver: WebDriver, dia: str, mes: str, anio: str) -> None:
    driver.find_element(By.ID, "dateOfBirthInput").click()
    sleep(0.2)
    year_select = driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
    year_select.click()
    year_select.find_element(By.XPATH, f'//option[@value="{anio}"]').click()
    sleep(0.2)
    month_select = driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
    month_select.click()
    meses = {
        "Enero": "0", "Febrero": "1", "Marzo": "2", "Abril": "3",
        "Mayo": "4", "Junio": "5", "Julio": "6", "Agosto": "7",
        "Septiembre": "8", "Octubre": "9", "Noviembre": "10", "Diciembre": "11"
    }
    if mes in meses:
        driver.find_element(By.XPATH, f'//option[@value="{meses[mes]}"]').click()
        sleep(0.2)
    else:
        print(f"Mes '{mes}' no válido.")
        return
    day_xpath = f'//div[contains(@class,"react-datepicker__day") and text()="{dia}" and not(contains(@class,"outside-month"))]'
    try:
        day_element = driver.find_element(By.XPATH, day_xpath)
        day_element.click()
        sleep(0.2)
    except Exception as e:
        print(f"No se pudo encontrar el día '{dia}' en el mes seleccionado. Error: {e}")

def seleccionar_estado_ciudad(driver: WebDriver, estado: str, ciudad: str) -> None:
    state_dropdown = driver.find_element(By.ID, "state")
    state_dropdown.click()
    sleep(0.2)
    state_input = driver.find_element(By.XPATH, "//input[@id='react-select-3-input']")
    state_input.send_keys(estado)
    sleep(0.2)
    state_input.send_keys(Keys.ENTER)
    sleep(0.2)
    city_dropdown = driver.find_element(By.ID, "city")
    city_dropdown.click()
    sleep(0.2)
    city_input = driver.find_element(By.XPATH, "//input[@id='react-select-4-input']")
    city_input.send_keys(ciudad)
    sleep(0.2)
    city_input.send_keys(Keys.ENTER)
    sleep(0.2)

def llenar_formulario(driver: WebDriver) -> None:
    campos_texto: dict[str, str] = {
        "firstName": "joseluis",
        "lastName": "duarte",
        "userEmail": "jose@gmail.com",
        "userNumber": "1000023",
        "currentAddress": "Calle Falsa 123, Bogotá, Colombia",
    }
    for key, value in campos_texto.items():
        llenar_texto_by_id(driver=driver, id_element=key, texto=value)
        sleep(0.2)
    driver.find_element(By.CSS_SELECTOR, 'label[for="gender-radio-1"]').click()
    sleep(0.2)
    seleccionar_fecha_nacimiento(driver, "19", "Mayo", "2025")
    sleep(0.2)
    subject_input = driver.find_element(By.ID, "subjectsInput")
    subject_input.send_keys("Maths")
    sleep(0.2)
    subject_input.send_keys(Keys.ENTER)
    sleep(0.2)
    seleccionar_hobby(driver, "Music")
    sleep(0.2)
    seleccionar_estado_ciudad(driver, "NCR", "Delhi")
    sleep(0.2)

def main() -> None:
    driver: WebDriver = get_driver(options=OPTIONS)
    llenar_formulario(driver=driver)
    sleep(5)
    driver.find_element(By.ID, "submit").click()
    sleep(5)
    driver.quit()

if __name__ == "__main__":
    main()