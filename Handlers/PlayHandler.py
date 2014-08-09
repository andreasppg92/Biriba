import logging

from Handlers.BaseHandler import BaseHandler

class PlayHandler(BaseHandler):
  def __init__(self, request, kwargs):
    super(PlayHandler, self).__init__(request, kwargs)
    self.html = "play.html"
    self.contract = {}

  def authGet(self):
    self.render()