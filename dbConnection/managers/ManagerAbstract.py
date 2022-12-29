from abc import ABC

class ManagerAbstract(ABC):
  INSERT_VALUE_TEMPLATE = "%s"
  def getInsertValuesTemplate(self, values: list) -> str:
    valueInstances = []
    for _ in values:
      valueInstances.append(self.INSERT_VALUE_TEMPLATE)
    
    return ",".join(map(str, valueInstances))
    