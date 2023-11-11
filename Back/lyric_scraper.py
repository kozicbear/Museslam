"""
A class that scrapes lyrics from AZ Lyrics
"""

import requests
import re
from bs4 import BeautifulSoup
import string
from collections import defaultdict
import json

sites = [
    'https://www.azlyrics.com/m/muse.html'
]

class LyricScraper():
	def __init__(self):
		"""
		Initializes list to capture lyrics
		"""
		self.lyrics = []

	def scrape_lyrics(self, url=sites[0], link_requirement='https://www.azlyrics.com/m/muse.html'):
		print("Scraping from AZLyrics")
		
		r = requests.get(url)
		soup = BeautifulSoup(r.content, 'html5lib')
		soup_links = soup.find_all('div', attrs={'id': 'listAlbum'})

		for div in soup_links:
			links = div.findAll('a')
			# go into each song
			for a in links:
				# print(a['href'])
				name = str(a)
				name = name.split('>', 1)[1].split('<')[0]
				# print(name)
				# scrape lyrics
				self.scrape_song(a['href'], name)
	
	def scrape_song(self, song_url, song_name):
		r = requests.get("https://www.azlyrics.com", song_url)
		soup = BeautifulSoup(r.content, 'html5lib')
		lyrics = soup.select('div', attrs={'class': 'ringtone'})
		print(lyrics)
        

def main():
	scraper = LyricScraper()

	scraper.scrape_lyrics()

if __name__ == '__main__':
	main()