import os
import time
import pyperclip
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common import StaleElementReferenceException

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def run_check(x, driver, check_type, main_directory, full_directory_path, screenshot_outputs, notepad_outputs):
    wait = WebDriverWait(driver, 120)

    driver.get("https://onesupport.apps.homedepot.com/")
    driver.maximize_window()

    # SIGN IN
    driver.find_element(By.ID, 'inputUsername').send_keys('rc982be')
    driver.find_element(By.ID, 'inputPassword').send_keys('fry.brute.hax-06')
    driver.find_element(By.ID, 'buttonSignOn').click()

    input_element = wait.until(expected_conditions.presence_of_element_located((By.ID, 'mat-input-0')))
    input_element.clear()
    input_element.send_keys(x)

    submit_button = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    submit_button.click()

    copy_button_1 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-main-page[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/app-search[1]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[1]/div[1]/div[1]/app-store-side-tabs[1]/div[1]/div[2]/div[1]/app-store-health[1]/div[1]/mat-expansion-panel[1]/div[1]/mat-action-row[1]/button[1]/span[4]")))
    copy_button_2 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-main-page[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/app-search[1]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[1]/div[1]/div[1]/app-store-side-tabs[1]/div[1]/div[2]/div[1]/app-store-health[1]/div[1]/mat-expansion-panel[2]/div[1]/mat-action-row[1]/button[1]/span[4]")))
    copy_button_3 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/app-main-page[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/app-search[1]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[1]/div[1]/div[1]/app-store-side-tabs[1]/div[1]/div[2]/div[1]/app-store-health[1]/div[1]/mat-expansion-panel[3]/div[1]/mat-action-row[1]/button[1]/span[4]")))

    driver.execute_script("document.body.style.zoom = '67%'")
    screenshot_name = f"ST{x}-{'post' if check_type == 'post-check' else 'pre'}-check.png"
    screenshot_path = os.path.join(full_directory_path, screenshot_name)
    driver.save_screenshot(screenshot_path)
    screenshot_outputs[x] = screenshot_path
    driver.execute_script("document.body.style.zoom = '100%'")

    # Click server button
    server_button = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/app-root[1]/div[1]/app-main-page[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/app-search[1]/div[1]/mat-tab-group[1]/div[1]/mat-tab-body[1]/div[1]/div[1]/app-store-side-tabs[1]/div[1]/div[1]/button[3]/img[1]')))
    driver.execute_script("arguments[0].click();", server_button)

    time.sleep(5)

    try:
        wifi5 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Open Server Options'])[9]")))
        wifi5.click()

    except StaleElementReferenceException:
        time.sleep(5)
        wifi5 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Open Server Options'])[9]")))
        wifi5.click()

    sanity_check = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@aria-label='Run All Sanity Checks']")))
    sanity_check.click()

    tick1 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='View Server Details'])[1]")))
    tick2 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='View Server Details'])[2]")))
    tick3 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='View Server Details'])[3]")))
    tick4 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='View Server Details'])[4]")))
    tick5 = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@aria-label='View Server Details'])[5]")))

    # Copy sanity check result
    sanity_copy = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@aria-label='Copy Store Sanity Checks']"))).click()
    time.sleep(1)
    clipboard_text = pyperclip.paste()

    # Save sanity check result to file
    if check_type in ['pre-check', 'post-check']:
        file_name = f"ST{x}-{'post' if check_type == 'post-check' else 'pre'}-sanity.txt"
        file_path = os.path.join(full_directory_path, file_name)
        with open(file_path, 'w') as file:
            file.write(clipboard_text)
        error_index = clipboard_text.find("<<< OneSupport Sanity Check Error(s) and Notice(s) Summary >>>")
        classification = "ERROR" if error_index != -1 and "Errors:" in clipboard_text[error_index:] else "OK"
        notepad_outputs[x] = (file_path, classification)

    driver.quit()

main_directory = r'C:\Users\RC982BE\Downloads\TEST'

check_type = input("Enter the type of check (sanity, pre-check, or post-check): ").strip().lower()

while check_type not in ['sanity', 'pre-check', 'post-check']:
    print("Invalid input. Please enter 'sanity', 'pre-check', or 'post-check'.")
    check_type = input("Enter the type of check: ").strip().lower()

if check_type in ['pre-check', 'post-check']:
    today_date = time.strftime("%Y-%m-%d")
    directory_name = today_date + '-' + check_type.replace('-', '_')
    full_directory_path = os.path.join(main_directory, directory_name)
    create_directory(full_directory_path)

# stores = ['7146', '7262', '1855', '2213', '3847', '4020', '4742', '6377']
# stores = ['4020']
# stores = ['7146', '7262', '1855', '3847']
stores = ['6377', '4020', '4742']

screenshot_outputs = {}
notepad_outputs = {}

threads = []
start_time = time.time()

for x in stores:
    t = threading.Thread(target=run_check, args=(x, webdriver.Chrome(), check_type, main_directory, full_directory_path, screenshot_outputs, notepad_outputs))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

sorted_screenshot_outputs = dict(sorted(screenshot_outputs.items()))
sorted_notepad_outputs = dict(sorted(notepad_outputs.items()))

print("\nScreenshot Outputs:")
for store, screenshot_path in sorted_screenshot_outputs.items():
    print(f"{store} ---> screenshot saved to {screenshot_path}")

print("\nNotepad Outputs:")
for store, (file_path, classification) in sorted_notepad_outputs.items():
    print(f"{store} ---> SANITY({classification}) report saved to {file_path}")

end_time = time.time()
elapsed_time_seconds = end_time - start_time
elapsed_minutes = int(elapsed_time_seconds // 60)
remaining_seconds = int(elapsed_time_seconds % 60)
print(f"\nElapsed time: {elapsed_minutes} minutes {remaining_seconds} seconds")
print("All checks completed.")