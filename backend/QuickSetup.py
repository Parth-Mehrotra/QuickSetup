import webapp2
import datetime
from google.appengine.ext import db

class Script(db.Model):
	route = db.StringProperty(required=True)
	script = db.StringProperty(required=True)
	runs = db.IntegerProperty(required=True)
	creation_date = db.DateProperty(required=True)

class Reserve(webapp2.RequestHandler):
	def post(self):
		print self.request.path
		print self.request.get("script")

app = webapp2.WSGIApplication([
	('/.*', Reserve),
], debug=True)
