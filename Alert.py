from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Information alert
driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']").click()
Alert(driver).accept()  # this is accepting the alter at driver
print(driver.find_element(By.XPATH, "//p[@id='result']").text)
# Confirmation alert
driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']").click()
# Alert(driver).dismiss() # this is dismissed the alter at driver
print(Alert(driver).text)  # this is to print the alter message
alert = Alert(driver)
alert.accept()
print(driver.find_element(By.XPATH, "//p[@id='result']").text)
# Alert Prompt
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
alert.send_keys("Hi, I am Credence.")
alert.accept()
print(driver.find_element(By.XPATH, "//p[@id='result']").text)