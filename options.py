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
    driver.get("https://demoqa.com/login")
    return driver
