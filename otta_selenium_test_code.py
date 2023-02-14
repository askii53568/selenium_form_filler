from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

##Test code

#Print all company names on the page    

jobs = driver.find_elements("xpath", "//p[@data-testid='job-company-name']")
for job in jobs:
    print(job.text)
    
#
#


#Find saved section heading
if "Saved" in driver.find_element("xpath", "//div[@data-testid='shortlist-section']/div/h3").text:
    print("Found it!")
    
#
#

# WebDriverWait(driver=driver, timeout=10).until(
#     lambda x: x.execute_script("return document.readyState === 'complete'")
# )
# error_message = "Incorrect username or password."
# # get the errors (if there are)
# errors = driver.find_elements("css selector", ".flash-error")
# # print the errors optionally
# # for e in errors:
# #     print(e.text)
# # if we find that error message within errors, then login is failed
# if any(error_message in e.text for e in errors):
#     print("[!] Login failed")
# else:
#     print("[+] Login successful")