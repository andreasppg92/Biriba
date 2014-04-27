import logging

class BaseTable(object):
  
  def __init__(self):
    self.name = "None"
    self.fields = {}
    self.cursor = None

  def link(self, cursor):
    self.cursor = cursor

  def exists(self):
    command = "SELECT * FROM information_schema.tables WHERE table_name=%s"
    self.cursor.execute(command, (self.name, ))
    return self.cursor.rowcount == 1

  def create(self):
    command = "CREATE TABLE " + self.name
    fields = []
    for field, details in self.fields.iteritems():
      fields.append(field + " " + details)
    self.cursor.execute(command + " (" + ", ".join(fields) + ")")
    self.cursor.connection.commit()
    logging.info("Table " + self.name + " created")

  def drop(self):
    self.cursor.execute("DROP TABLE " + self.name)
    self.cursor.connection.commit()
    logging.info("Table " + self.name + " droped")
