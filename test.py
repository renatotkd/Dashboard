import pytest
import time
from selenium import webdriver


chrome_path = "/home/renato/programas/dash/chrome-linux64/chrome"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path

driver = webdriver.Chrome(options=chrome_options)

url="http:127.0.0.1:8080"

driver.get(url)
time.sleep(10)

assert "Dash" in driver.title
#assert "Pagina inicial " in driver.page_source
print('teste inicial')


driver.get(url+"/formulario")
time.sleep(10)
assert "Dashboard " in driver.page_source