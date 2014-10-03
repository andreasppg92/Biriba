import logging

from BaseHandler import BaseHandler

class PlayHandler(BaseHandler):
    def __init__(self, request, kwargs):
        super(PlayHandler, self).__init__(request, kwargs)
        self.html = "play.html"
        self.contract = {}


    def authGet(self, *args, **kwargs):
        try:
            command = self.get_argument("command")
            if command == "getPlayersHand":
                hand = self.controller.getCurrentPlayersHand()
                self.write(str(hand))
        except Exception as e:
            self.controller.startGame()
            self.render()