from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://portal.hubirancell.com/auth/login")
driver.set_window_size(1920, 1080)
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('989026825111')
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('4120555445')
driver.find_element(By.XPATH, '/html/body/app-root/div/div/app-login/div/div/div[2]/button').click()

time.sleep(1)
driver.save_screenshot("screenshot.png")
driver.close()