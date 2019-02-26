#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#	 http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import wikipedia
import twitter
import models
import logging

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Plotbot!')

class Tweet(webapp2.RequestHandler):
	def get(self):
		page = self.request.get('page')
		valid_movie = False
		if page:
			url = 'https://en.wikipedia.org/wiki/' + page
			movie = wikipedia.get_movie_page(url)
		
		else:		
			while valid_movie == False:
				url = 'https://en.wikipedia.org' + wikipedia.pick_movie()
				q = models.Movie.query(models.Movie.url == url)
				if q.count() > 0:
					continue
				
				movie = wikipedia.get_movie_page(url)
				if movie is not None:
					valid_movie = True

		tweets = twitter.construct(movie)
		
		m = models.Movie(url = url)
		m.put()
		last_id = None
		for i in tweets:
			t = twitter.send_tweet(i, in_reply_to=last_id)
			last_id = t.id
			self.response.write(i + '\n')
	

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/admin/tweet', Tweet)
], debug=True)
