import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
from LoggerClass import LoggerClass
from dbConnection.entities.EntityInterface import EntityInterface
load_dotenv()

class MySqlConnection:
  def __init__(self, entity: EntityInterface, logger: LoggerClass):
    self.entity = entity
    self.logger = logger
    self._getConnection()
  
  """
    returns True if connection successful, False if not
  """
  def _getConnection(self) -> bool:
    self.connection = mysql.connector.connect(
      host= os.environ.get('HOST'),
      database= os.environ.get('DATABASE'),
      user= os.environ.get('USER'),
      password= os.environ.get('PASSWORD')
    )
    
    if self.connection.is_connected():
        db_Info = self.connection.get_server_info()
        self.logger.logInfo("Connected to MySQL Server version " + db_Info)
        self.cursor = self.connection.cursor()
        return True
      
    return False
    
  def _closeConnection(self):
    if self.connection.is_connected():
        self.cursor.close()
        self.connection.close()
        self.logger.logInfo("MySQL connection is closed")
        