from google.appengine.ext import ndb

class Movie(ndb.Model):
	url = ndb.StringProperty()
	date_tweeted = ndb.DateTimeProperty(auto_now_add=True)