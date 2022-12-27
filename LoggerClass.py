import os
import logging
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class LoggerClass:
  def __init__(self) -> None:
    logging.basicConfig( 
      filename=Path(os.environ.get('LOG_FILE')),
      filemode='a',
      level=logging.DEBUG,
      format= '%(asctime)s - %(levelname)s - %(message)s',
    )
    
  def logError(self, error) -> None:
    logging.exception(str(error))
    
  def logInfo(self, msg) -> None:
    logging.info(msg)
  