import webapp2

class Reserve(webapp2.RequestHandler):
    def get(self):
        print self.request.path

app = webapp2.WSGIApplication([
    ('/.*', Reserve),
], debug=True)
