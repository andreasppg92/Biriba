import tornado.web

class BaseHandler(tornado.web.RequestHandler):
  def __init__(self, request, kwargs):
    super(BaseHandler, self).__init__(request, kwargs)
    self.tables = self.application.settings["database"].tables

  def loggedIn(self):
    return not self.get_secure_cookie("user") is None

  def authenticate(self, success, *args, **kwargs):
    if self.loggedIn():
      success(*args, **kwargs)
    else:
      self.redirect("/login")

  def get(self, *args, **kwargs):
    self.authenticate(self.authGet, *args, **kwargs)

  def post(self, *args, **kwargs):
    self.authenticate(self.authPost, *args, **kwargs)

  def authGet(self, *args, **kwargs):
    raise "Not implemented method authGet"

  def authPost(self, *args, **kwargs):
    raise "Not implemented method authPost"
