import os
import time
import random
from selenium import webdriver
from dotenv import load_dotenv
from LoggerClass import LoggerClass
from dbConnection.entities.ProductScrapeValueEntity import ProductScrapeValueEntity
from dbConnection.managers.ProductScrapeValueManager import ProductScrapeValueManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
load_dotenv()

class MainController():
  def __init__(self) -> None:
    self.logger = LoggerClass()
  
  def execute(self):
    try:
      self.simulateRandomAccess()
      driver = self.get_driver()
      self.saveScrape(self.getPrice(driver))
    except BaseException as e:
      self.logger.logError(e)
    

  def get_driver(self):
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
  def simulateRandomAccess(self):
    time.sleep(self.minutesToSecond(self.getRandomIntForMax(os.environ.get('MAX_WAITING'))))
    
    
  def getRandomIntForMax(self, int):
    return round(random.random() * int)

  def minutesToSecond(self, minutes):
    return minutes * 60
    
  def getPrice(self, driver):
    element = driver.find_element(By.XPATH, os.environ.get('WEBSITE_XPATH'))
    return element.text.split(" ")[0]

  def saveScrape(self, value: float):
    entity = ProductScrapeValueEntity(os.environ.get('PRODUCT_SCRAPE_ID'), value) # '1); DROP table test; -- '
    manager = ProductScrapeValueManager(entity, self.logger)
    manager.insertProductScrapeValue()
    

main = MainController()
main.execute()
