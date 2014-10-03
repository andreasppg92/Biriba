import logging

from BaseHandler import BaseHandler

class LoginHandler(BaseHandler):
  def __init__(self, request, kwargs):
    super(LoginHandler, self).__init__(request, kwargs)
    self.html = "login.html"
    self.contract = {"failed": bool}


  def get(self):
    if self.loggedIn():
      self.redirect("/")
    else:
      data = {"failed": False}
      self.render(data)

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
    
    if not users.authenticate(username, password):
      data = {"failed": True}
      self.render("../Templates/login.html", data=data)
    else:
      if remember:
        self.set_secure_cookie("user", username)
      else:
        self.set_secure_cookie("user", username, expires_days=None)
      self.redirect("/")
