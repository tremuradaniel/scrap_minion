from dbConnection.entities.EntityInterface import EntityInterface


class ProductScrapeValueEntity(EntityInterface):
  TABLE_NAME = "product_scrape_value"
  PRODUCT_WEBSITE_ID_COLUMN = "product_website_id"
  VALUE_COLUMN = "value"
  
  def __init__(self, productWebsiteId, value) -> None:
    self.productWebsiteId = productWebsiteId
    self.value = value
    
  def getInsertValues(self) -> list:
    return [self.productWebsiteId, self.value]
  
  def getTableName(self) -> str:
    return self.TABLE_NAME
  
  def getTableColumns(self) -> str:
    return ",".join(map(str, [self.PRODUCT_WEBSITE_ID_COLUMN, self.VALUE_COLUMN]))
