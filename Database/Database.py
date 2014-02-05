import psycopg2

from Tables.UsersTable import UsersTable

class Database(object):
  def __init__(self):
    self.name = "database"
    self.user = "andres"
    self.tables = {
      "users": UsersTable()
    }
    self.connection = None
    self.cursor = None

  def connectAndInitialize(self):
   # try:
    self.connection = psycopg2.connect(database="database", user="andreas")
    cursor = self.connection.cursor()
    for name, table in self.tables.iteritems():
      table.initialize(cursor)
   # except:
   #   print "Error on connecting to database"
