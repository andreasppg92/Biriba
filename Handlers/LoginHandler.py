from Handlers.BaseHandler import BaseHandler

class LoginHandler(BaseHandler):
  def get(self):
    self.render("../Templates/login.html")

  def post(self):
    pass
