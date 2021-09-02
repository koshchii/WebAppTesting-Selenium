# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 19:24:31 2021

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
time.sleep(2)

#Search with id locator
search_id = 'search_query_top'
search_element = driver.find_element_by_id(search_id)
search_element.click()
search_element.send_keys('Hello')
time.sleep(2)

#Submit search with name locator
submit_search_name = 'submit_search'
submit_search_element = driver.find_element_by_name(submit_search_name)
submit_search_element.click()
time.sleep(2)

#Sign in with class locator
sign_in_class = 'login'
sign_in_element = driver.find_element_by_class_name(sign_in_class)
sign_in_element.click()
time.sleep(2)

#Contact us with link locator
contact_link = 'Contact us'
contact_element = driver.find_element_by_link_text(contact_link)
contact_element.click()
time.sleep(2)

#My orders with partial link locator
orders_plink = 'orders'
orders_element = driver.find_element_by_partial_link_text(orders_plink)
orders_element.click()
time.sleep(2)
