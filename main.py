import tornado.ioloop
import tornado.web
import settings

settings = {
  "cookie_secret": settings.secret
}
application = tornado.web.Application([
  (r"/", None),
], **settings)

def main():
  application.listen(settings.port)
  tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
  main()
