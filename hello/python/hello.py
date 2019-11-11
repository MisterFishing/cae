import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("<h1 style='text-align: center;'>Hello Python</h1><p style='text-align: center;'>Welcom to Cloud APP World!</p>")

app = webapp2.WSGIApplication([('/', MainPage),], debug=True)
