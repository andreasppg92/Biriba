import tornado.ioloop
import tornado.web
import optparse
import logging
import os

from Handlers.LoginHandler import LoginHandler
from Handlers.IndexHandler import IndexHandler
from Handlers.PlayHandler import PlayHandler
from Database.Database import Database

SETTINGS = {
  "secret": "17l/pdU2SAeJWx61w3TGPwQ1tI2hPUVGgUfmqxKHKWY",
  "login": "/login",
  "port": 8000,
  "static": "./Static"
}

# Options parser
parser = optparse.OptionParser()
parser.add_option("-d", "--debug", action="store_true", dest="debug", 
  help="Enable debug mode")
parser.add_option("-D", "--drop", action="store_true", dest="drop", 
  help="Drop tables")
parser.add_option("-A", "--admin", action="store_true", dest="admin", 
  help="Create admin user")
(options, args) = parser.parse_args()

# Database
database = Database()

# Tornado application
application = tornado.web.Application([
  (r"/login", LoginHandler),
  (r"/play", PlayHandler),
  (r"/", IndexHandler)
], **{
  "cookie_secret": SETTINGS["secret"],
  "static_path"  : SETTINGS["static"],
  "database"     : database
})

def main():
  # Set logging
  logging.basicConfig(
    format = "%(asctime)-15s %(filename)s:%(lineno)d %(levelname)s: %(message)s",
    level = logging.DEBUG if options.debug else logging.INFO
  )

  # Connect and initialize database
  database.connect()
  if options.drop:
    database.dropTables()
  database.initialize()

  #Add admin user if needed
  if options.admin and not database.tables["users"].usernameExists("admin"):
    database.tables["users"].addUser("admin", "123")
    logging.info("Admin user created")
    
  # Start the server
  application.listen(SETTINGS["port"])
  logging.info("Application listening on port " + str(SETTINGS["port"]))
  tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
  main()
