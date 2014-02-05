class BaseTable(object):
  def __init__(self):
    self.name = None
    self.fields = None
    self.cursor = None

  def execute(self, command):
    try:
      self.cursor.execute(command + ";")
    except:
      print "ERROR executing command:\n" + command

  def initialize(self, cursor):
    if self.name is None or self.fields is None:
      raise "Name or fields not set"
    else:
      self.cursor = cursor
      command = "CREATE TABLE " + self.name
      fields = []
      for field, details in self.fields.iteritems():
        fields.append(field + " " + details)
      fields = ", ".join(fields)
      self.execute(command + " (" + fields + ")")
   

