# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 16:40:30 2021
@author: alexk

CSS basic structure:

tag[attribute="value"]

if "attribute" == "id", then the CSS shortcut is:
#value

if "attribute" == "class", then the CSS shortcut is:
.value
"""

import time
from selenium import webdriver

#Initialize driver
driver = webdriver.Chrome()

#Open URL and maximize window
url = "http://automationpractice.com/index.php"
driver.get(url)
driver.maximize_window()

#Relative CSS selector
cart_CSS = 'a[title="View my shopping cart"]'
cart_element = driver.find_element_by_css_selector(cart_CSS)
cart_element.click()
time.sleep(2)

#CSS selector using id attribute
logo_CSS_id = '#header_logo'
logo_element = driver.find_element_by_css_selector(logo_CSS_id)
logo_element.click()
time.sleep(2)

#CSS selector using class attribute
sign_in_CSS_class = '.login'
sign_in_element = driver.find_element_by_css_selector(sign_in_CSS_class)
sign_in_element.click()
