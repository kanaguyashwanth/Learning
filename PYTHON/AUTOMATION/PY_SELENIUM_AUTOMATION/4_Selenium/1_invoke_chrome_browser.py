import time
from selenium import webdriver

# If the Selenium driver version and Chrome version are up-to-date, the below lines work well
driver = webdriver.Chrome()
driver.get("https://google.co.in")


# If it doesn't work well, then we have to follow the below steps:
'''
PROCESS:
- First, we need to talk to chrome driver
- Chrome driver(middle man) interprets all webdriver commands and invokes them on chrome browser.
- Without driver, we can start talking with the browser
'''
# service_object = Service("directory_of_chrome_driver")
# webdriver.chrome(service = service_object)











time.sleep(2)