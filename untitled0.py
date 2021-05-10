#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 19:47:16 2021

@author: davidhinton
"""


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



#Web driver is what links up what browser and helps to drive actions
path = '/Users/davidhinton/Documents/ccc_prod_webscraper/chromedriver'

url =  'https://masscannabiscontrol.com/product-catalog/'


def main(driver):
    try:
    
        driver.get(url)
        WebDriverWait(driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe"))
        )
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn"))
        ).click()
        
    
       
        search = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div/input"))
        )
        
        search.send_keys("")
        search.send_keys(Keys.RETURN)
        
        
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[3]/div[2]/div[1]/div[1]/div"))
        ).click()
        
        
        
        product_id = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.fade.modal.show > div > div > div.modal-header > div"))
        )
        
        print(product_id.text)
        
       
        #for product in page_element:
            
            #product_id = WebDriverWait(driver, 20).until(
             #   EC.presence_of_element_located(By.CLASS_NAME, "px-3 modal-title h4"))
            #product_id.text
        
    except:
        driver.quit()
    
#class="item-grid-result h-100"


# if __name__ == "__main__":
#     driver = webdriver.Chrome(path)

#     main(driver)



#driver = webdriver.Chrome(executable_path = path)

#driver.get(url)

#pop_up = driver.find_element(By.CLASS_NAME, 'btn btn-primary btn-lg m-3')

#pop_up.click()

#try:
   # WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[1]/div[2]/div[2]/button'))).click()
#except:
 #   driver.quit()