import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import NoSuchElementException, ElementClickInterceptedException, TimeoutException, \
    StaleElementReferenceException

driver = webdriver.Chrome()
driver.get("https://onesupport.apps.homedepot.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)


# SIGN IN
driver.find_element(By.ID, 'inputUsername').send_keys('rc982be')
driver.find_element(By.ID, 'inputPassword').send_keys('fry.brute.hax-06')
driver.find_element(By.ID, 'buttonSignOn').click()
time.sleep(2)



stores = ['0121', '0508', '0947', '1540', '2583', '4621', '6542', '7159']
#US0121 US0508 US0947 US1540 US2583 US4621 US6542 CA7159

wait = WebDriverWait(driver, 120)

start_time = time.time()

for x in stores:
    input_element = wait.until(expected_conditions.presence_of_element_located((By.ID, 'mat-input-0')))
    input_element.clear()
    input_element.send_keys(x)

    submit_button = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    submit_button.click()

    server_button = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/app-root[1]/div[1]/app-main-page[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/app-search[1]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[1]/div[1]/div[1]/app-store-side-tabs[1]/div[1]/div[1]/button[3]/img[1]')))
    driver.execute_script("arguments[0].click();", server_button)

    # Wait for a short period to allow for any changes to the DOM
    time.sleep(2)

    try:
        wifi5 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Open Server Options'])[9]")))
        wifi5.click()


    except StaleElementReferenceException:
        time.sleep(2)
        wifi5 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Open Server Options'])[9]")))
        wifi5.click()

    # time.sleep(3)

    # wifi1 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Open Server Options'])[1]")))
    # wifi2 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Open Server Options'])[3]")))
    # wifi3 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Open Server Options'])[5]")))
    # wifi4 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Open Server Options'])[7]")))
    #wifi5 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Open Server Options'])[9]")))

    #stupsh01 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//td[@role='cell'][normalize-space()='stupsh01'])[2]")))

    sanity_check = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@aria-label='Run All Sanity Checks']")))
    sanity_check.click()

    tick1 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='View Server Details'])[1]")))
    tick2 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='View Server Details'])[2]")))
    tick3 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='View Server Details'])[3]")))
    tick4 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='View Server Details'])[4]")))
    tick5 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='View Server Details'])[5]")))

    sanity_copy = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@aria-label='Copy Store Sanity Checks']"))).click()


    time.sleep(0.5)

    clipboard_text = pyperclip.paste()

    error_index = clipboard_text.find("<<< OneSupport Sanity Check Error(s) and Notice(s) Summary >>>")
    if error_index != -1 and "Errors:" in clipboard_text[error_index:]:
        classification = "ERROR"
    else:
        classification = "OK"

    server_id_index = clipboard_text.find("~~~ ST")
    server_id = clipboard_text[server_id_index + 4: server_id_index + 10]

    print(f"{server_id} ---> {classification}")



    close_button = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//i[@class='icon_close']")))
    close_button.click()
    #time.sleep(1)


end_time = time.time()  # Record the ending time
elapsed_time_seconds = end_time - start_time  # Calculate elapsed time in seconds

# Calculate minutes and remaining seconds
elapsed_minutes = int(elapsed_time_seconds // 60)
remaining_seconds = int(elapsed_time_seconds % 60)

print(f"Elapsed time: {elapsed_minutes} minutes {remaining_seconds} seconds")