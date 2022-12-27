from dbConnection.MySqlConnection import MySqlConnection

class ProductScrapeValueManager(MySqlConnection):

  def insertProductScrapeValue(self):
    # TODO: make this sql injection not friendly
    self.cursor.execute("""INSERT INTO %s (%s) VALUES (%s);""" % (
      self.entity.getTableName(),
      self.entity.getTableColumns(),
      self.entity.getInsertValues()
      ))
    self.connection.commit()
    self._closeConnection()
