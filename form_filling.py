from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import autoit
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options) 

first_name = "Askar"
last_name = "Suankulova"
email = "askar.suankulova@gmail.com"
phone = "07508865835"

driver.get("https://boards.greenhouse.io/beacon67/jobs/5509540003?gh_src=f923fec23us")

WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'"))
try: 
    name_input = driver.find_element("xpath","//input[contains(@*,'first')]")
except NoSuchElementException:
    name_input = driver.find_element(By.XPATH, ("//*[text()[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'first name')]]/following-sibling::input"))
    print(name_input)
    
try:
    surname_input = driver.find_element("xpath","//input[contains(@*,'last')]")
except NoSuchElementException:
    surname_input = driver.find_element(By.XPATH, ("//*[text()[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'last name')]]/following-sibling::input"))

try:
    email_input = driver.find_element(By.XPATH,"//input[contains(@*,'email')]")
except:
    email_input = driver.find_element(By.XPATH, ("//*[text()[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'email')]]/following-sibling::input"))

    
try:
    phone_input = driver.find_element(By.XPATH,"//input[contains(@*,'phone')]")
except:
    phone_input = driver.find_element(By.XPATH, ("//*[text()[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'phone')]]/following-sibling::input"))
    
try:
    resume_input = driver.find_element(By.XPATH, ("//input[text()[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'attach')]]"))
except:
    resume_input = driver.find_element(By.XPATH, ("//button[text()[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'attach')]]")).click()
    print("Cannot find RESUME element") 
  
#if privacy policy button is on the same level as the label
try:
    privacy_policy_input = driver.find_element(By.XPATH, ("//*[text()[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'privacy policy')]]/following-sibling::select"))
#if privacy policy button/dropdown is inside the span or label 
except:
    privacy_policy_text = driver.find_element(By.XPATH, ("//*[text()[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'privacy policy')]]"))
    privacy_policy_input = privacy_policy_text.find_element(By.XPATH, ("./select"))

    
name_input.send_keys(first_name) 
surname_input.send_keys(last_name) 
email_input.send_keys(email) 
phone_input.send_keys(phone) 
sleep(3)
#upload the cv
autoit.control_send("[CLASS:#32770]", "Edit1", "C:\\Folder\\CV.pdf")
autoit.control_click("[CLASS:#32770]", "Button1")

print("END")