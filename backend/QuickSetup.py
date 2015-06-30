import webapp2
import datetime
import json
from google.appengine.ext import ndb

#TODO We should keep track of the amount of time since the last run from the same IP so people can't force their scripts to the top of the leader board simply by getting a bunch of times
class Script(ndb.Model):
	route = ndb.StringProperty(required=True)
	script = ndb.StringProperty(required=True)
	runs = ndb.IntegerProperty(required=True)
	creation_date = ndb.DateProperty(auto_now_add=True)

class Explore(webapp2.RequestHandler):
	def post(self):
		self.response.headers['Content-Type'] = 'application/json'   
		scripts = Script.query(Script.runs >= 1).order(-Script.runs).fetch()
		routeRuns = []
		for script in scripts: 
			routeRuns.append({"route": script.route, "runs":script.runs})

		self.response.out.write(json.dumps(routeRuns))


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
	('/explore', Explore),
	('/.*', RetrieveReserve)
], debug=True)
