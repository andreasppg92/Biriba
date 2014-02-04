import tornado.ioloop
import tornado.web
import settings
import os.path

from Handlers.LoginHandler import LoginHandler

application = tornado.web.Application([
  (r"/login", LoginHandler),
], **{
  "cookie_secret": settings.secret,
  "static_path"  : settings.static,
  "xsrf_cookies" : settings.xsrf,
})

def main():
  application.listen(settings.port)
  tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
  main()
