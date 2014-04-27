import logging

from Handlers.BaseHandler import BaseHandler

class LoginHandler(BaseHandler):
  def get(self):
    if self.loggedIn():
      self.redirect("/")
    else:
      data = {"failed": False}
      self.render("../Templates/login.html", data=data)

  def post(self):
    users = self.tables["users"]

    if self.loggedIn():
      self.redirect("/")
      return

    try:
      username = self.get_argument("user")
      password = self.get_argument("pass")
      remember = self.get_argument("remember")
    except Exception as e:
      remember = False
    
    if users.authenticate(username, password):
      if remember:
        self.set_secure_cookie("user", username)
      else:
        self.set_secure_cookie("user", username, expires_days=None)
      self.redirect("/")
    else:
      data = {"failed": True}
      self.render("../Templates/login.html", data=data)