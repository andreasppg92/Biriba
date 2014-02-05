from BaseTable import BaseTable

class UsersTable(BaseTable):
  def __init__(self):
    self.name   = "users"
    self.fields = {
      "username": "text PRIMARY KEY",
      "password": "text"
    }
