import os
import time
import random
from selenium import webdriver
from dotenv import load_dotenv
from LoggerClass import LoggerClass
from MailerClass import MailerClass
from dbConnection.entities.ProductScrapeValueEntity import ProductScrapeValueEntity
from dbConnection.managers.ProductScrapeValueManager import ProductScrapeValueManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
load_dotenv()

class MainController():
  def __init__(self) -> None:
    self.logger = LoggerClass()
    self.mailer = MailerClass()
  
  def execute(self):
    try:
      self._simulateRandomAccess()
      driver = self.get_driver()
      self.value = self._getPrice(driver)
      self._saveScrape(self.value)
      self._notify(self.value)
    except BaseException as e:
      self.logger.logError(e)
    

  def _get_driver(self):
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
  def _simulateRandomAccess(self):
    time.sleep(self._minutesToSecond(self._getRandomIntForMax(os.environ.get('MAX_WAITING'))))
    
    
  def _getRandomIntForMax(self, int):
    return round(random.random() * int)

  def _minutesToSecond(self, minutes):
    return minutes * 60
    
  def _getPrice(self, driver):
    element = driver.find_element(By.XPATH, os.environ.get('WEBSITE_XPATH'))
    return element.text.split(" ")[0]

  def _saveScrape(self, value: float):
    entity = ProductScrapeValueEntity(os.environ.get('PRODUCT_SCRAPE_ID'), value)
    manager = ProductScrapeValueManager(entity, self.logger)
    manager.insertProductScrapeValue()
    
  def _notify(self, value):
    if value <= (int) (os.environ.get('ALERT_FOR_QTY')):
      self.mailer.sendAlert("Threshold has beend passed", "The threshold for you product has been passed")
    

main = MainController()
main.execute()
