from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(2)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("Admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

