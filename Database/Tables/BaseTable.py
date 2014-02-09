import logging

class BaseTable(object):
  def __init__(self):
    self.name = None
    self.fields = None

  def create(self):
    command = "CREATE TABLE " + self.name
    fields = []
    for field, details in self.fields.iteritems():
      fields.append(field + " " + details)
    return command + " (" + ", ".join(fields) + ")"

  def drop(self):
    return "DROP TABLE" + self.name
