from selenium import webdriver
import os
import time
import random
from dotenv import load_dotenv
load_dotenv()
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def main():
  simulateRandomAccess()
  driver = get_driver()
  print(getPrice(driver))

def get_driver():
  service = Service(os.environ.get('PATH_TO_CHROME_DRIVER'))

  options = webdriver.ChromeOptions()

  # set option to make browsing easier
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("no-sandbox")
  options.add_argument("disable-blink-features=AutomationControlled")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("--headless")
  driver = webdriver.Chrome(service=service, options=options)
  
  driver.get(os.environ.get('WEBSITE_ADDRESS') + os.environ.get('WEBSITE_PATH'))
  
  return driver

"""
  simulateRandomAccess() - delay the running of the script so that 
  the access will not be made each day in order to reduce the 
  suspicion of scraping 
"""
def simulateRandomAccess():
  time.sleep(minutesToSecond(getRandomIntForMax(os.environ.get('MAX_WAITING'))))
  
  
def getRandomIntForMax(int):
  return round(random.random() * int)

def minutesToSecond(minutes):
  return minutes * 60
  
def getPrice(driver):
  element = driver.find_element(By.XPATH, os.environ.get('WEBSITE_XPATH'))
  return element.text.split(" ")[0]

main()