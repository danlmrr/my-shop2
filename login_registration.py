import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://practice.automationtesting.in/')

my_account = driver.find_element(By.LINK_TEXT, "My Account").click()
email = driver.find_element(By.ID, "reg_email")
email.send_keys("alex123@gmail.com")
password = driver.find_element(By.ID, "reg_password")
password.send_keys("532Alex131")

register = driver.find_element(By.CSS_SELECTOR, "[name='register']")
register.click()
email = driver.find_element(By.ID, "reg_email")
email.click()
register = driver.find_element(By.CSS_SELECTOR, "[name='register']")
register.click()

######## Задание 2

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://practice.automationtesting.in/')

my_account = driver.find_element(By.LINK_TEXT, "My Account").click()
username = driver.find_element(By.ID, "username")
username.send_keys("alex123@gmail.com")
password = driver.find_element(By.ID, "password")
password.send_keys("532Alex131")
login = driver.find_element(By.NAME, "login").click()

logout = driver.find_element(By.LINK_TEXT, "Logout")
logout_text = logout.text

assert logout_text == "Logout"
if logout_text == "Logout":
    print("Присутсвует")
time.sleep(3)

########### Задание 3
