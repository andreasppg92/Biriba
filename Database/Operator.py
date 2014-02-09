import Queue
import logging

class Operator(object):
  def __init__(self, connection):
    self.connection = connection
    self.cursor = connection.cursor()
    self.commands = Queue.Queue()

  def queue(self, command):
    self.commands.add(command)

  def execute(self, command):
    try:
      self.cusor(command)
    except Exception as e:
      logging.warning("SQL. " + command)
      map(logging.debug, e.split("\n"))

  def executeAll(self):
    while not self.commands.empty():
      self.execute(self.commands.get())

  def commit(self):
    self.connection.commit()
