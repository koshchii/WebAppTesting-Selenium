# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:04:29 2021

@author: alexk
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')

#Initialize driver
#driver = w ebdriver.Firefox()
driver = webdriver.Chrome(options=chrome_options)

#Open URL
url = "http://automationpractice.com/index.php"
driver.get(url)

#Maximize window
driver.maximize_window()

#Press "Contuct us" button
contact_xpath = '//*[@id="contact-link"]/a'
contact = driver.find_element_by_xpath(contact_xpath)
contact.click()

#Wait 2 seconds before executing next command
time.sleep(2)

#Press "go back" in the browser and wait
driver.back()
time.sleep(2)

#Press "go forward" in the browser and wait
driver.forward()
time.sleep(2)

#Print the title
print("The current page title: ", driver.title)
time.sleep(2)

#Minimize the screen
driver.minimize_window()
time.sleep(2)

#Maximize the screen
driver.maximize_window()
time.sleep(2)

#Print URL
print("The current URL: ", driver.current_url)
time.sleep(2)

#Reload the page
driver.refresh()
time.sleep(2)

#Close thepage
driver.close()
print("The page was closed sucessfully")
