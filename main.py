import tornado.ioloop
import tornado.web
import optparse
import settings
import logging

from Handlers.LoginHandler import LoginHandler
from Database.Database import Database

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
], **{
  "cookie_secret": settings.secret,
  "static_path"  : settings.static,
  "database"     : database
})

def main():
  # Set logging
  logging.basicConfig(
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    level=logging.DEBUG if options.debug else logging.INFO
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
  application.listen(settings.port)
  logging.info("Application listening on port " + str(settings.port))
  tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
  main()
