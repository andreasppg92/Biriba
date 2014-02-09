import psycopg2
import logging

from Tables.UsersTable import UsersTable
from Operator import Operator

class Database(object):
  def __init__(self):
    self.name = "database"
    self.user = "andreas"
    self.operator = None
    self.tables = [
      UsersTable()
    ]

  def connect(self):
    try:
      connection = psycopg2.connect(database=self.name, user=self.user)
    except Exception as e:
      logging.error("Error connecting to database")
      map(logging.debug, e.split("\n"))
      return
    
    self.operator = Operator(connection)
    logging.info("Connected to database")
  
  def createTables(self):
    for table in self.tables():
      self.operator.queue(table.drop())
      self.operator.queue(table.create())
    self.operator.executeAll()
    self.operator.commit()
    logging.info("Tables created")
