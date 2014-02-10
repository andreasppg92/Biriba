import psycopg2
import logging

from Tables.UsersTable import UsersTable

class Database(object):
  def __init__(self):
    self.connection = None
    self.name = "database"
    self.user = "andreas"
    self.tables = [
      UsersTable()
    ]

  def connect(self):
    try:
      self.connection = psycopg2.connect(database=self.name, user=self.user)
      logging.info("Connected to database")
    except Exception as e:
      logging.error("Error connecting to database")
      map(logging.debug, str(e).split("\n"))
  
  def initialize(self):
    if self.connection is None:
      logging.error("Intialization needs connection first")
    for table in self.tables:
      table.link(self.connection.cursor())
      if not table.exists():
        table.create()
  
  def dropTables(self):
    for table in self.tables:
      table.drop()
