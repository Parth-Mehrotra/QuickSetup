import webapp2
import datetime
from google.appengine.ext import ndb

class Script(ndb.Model):
	route = ndb.StringProperty(required=True)
	script = ndb.StringProperty(required=True)
	runs = ndb.IntegerProperty(required=True)
	creation_date = ndb.DateProperty(auto_now_add=True)

class Reserve(webapp2.RequestHandler):
	def post(self):
		route = self.request.path
		script = self.request.get("script")
		reservation = Script(route=route, script=script, runs=0)
		reservation.put()

class Retrieve(webapp2.RequestHandler):
	def get(self):
		print self.request.path

app = webapp2.WSGIApplication([
	('/reserve/.*', Reserve),
	('/.*', Retrieve)
], debug=True)
