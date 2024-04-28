import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
print(driver.title)

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg' , 'Strawberry - 1/4 Kg']
actualList = []
driver.find_element(By.CLASS_NAME,'search-keyword').send_keys('ber')
time.sleep(2)

productList=driver.find_elements(By.XPATH, '//h4')
print(len(productList))

for product in productList:
    actualList.append(product.text)
    print(product.text)

assert expectedList != actualList,"Not Equal"

time.sleep(2)