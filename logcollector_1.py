
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException, StaleElementReferenceException, TimeoutException, NoSuchWindowException
import time
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
browser= webdriver.Chrome(chrome_options=chrome_options)
username='amit'                                                                                                 #username & password given for login
password='Password1'
url="http://spl099rptfe03a.compucom.local:58080/centralized-management/#/physical"                              #url of the website
browser.get(url)
time.sleep(3)
uname=browser.find_element_by_xpath('//*[@id="username"]')
uname.send_keys(username)
time.sleep(2)
passwd=browser.find_element_by_xpath('//*[@id="password"]')
passwd.send_keys(password)
time.sleep(2)
submit= browser.find_element_by_xpath('//*[@id="login-form"]/button/span')
submit.click()
time.sleep(7)


f=open("collectinglogsload","a+")                                                                               #GIVE complete FILEPATH with filename TO change the file where log copy is stored
logline= browser.find_elements_by_xpath('//*[contains(a,"spl099rpt52")]')                                         #prints all the servers name which i need to check
#while logline:
#try:
for log in logline:
    try:
        time.sleep(5)
        log.click()
        time.sleep(5)
        print(log.text)
        f.write(log.text)
        f.write(os.linesep)
    except (NoSuchElementException,ElementNotVisibleException,StaleElementReferenceException,TimeoutException):
        print("loading took long time")
        browser.get(url)
        continue
    except NoSuchWindowException:
        print("reload the page")
        browser.refresh()
        browser.get(url)
        time.sleep(5)
        continue

    time.sleep(5)
    try:
        element = WebDriverWait(browser,10000).until(EC.presence_of_element_located((By.XPATH,'//input[@type="text"]')))
    except (NoSuchElementException,ElementNotVisibleException,StaleElementReferenceException,TimeoutException):
        print("loading took long time-textbox")
        browser.get(url)
        continue
    except NoSuchWindowException:
        print("reload the page")
        browser.refresh()
        browser.get(url)
        time.sleep(5)
        continue
    try:
        browser.find_element_by_xpath('//input[@type="text"]').send_keys('load')                                        #uncomment to find for load balancer logs and comment the below one
        #browser.find_element_by_xpath('//input[@type="text"]').send_keys('emc-watch')                                    #type the module name whose logs you want like 'emc-health' or 'load'
    except(NoSuchElementException,ElementNotVisibleException,StaleElementReferenceException,TimeoutException):
        print("loading took long time-searchbox")
        continue
    except NoSuchWindowException:
        print("reload the page")
        browser.refresh()
        browser.get(url)
        time.sleep(5)
        continue
    time.sleep(10)
    try:
        browser.find_element_by_xpath('//*[@class="ui-icon ui-icon-arrowthick-1-s"]').click()
        time.sleep(20)
    except(NoSuchElementException ,ElementNotVisibleException, StaleElementReferenceException,TimeoutException):
        print("loading took long time-drilldown")
        continue
    except NoSuchWindowException:
        print("reload the page")
        browser.refresh()
        browser.get(url)
        time.sleep(5)
        continue
    try:
        browser.find_element_by_xpath('//*[@id="content"]/div/div[6]/h3/a').click()
        time.sleep(20)
    except(NoSuchElementException,ElementNotVisibleException,StaleElementReferenceException,TimeoutException):
        print("loading took long time-logname")
        continue
    except NoSuchWindowException:
        print("reload the page")
        browser.refresh()
        browser.get(url)
        time.sleep(5)
        continue
    try:
        browser.find_element_by_xpath('//*[@class="ui-icon ui-icon-print"]').click()
        time.sleep(20)
    except (NoSuchElementException,ElementNotVisibleException,StaleElementReferenceException,TimeoutException):
        print("loading took long time-logdrilldown")
        continue
    except NoSuchWindowException:
        print("reload the page")
        browser.refresh()
        browser.get(url)
        time.sleep(5)
        continue
    try:
        logs= browser.find_elements_by_xpath('//code')
        for line in logs:                                                                                               #the loop which writes in a file can comment to disable it
            print(line.text)
            f.write(line.text)
            f.write(os.linesep)
        time.sleep(20)
    except(NoSuchElementException,ElementNotVisibleException,StaleElementReferenceException,TimeoutException):
        print("loading took long time-copycode")
        browser.refresh()
        continue
    except NoSuchWindowException:
        print("reload the page")
        browser.refresh()
        browser.get(url)
        time.sleep(5)
        continue
    try:
        browser.find_element_by_xpath('//*[@id="file-view-close"]/span').click()
        time.sleep(20)
    except (NoSuchElementException,ElementNotVisibleException,StaleElementReferenceException,TimeoutException):
        print("loading took long time-close button")
        continue
    except NoSuchWindowException:
        print("reload the page")
        browser.refresh()
        browser.get(url)
        time.sleep(5)
        continue
    browser.get(url)
    time.sleep(5)

f.close()
browser.find_element_by_xpath('//*[@id="header-logout"]').click()                                                       # click action for logout
browser.quit()





