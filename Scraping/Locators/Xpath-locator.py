# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 13:35:09 2021
@author: alexk

Relative Xpath basic structure:

//tag[@attribute="value"]
"""

import time
from selenium import webdriver

#Initialize driver
driver = webdriver.Chrome()

#Open URL and maximize window
url = "http://automationpractice.com/index.php"
driver.get(url)
driver.maximize_window()

#Use relative Xpath
cart_Xpath = '//a[@title="View my shopping cart"]'
cart_element = driver.find_element_by_xpath(cart_Xpath)
cart_element.click()
time.sleep(2)
driver.close()
time.sleep(2)

#Use absolute Xpath
driver = webdriver.Chrome()
url = "http://automationpractice.com/index.php"
driver.get(url)

cart_abs_Xpath = '/html/body/div/div[1]/header/div[3]/div/div/div[3]/div/a'
cart_element = driver.find_element_by_xpath(cart_abs_Xpath)
cart_element.click()
time.sleep(2)