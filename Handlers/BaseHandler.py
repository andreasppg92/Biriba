import tornado.web

class BaseHandler(tornado.web.RequestHandler):
  def __init__(self, request, kwargs):
    super(BaseHandler, self).__init__(request, kwargs)
    self.tables = self.application.settings["database"].tables

  def authenticate(self, success, *args, **kwargs):
    if self.get_secure_cookie("user") == None:
      self.redirect("/login")
    else:
      success(*args, **kwargs)

  def get(self, *args, **kwargs):
    self.authenticate(self.authGet, *args, **kwargs)

  def post(self, *args, **kwargs):
    self.authenticate(self.authPost, *args, **kwargs)

  def authGet(self, *args, **kwargs):
    raise "Not implemented method authGet"

  def authPost(self, *args, **kwargs):
    raise "Not implemented method authPost"
