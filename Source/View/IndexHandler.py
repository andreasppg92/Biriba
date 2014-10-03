import logging

from BaseHandler import BaseHandler

class IndexHandler(BaseHandler):
  def __init__(self, request, kwargs):
    super(IndexHandler, self).__init__(request, kwargs)
    self.html = "index.html"
    self.contract = {}

  def authGet(self):
    self.render()
