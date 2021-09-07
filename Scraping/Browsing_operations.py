# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:04:29 2021

@author: alexk
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Run Chrome in background (uncomment to test)
#chrome_options = Options()
#chrome_options.add_argument('--headless')
#driver = webdriver.Chrome(options=chrome_options)

#Initialize driver
driver = webdriver.Chrome()
#Chose URL to open
url = "http://automationpractice.com/index.php"
driver.get(url)

#Maximize Chrome window
driver.maximize_window()

#Press the "Contact us" button
contact_xpath = '//*[@id="contact-link"]/a'
contact = driver.find_element_by_xpath(contact_xpath)
contact.click()

#Wait 2 seconds before executing next command
time.sleep(2)

#Press browser's "go back" button
driver.back()
time.sleep(2)

#Press browser's "go forward" button
driver.forward()
time.sleep(2)

#Page title
print("The current page title: ", driver.title)
time.sleep(2)

#Minimize the screen
driver.minimize_window()
time.sleep(2)

#Page URL
print("The current URL: ", driver.current_url)
time.sleep(2)

#Reload the page
driver.refresh()
time.sleep(2)

#Close the page
driver.close()
print("The page was closed sucessfully")
