import tornado.web

class BaseHandler(tornado.web.RequestHandler):
  def initialize(self):
    pass

  def authenticate(self, success, *args, **kwargs):
    if self.get_secure_cookie("name") == None:
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
