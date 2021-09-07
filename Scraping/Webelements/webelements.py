# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:12:32 2021

@author: alexk
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

#Initialize driver
driver = webdriver.Firefox()

#URLs to explore
shopping_url = "http://automationpractice.com/index.php"
flight_url = "http://www.edreams.com/"

#Open URL and maximize window
url = shopping_url
driver.get(url)
driver.maximize_window()
time.sleep(2)

#Interact with Box and Button elements
search_id = 'search_query_top'
search_box = driver.find_element_by_id(search_id)
search_box.click()

#Input text in the box
search_box.send_keys('PulloverX')
time.sleep(2)

#Remove one symbol
search_box.send_keys(Keys.BACK_SPACE)
time.sleep(2)

#Remove the whole text
search_box.clear()

#Press search button
search_button_name = 'submit_search'
search_button = driver.find_element_by_name(search_button_name)
search_button.click()
time.sleep(2)
driver.close()
time.sleep(2)

#Open another URL with chrome and maximize window
driver = webdriver.Chrome()
url = flight_url
driver.get(url)
driver.maximize_window()
time.sleep(2)

#Accept policies
terms_button_id = 'didomi-notice-agree-button'
terms_button = driver.find_element_by_id(terms_button_id)
terms_button.click()
time.sleep(2)

#Ineract with Radial Button
one_way_xpath = '//*[@id="react-app"]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div/div[2]/label/div/div[2]/span'
one_way_rad_button = driver.find_element_by_xpath(one_way_xpath)
one_way_rad_button.click()
time.sleep(2)

#Interact with Check Box
direct_flights_only_class = '//*[@id="react-app"]/div/div/div[1]/div/div[2]/div/div[1]/div[3]/div/label/div/div[1]/span/span/span'
direct_flights_only_box = driver.find_element_by_xpath(direct_flights_only_class)
direct_flights_only_box.click()
time.sleep(2)

#Interact with Tab element
hotel_xpath = '//div/span[2][text()="Hotels"]'
hotel_tab = driver.find_element_by_xpath(hotel_xpath)
hotel_tab.click()
time.sleep(2)

#Interact with Static Drop Down Menu
'''
Here one need to be carefull. The hotel Tab contains
static drop down menus "Rooms", "Adults", and "Children"
which belong to iFrame. Therefore, in order to interact
with these menues one needs to switch to the corresponding
iFrame in the first place. iFrames can be acessed by:
Index (0, 1, ...), Name, ID, or Webelement. If
Name, ID, or Webelement are not provided (as in our case)
the Index of a particular iFrame can be deduced using
the script below:

iframes_dict = driver.find_elements_by_tag_name("iframe")
size = len(iframes_dict)
print(f'Number of iFrames on this page: {size}.')

for indx in range(size-1):
    driver.switch_to.frame(indx)
    #check if "Rooms" box belongs to this frame
    rooms_name = 'no_rooms'
    rooms = len(driver.find_elements_by_name(rooms_name))
    #if the element doesn't belong to this frame then rooms = 0
    if rooms:
        print(f'The "Rooms" box belongs to iFrame with index {indx}.')
    driver.switch_to.default_content()

One can see that we need to work with iFrame number 1
'''

#Switch to frame 1
driver.switch_to.frame(1)
time.sleep(2)

#Select 3 rooms, 2 adults, 1 child
rooms_name = 'no_rooms'
rooms = driver.find_element_by_name(rooms_name)
dropdown_rooms = Select(rooms)
dropdown_rooms.select_by_index('2')
time.sleep(2)

adults_name = 'group_adults'
adults = driver.find_element_by_name(adults_name)
dropdown_adults = Select(adults)
dropdown_adults.select_by_value('2')
time.sleep(2)

children_name = 'group_children'
children = driver.find_element_by_name(children_name)
dropdown_children = Select(children)
dropdown_children.select_by_index('1')
time.sleep(2)

#Return to defualt content (Flights tab)
driver.switch_to.default_content() 
flights_tab_xpath = '//div/span[2][text()="Flights"]'
flights_tab = driver.find_element_by_xpath(flights_tab_xpath)
flights_tab.click()

#Interact with Hyperlinks
click_here_xpath = '//div/span[2]/a[@href]'
covid_click_here_link = driver.find_element_by_xpath(click_here_xpath)
covid_click_here_link.click()
time.sleep(2)

