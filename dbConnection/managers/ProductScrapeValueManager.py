from dbConnection.MySqlConnection import MySqlConnection
from dbConnection.managers.ManagerAbstract import ManagerAbstract

class ProductScrapeValueManager(MySqlConnection, ManagerAbstract):
  def insertProductScrapeValue(self):
    stmt = """
      INSERT INTO {} ({}) VALUES({});
    """.format(
      self.entity.getTableName(), 
      self.entity.getTableColumns(),
      self.getInsertValuesTemplate(self.entity.getInsertValues())
    )

    self.cursor.execute(stmt, 
        (self.entity.getInsertValues())
    )

    self.connection.commit()
    self._closeConnection()
