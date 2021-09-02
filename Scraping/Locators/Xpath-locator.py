# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 13:35:09 2021

@author: alexk
"""

import time
from selenium import webdriver

#Initialize driver
driver = webdriver.Chrome()

#Open URL and maximize window
url = "http://automationpractice.com/index.php"
driver.get(url)
driver.maximize_window()

'''
Xpath basic structure:
    
//tag[@attribute="value"]
'''

#Use relative Xpath
#cart_Xpath = '//a[@title="View my shopping cart"]'
#cart_element = driver.find_element_by_xpath(cart_Xpath)
#cart_element.click()

#Use absolute Xpath
cart_abs_Xpath = '/html/body/div/div[1]/header/div[3]/div/div/div[3]/div/a'
cart_element = driver.find_element_by_xpath(cart_abs_Xpath)
cart_element.click()
