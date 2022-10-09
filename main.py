from selenium import webdriver
import os
from dotenv import load_dotenv
load_dotenv()
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def get_driver():
  service = Service(os.environ.get('PATH_TO_CHROME_DRIVER'))

  options = webdriver.ChromeOptions()

  # set option to make browsing easier
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("no-sandbox")
  options.add_argument("disable-blink-features=AutomationControlled")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  
  driver = webdriver.Chrome(service=service, options=options)
  
  driver.get(os.environ.get('WEBSITE_ADDRESS') + os.environ.get('WEBSITE_PATH'))
  
  return driver

def main():
  driver = get_driver()
  print(getPrice(driver))
  
def getPrice(driver):
  element = driver.find_element(By.XPATH ,os.environ.get('WEBSITE_XPATH'))
  return element.text.split(" ")[0]

main()