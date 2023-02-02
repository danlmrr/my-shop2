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
shop = driver.find_element(By.LINK_TEXT, "Shop").click()
book_html5_forms = driver.find_element(By.CSS_SELECTOR, "[src='https://practice.automationtesting.in/wp-content/uploads/2017/01/Mastering-HTML5-Forms-300x300.jpg']").click()

html5_forms = driver.find_element(By.CLASS_NAME, "entry-title")
html5_forms_text = html5_forms.text
assert html5_forms_text == "HTML5 Forms"
if html5_forms_text == "HTML5 Forms":
    print("Название соответсвует")

################Задание 2

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
shop = driver.find_element(By.LINK_TEXT, "Shop").click()
html = driver.find_element(By.CSS_SELECTOR, "[href='https://practice.automationtesting.in/product-category/html/']").click()

items = driver.find_elements(By.CSS_SELECTOR, "[class='count']")
if items == "(3)":
    print("3 товара")






################## Задание 3

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
shop = driver.find_element(By.LINK_TEXT, "Shop").click()

default = driver.find_element(By.CSS_SELECTOR, "[value='menu_order']")
default_text = default.text
assert default_text == "Default sorting"
if default_text == "Default sorting":
    print("Дефолт")
else:
    print("Неверно")


driver.find_element(By.NAME, "orderby").click()
driver.find_element(By.CSS_SELECTOR, "[value='price-desc']").click()

driver.find_element(By.NAME, "orderby").click()
driver.find_element(By.CSS_SELECTOR, "[value='menu_order']").click()

driver.find_element(By.NAME, "orderby").click()
driver.find_element(By.CSS_SELECTOR, "[value='price-desc']").click()

time.sleep(4)
############ Задание 4

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
shop = driver.find_element(By.LINK_TEXT, "Shop").click()

android = driver.find_element(By.CSS_SELECTOR,"[href='https://practice.automationtesting.in/product/android-quick-start-guide/']" ).click()

bop = driver.find_element(By.CSS_SELECTOR, " .price > del > span ")
bop_text = bop.text
bnp = driver.find_element(By.CSS_SELECTOR, " .price > ins > span ")
bnp_text = bnp.text

assert bop_text == "₹600.00"
assert bnp_text == "₹450.00"

book_cover = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
book_cover.click()

book_cover_close = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
book_cover_close.click()
driver.quit()
############## Задание 5

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
shop = driver.find_element(By.LINK_TEXT, "Shop").click()
