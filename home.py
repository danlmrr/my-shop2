import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(10)

driver.get('https://practice.automationtesting.in/')

driver.execute_script("window.scrollBy(0, 600);")
ruby = driver.find_element(By.CSS_SELECTOR, "[title='Selenium Ruby']").click()
reviews = driver.find_element(By.CLASS_NAME, "reviews_tab").click()
star = driver.find_element(By.CLASS_NAME, "star-5").click()
comments = driver.find_element(By.ID, "comment")
comments.send_keys("Nice book!")
name = driver.find_element(By.ID, "author")
name.send_keys("Alex")
email = driver.find_element(By.ID, "email")
email.send_keys("alex123@gmail.com")
sumbit = driver.find_element(By.CSS_SELECTOR, "[value='Submit']").click

########### Задание2


