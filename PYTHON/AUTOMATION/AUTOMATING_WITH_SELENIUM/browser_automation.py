from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

login_page_url = 'https://www.saucedemo.com/'

username = 'standard_user'
password = 'secret_sauce'

chrome_driver_path = 'C:\\Users\\kyas\\Downloads\\chromedriver-win64\\chromedriver.exe'


screenshot_folder = 'C:\\Users\\kyas\\OneDrive - Hewlett Packard Enterprise\\Desktop\\Screenshots'
screenshot_file = 'screenshot.png'

service = Service(chrome_driver_path)


driver = webdriver.Chrome(service=service)


driver.get(login_page_url)


username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'user-name')))
username_field.send_keys(username)


password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'password')))
password_field.send_keys(password)


sign_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'login-button')))
sign_in_button.click()


driver.implicitly_wait(5)


driver.save_screenshot(f"{screenshot_folder}\\{screenshot_file}")

input("Screenshot captured! Press Enter to close the browser")


driver.quit()
