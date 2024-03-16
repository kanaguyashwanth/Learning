import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# STEP 1: RUN HEADLESS MODE
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys('standard_user')
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys('secret_sauce')
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

# STEP 2: FINDING THE HEIGHT OF THE PAGE
# We know width of page is constant
webpage_width = 1920
# Getting the height of the page through JS code
webpage_height = driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
# Setting the window size
driver.set_window_size(webpage_height, webpage_height)

# STEP 3: TAKING SCREENSHOT OF WEBPAGE
page_body = driver.find_element(By.TAG_NAME, 'body')
page_body.screenshot("full_page_screenshot.png")

driver.quit()










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
# driver.find_element(By.ID, 'user-name').send_keys('standard_user')
# driver.find_element(By.ID, 'password').send_keys('secret_sauce')
# driver.find_element(By.ID, 'login-button').click()


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