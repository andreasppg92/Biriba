import psycopg2
import logging

from Tables.UsersTable import UsersTable

class Database(object):
  def __init__(self):
    self.connection = None
    self.name = "database"
    self.user = "andreas"
    self.tables = {
      "users": UsersTable()
    }

  def connect(self):
    try:
      self.connection = psycopg2.connect(database=self.name, user=self.user)
      for _, table in self.tables.iteritems():
        table.link(self.connection.cursor())
      logging.info("Connected to database")
    except Exception as e:
      logging.error("Error connecting to database")
      map(logging.debug, str(e).split("\n"))
  
  def initialize(self):
    if self.connection is None:
      logging.error("Intialization needs connection first")
      return
    for _, table in self.tables.iteritems():
      if not table.exists():
        table.create()
  
  def dropTables(self):
    for _, table in self.tables.iteritems():
      table.drop()
