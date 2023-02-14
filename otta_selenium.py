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

email = "diana.suankulova@gmail.com"
password = "U2sdqMqjR#7-Twu"

#open otta.com
driver.get("http://app.otta.com/login")
driver.find_element("id","email").send_keys(email)
driver.find_element("id","password").send_keys(password)
driver.find_element("xpath",'//*[@id="root"]/div[1]/div/div/div[1]/form/div[3]/button').click()


time.sleep(5)


WebDriverWait(driver=driver, timeout=10).until(EC.visibility_of_element_located(("xpath", "//div[@data-testid='shortlist-section']")))
#Find "Saved" heading
saved_heading = driver.find_element("xpath", "//div[@data-testid='shortlist-section']/div/h3[text()='Saved']")
#Find "Shortlist" section
saved_shortlist = saved_heading.find_element("xpath","./../..")
#Find immediately available saved jobs
#saved_jobs = saved_shortlist.find_elements("xpath", "p[@data-testid='job-company-name']")
#Find all apply links
jobs = driver.find_elements("xpath", "//a[@data-testid='apply-button-link']")
for job in jobs:
    driver.get(job.get_attribute("href"))
    #waits to load all the job details
    WebDriverWait(driver=driver, timeout=30).until(EC.visibility_of_element_located(("xpath","//div[@data-testid='apply-content']/*")))
    try:
        #Finds the div with "Apply on ___" 
        element = driver.find_element("xpath","//*[contains(text(), 'Or apply on')]")
        #Finds the hyoerlink of the application website within the div
        website_link = element.find_element("xpath",".//a")
        driver.get(website_link.get_attribute("href"))
    except NoSuchElementException:
        apply_button = driver.find_element("xpath", "//button[@data-testid='apply-modal-external-button']")
        apply_button.click()

          
driver.close()










