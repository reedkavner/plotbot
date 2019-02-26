from bs4 import BeautifulSoup
import requests
import re
import random
from datetime import datetime
from requests_toolbelt.adapters import appengine
import logging

appengine.monkeypatch()

def get_movie_page(url):
	logging.debug("Getting %s" % url)
	r = requests.get(url)
	soup = BeautifulSoup(r.content, 'html.parser')
	page_title = soup.find("h1", {"id": "firstHeading"}).text
	plot = []
	el = soup.find("span", {"id": "Plot"})
	#if there is no plot section, return None
	if el == None:
		return None
	el = el.parent
	# grab all the 'p' elements until we hit an 'h2'
	while True:
		el = el.nextSibling
		if el.name == 'h2':
			break
		elif el.name == 'p':
			plot.append(el)

	link_titles = []
	for i in plot:
		# first remove text in parentheses, likely actor names
		i = re.sub(r'\([^)]*\)', '', str(i))
		#then convert it back into a BS object
		i = BeautifulSoup(i, 'html.parser')
		links = i.findAll('a')
		for l in links:
			try:
				link_titles.append(l['title'].lstrip('wikt:'))
			except:
				logging.debug("No link title")

	if len(link_titles) == 0:
		return None
	return {
		'page_title' : page_title,
		'link_titles' :link_titles
	}

def pick_movie():
	this_year = datetime.today().year
	rand_year = random.randint(1980, this_year)
	url = "https://en.wikipedia.org/wiki/List_of_American_films_of_%i" % rand_year
	r = requests.get(url)
	soup = BeautifulSoup(r.content, 'html.parser')
	tables = soup.findAll('table', {'class': 'wikitable'})

	#pick a table
	rand_table = random.randint(0, len(tables) - 1)
	table = tables[rand_table]
	
	#pick a movie
	movies = table.findAll("i")

	valid = False
	while valid == False:
		rand_movie = random.randint(0, len(movies) - 1)
		movie = movies[rand_movie]
		try:
			url = movie.findAll('a')[0]['href']
		except:
			logging.debug("No movie link")
			pass
		valid = True

	return url

if __name__ == '__main__':
	pick_movie()







