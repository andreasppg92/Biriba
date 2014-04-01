from Handlers.BaseHandler import BaseHandler

class LoginHandler(BaseHandler):
  def get(self):
  	data = {"failed": False}
	self.render("../Templates/login.html", data=data)

  def post(self):
  	users = self.tables["users"]
  	args = self.get_argumentes()

  	if users.authenticate(args["user"], args["pass"]):
  		if args["remember"]:
  			self.set_secure_cookie("user", args["user"])
  		else:
  			self.set_secure_cookie("user", args["user"], expires_days=None)
  		self.redirect("/")
  	else:
  		data = {"failed": True}
  		self.render("../Templates/login.html", data=data)