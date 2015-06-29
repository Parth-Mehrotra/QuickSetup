import webapp2
import datetime
from google.appengine.ext import ndb

class Script(ndb.Model):
	route = ndb.StringProperty(required=True)
	script = ndb.StringProperty(required=True)
	runs = ndb.IntegerProperty(required=True)
	creation_date = ndb.DateProperty(auto_now_add=True)

class RetrieveReserve(webapp2.RequestHandler):
	def is_unique(self, route):
		return len(Script.query(Script.route == route).fetch(1)) is 0

	def post(self):
		route = self.request.path
		if self.is_unique(route):
			script = self.request.get("script")
			reservation = Script(route=route, script=script, runs=0)
			reservation.put()
			self.response.status = 202
		else:
			self.response.status = 409

	def get(self):
		scripts = Script.query(Script.route == self.request.path).fetch(1)
		print scripts
		if len(scripts) is not 0:
			scripts[0].runs+=1
			scripts[0].put()
			self.response.out.write(scripts[0].script)
		else:
			self.response.status = 404

app = webapp2.WSGIApplication([
	('/.*', RetrieveReserve)
], debug=True)
