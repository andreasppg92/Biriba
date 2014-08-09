import tornado.web
import logging
import inspect
import os 


class BaseHandler(tornado.web.RequestHandler):
  def __init__(self, request, kwargs):
    super(BaseHandler, self).__init__(request, kwargs)
    self.tables = self.application.settings["database"].tables
    self.html = None
    self.contract = None

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
    logging.error("Not implemented method authGet")

  def authPost(self, *args, **kwargs):
    logging.error("Not implemented method authPost")

  def render(self, data = {}):
    if self.html == None:
      logging.error("Html path not sepcified")
    if self.contract == None:
      logging.error("Contract not sepcified")
    
    path = "html/" + self.html
    if not os.path.exists(os.path.abspath("Handlers/" + path)):
      logging.error(("Html file not found: " + path))

    for key, valueType in self.contract.iteritems():
      if not key in data:
        logging.error("Missing key: \"" + key + "\"")
      elif type(data[key]) != valueType:
        logging.error("Misstyped data: \"" + key + "\"")

    super(BaseHandler, self).render(path, data = data)