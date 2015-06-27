import webapp2

class Reserve(webapp2.RequestHandler):
    def post(self):
        print self.request.path

app = webapp2.WSGIApplication([
    ('/.*', Reserve),
], debug=True)
