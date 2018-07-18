import webapp2
import os
import jinja2

from google.appengine.ext import ndb

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Word(ndb.Model):
    noun1 = ndb.StringProperty(required=True)
    noun2 = ndb.StringProperty(required=True)
    verb1 = ndb.StringProperty(required=True)
    adjective1 = ndb.StringProperty(required=True)

class Home(webapp2.RequestHandler):
    def get(self):
        home = jinja_env.get_template('templates/home.html')
        self.response.write(home.render())

class FillInBlanks(webapp2.RequestHandler):
    def get(self):
        start = jinja_env.get_template('templates/start.html')
        self.response.write(start.render())

    def post(self):
        endpage = jinja_env.get_template('templates/end.html')
        noun1 = self.request.get('noun1')
        noun2 = self.request.get('noun2')
        verb1 = self.request.get('verb1')
        adjective1 = self.request.get('adjective1')
        user_input = {
            'noun1': noun1,
            'noun2': noun2,
            'verb1': verb1,
            'adjective1': adjective1,
        }
        words =  Word(noun1=noun1, noun2=noun2, verb1=verb1, adjective1=adjective1)
        words.put()
        self.response.write(endpage.render(user_input))

class History(webapp2.RequestHandler):
    def get(self):
        list_template = jinja_env.get_template('templates/endcopy.html')
        query = Word.query()
        words = query.fetch()
        story = {
            'story': words
        }
        print(story)
        self.response.write(list_template.render(story))


app = webapp2.WSGIApplication([
    ('/start', FillInBlanks),
    ('/history', History),
    ('/', Home)
])
