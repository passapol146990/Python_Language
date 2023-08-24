from selenium import webdriver
from selenium.webdriver.common.by import By

url = str("http://10.99.92.1/webAuth/")
drive = webdriver.Chrome()
drive.get(url)

drive.find_element(By.XPATH,'//*[@id="une"]').send_keys('66011214240')
drive.find_element(By.XPATH,'//*[@id="passwd"]').send_keys('Pw@1469900681121')
drive.find_element(By.XPATH,'//*[@id="loginbt"]').click()

