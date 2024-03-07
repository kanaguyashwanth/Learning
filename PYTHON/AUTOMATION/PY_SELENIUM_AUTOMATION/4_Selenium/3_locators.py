import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                         # Opens Chrome
driver.get("https://www.saucedemo.com/")            # Opens Link
driver.maximize_window()                            # Maximizes window size
print(driver.title)                                 # Prints the title of the webpage
print(driver.current_url)                           # Prints webpage url


'''
Locators provided by Selenium: [Search for them on webpage by inspect element]
-ID
-Xpath
-CSSSelector
-Classname
-name
-linkText
'''


'''
# METHOD 1: (Using ID)
Now after visiting the webpage, we want to type the credential on the textfield (saucedemo.com)
'''
driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.ID, 'login-button').click()


'''
# METHOD 2: (Using XPATH)
SYNTAX:
//tagname[@attribute='value']
'''
# driver.find_element(By.XPATH, "//input[@type='text']").send_keys('standard_user')
# driver.find_element(By.XPATH, "//input[@type='password']").send_keys('secret_sauce')
# driver.find_element(By.XPATH, "//input[@type='submit']").click()
# message = driver.find_element(By.CLASS_NAME,"app_logo").text          # Grabs the text
# print(message)                                                        # Prints the text
# assert "Swag Labs" in message                                         # Checks if text is present or not, can be ues for verification.


'''
# METHOD 3: (Using CSSSelector)
SYNTAX:
tagname[attribute='value']

Other Valid CSSSelectors:
#id
.classname

'''
# driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys('standard_user')
# driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys('secret_sauce')
# driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()



'''
# METHOD 4: (LinkText)
- Wherever there is a   
'''


time.sleep(300)