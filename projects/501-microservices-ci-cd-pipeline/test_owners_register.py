from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random

# Set chrome options for working with headless mode (no screen)
chrome_options = webdriver.ChromeOptions()
# Update webdriver instance of chrome-driver with adding chrome options
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(30)

# Connect to the application
url = "http://3.236.53.199:8080"
driver.get(url)
sleep(3)
owners_link = driver.find_element_by_link_text("OWNERS")
owners_link.click()
sleep(2)
all_link = driver.find_element_by_link_text("REGISTER")
all_link.click()
sleep(2)

# Register new Owner to Petclinic App
fn_field = driver.find_element_by_name('firstName')
fn = 'Chris' + str(random.randint(0, 10))
fn_field.send_keys(fn)
sleep(1)
fn_field = driver.find_element_by_name('lastName')
fn_field.send_keys('Clarusway')
sleep(1)
fn_field = driver.find_element_by_name('address')
fn_field.send_keys('Ridge Corp. Street')
sleep(1)
fn_field = driver.find_element_by_name('city')
fn_field.send_keys('McLean')
sleep(1)
fn_field = driver.find_element_by_name('telephone')
fn_field.send_keys('+1230576803')
sleep(1)
fn_field.send_keys(Keys.ENTER)
sleep(10)

driver.quit()