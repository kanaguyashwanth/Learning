import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()                          # Opens Chrome
driver.get("https://onesupport.apps.homedepot.com/") # Opens Link
driver.maximize_window()                             # Maximizes window size
print(driver.title)                                  # Prints the title of the webpage
print(driver.current_url)                            # Prints webpage url
#driver.implicitly_wait(5)                           # Implicit wait / Blindly wait

'''
Locators provided by Selenium: [Search for them on webpage by inspect element]
-ID
-Xpath
-CSSSelector
-Classname
-name
-linkText
'''

# METHOD 1: (Using ID)
'''
Now after visiting the webpage, we want to type the credential on the textfield (https://onesupport.apps.homedepot.com/)
'''

# SIGN IN
driver.find_element(By.ID, 'inputUsername').send_keys('rc982be')
driver.find_element(By.ID, 'inputPassword').send_keys('fry.brute.hax-06')
driver.find_element(By.ID, 'buttonSignOn').click()
time.sleep(2)

values = ['0170', '0483', '1202', '1802', '2781', '3903', '7080', '8519']

wait = WebDriverWait(driver, 120)

for x in values:

    input_element = wait.until(expected_conditions.presence_of_element_located((By.ID, 'mat-input-0')))
    input_element.clear()
    input_element.send_keys(x)

    submit_button = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    submit_button.click()

    server_button = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/app-root[1]/div[1]/app-main-page[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/app-search[1]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[1]/div[1]/div[1]/app-store-side-tabs[1]/div[1]/div[1]/button[3]/img[1]')))
    driver.execute_script("arguments[0].click();", server_button)
    time.sleep(3)
    sanity_check = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@aria-label='Run All Sanity Checks']")))
    sanity_check.click()
    #time.sleep(30)
    #sanity_copy1 = wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "mdc-icon-button mat-mdc-icon-button mat-unthemed mat-mdc-button-base ng-star-inserted")))

    tick1 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='View Server Details'])[1]")))
    tick2 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='View Server Details'])[2]")))
    tick3 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='View Server Details'])[3]")))
    tick4 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='View Server Details'])[4]")))
    tick5 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='View Server Details'])[5]")))

    # wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-main-page[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/app-search[1]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[8]/div[1]/div[1]/app-store-side-tabs[1]/div[1]/div[2]/div[3]/app-store-servers-table[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[5]/div[1]/button[1]/span[3]")))
    # wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-main-page[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/app-search[1]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[8]/div[1]/div[1]/app-store-side-tabs[1]/div[1]/div[2]/div[3]/app-store-servers-table[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[5]/div[1]/button[1]/span[3]")))
    # wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-main-page[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/app-search[1]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[8]/div[1]/div[1]/app-store-side-tabs[1]/div[1]/div[2]/div[3]/app-store-servers-table[1]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[5]/div[1]/button[1]/span[3]")))
    # wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-main-page[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/app-search[1]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[8]/div[1]/div[1]/app-store-side-tabs[1]/div[1]/div[2]/div[3]/app-store-servers-table[1]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[5]/div[1]/button[1]/span[3]")))

    sanity_copy1 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@aria-label='Copy Store Sanity Checks']"))).click()

    close_button = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//i[@class='icon_close']")))
    close_button.click()
    time.sleep(1)



# SELECTING SEARCH FIELD



# GIVING INPUTS ON SEARCH FIELD
# driver.find_element(By.CSS_SELECTOR, '.mat-mdc-form-field-infix').


'''
# METHOD 2: (Using XPATH)
SYNTAX:
//tagname[@attribute='value']
'''
# driver.find_element(By.XPATH, "//input[@type='text']").send_keys('standard_user')
# driver.find_element(By.XPATH, "//input[@type='password']").send_keys('secret_sauce')
# driver.find_element(By.XPATH, "//input[@type='submit']").click()
#message = driver.find_element(By.CLASS_NAME,"form_input").text
# print(message)
# assert "Success" in message

time.sleep(300)