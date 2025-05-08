from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
nombre = driver.find_element(By.ID,"firstName")
apellido = driver.find_element(By.ID,"lastName")
Email =driver.find_element(By.ID,"userEmail")
Mobile =driver.find_element(By.ID,"userNumber")
Subjects =driver.find_element(By.ID,"subjectsInput")
CurrentAddress= driver.find_element(By.ID,"currentAddress")
submit=driver.find_element(By.ID,"submit")


nombre.send_keys("jose")
apellido.send_keys("luis")
Email.send_keys("joseluis@gmail.com")
Mobile.send_keys("31275054")
Subjects.send_keys("English")
CurrentAddress.send_keys("cristian es gay")
submit.submit()
time.sleep(2)
driver.quit()
