from BaseTable import BaseTable

import hashlib

class UsersTable(BaseTable):
  def __init__(self):
    super(UsersTable, self).__init__()
    self.name   = "users"
    self.fields = {
      "username": "text PRIMARY KEY",
      "email": "text",
      "password": "text"
    }

  def addUser(self, username, password):
    password = hashlib.sha512(password).hexdigest
    command = "INSERT INTO " + self.name + "VALUES (%s, %s)"
    self.cursor.execute(command, (username, password))
    self.cursor.connection.commit()

  def usernameExists(self, username):
    command = "SELECT * FROM " + self.name + " WHERE username=%s"
    self.cursor.execute(command, (username,))
    return self.cursor.rowcount != 0

  def emailExists(self, email):
    command = "SELECT * FROM " + self.name + " WHERE email=%s"
    self.cursor.execute(command, (email,))
    return self.cursor.rowcount != 0

  def authenticate(self, username, password):
    password = hashlib.sha512(password).hexdigest
    command = "SELECT * FROM " + self.name + \
              " WHERE username=%s AND password=%s"
    self.cursor.execute(command, (username, password))
    return self.cursor.rowcount == 1