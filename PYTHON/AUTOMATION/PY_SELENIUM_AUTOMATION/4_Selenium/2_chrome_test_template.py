import time
from selenium import webdriver
driver = webdriver.Chrome()                         # Opens Chrome
driver.get("https://www.saucedemo.com/")            # Opens Link
driver.maximize_window()                            # Maximizes window size
print(driver.title)                                 # Prints the title of the webpage
print(driver.current_url)                           # Prints webpage url






time.sleep(30)