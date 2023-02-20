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
first_name = "Diana"
last_name = "Suankulova"

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
apply_buttons = driver.find_elements("xpath", "//button[@data-testid='apply-button']")
for apply_button in apply_buttons:
    apply_button.click()
    #waits to load all the job details
    #we do this by making sure any paragraphs within the apply-content div are loaded
    #the assumption is that if a paragraph within the div is loaded, the rest of the content is loaded too
    WebDriverWait(driver=driver, timeout=30).until(EC.visibility_of_element_located(("xpath","//div[@data-testid='apply-content']//p")))
    try:
        #Finds the div with "Apply on ___" 
        element = driver.find_element("xpath","//*[contains(text(), 'Or apply on')]")
        #Finds the hyoerlink of the application website within the div
        website_link = element.find_element("xpath",".//a")
        link = website_link.get_attribute("href")
        #if the job listing is on workable, then we will see 2 tabs, one with the listing and the other with 
        #the application form. the application form is accessable via /apply
        #the <a> tag coming from otta will have source=Otta attached to the href by default
        #we replace that with "apply/" to automatically access the form
        if "workable" in link:
            driver.get(link.replace("?utm_source=Otta","apply/"))
        else:
            driver.get(website_link.get_attribute("href"))
    except NoSuchElementException:
        apply_button = driver.find_element("xpath", "//button[@data-testid='apply-modal-external-button']")
        apply_button.click()
    

          
driver.close()










