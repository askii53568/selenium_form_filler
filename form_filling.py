from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options) 

first_name = "Askar"
last_name = "Suankulova"
email = "askar.suankulova@gmail.com"
phone = "07508865835"

driver.get("https://apply.workable.com/starling-bank/j/29599F93AF/apply/")

WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'"))
try: 
    name_input = driver.find_element("xpath","//input[contains(@id | @name,'first')]")
    surname_input = driver.find_element("xpath","//input[contains(@id | @name,'last')]")
    email_input = driver.find_element("xpath","//input[contains(@id | @name,'email')]")
    phone_input = driver.find_element("xpath","//input[contains(@id | @name,'phone')]")
    resume_input = driver.find_element("xpath","//input[contains(@*,'resume')]")
    
    name_input.send_keys(first_name) 
    surname_input.send_keys(last_name) 
    email_input.send_keys(email) 
    phone_input.send_keys(phone) 
except NoSuchElementException:
    print("NO SUCH ELEMENT")