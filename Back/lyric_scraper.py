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

songs_to_scrape = [
	"Sunburn",
	"Falling Down", 
	"Unintended", 
	"New Born", 
	"Plug In Baby", 
	"Time Is Running Out", 
	"Sing For Absolution", 
	"Hysteria", 
	"Starlight", 
	"Knights Of Cydonia", 
	"Uprising", 
	"Resistance", 
	"Madness", 
	"Animals", 
	"Pressure", 
]

class LyricScraper():
	def __init__(self):
		"""
		Initializes list to capture lyrics
		"""
		self.lyrics = []

	def scrape_lyrics(self, url=sites[0], songs_to_scrape=songs_to_scrape):
		"""
			Method to scrape lyrics from AZLyrics Muse songs. WARNING: It will get your IP access
			denied from accessing AZLyrics for scraping however not before obtaining enough lyrics
			for a small insprining set that I am using.
		"""
		print("Scraping from AZLyrics")
		
		r = requests.get(url)
		soup = BeautifulSoup(r.content, 'html5lib')
		soup_links = soup.find_all('div', attrs={'id': 'listAlbum'})
		lyrics = []
		for div in soup_links:
			links = div.findAll('a')
			# go into each song
			for a in links:
				name = str(a)
				name = name.split('>', 1)[1].split('<')[0]
				# scrape lyrics
				if name in songs_to_scrape:
					print("song: ", name)
					try:
						song_lyrics = self.scrape_song(a['href'], name)
						lyrics.append(song_lyrics)
						f = open("lyrics.txt", "a")
						for line in song_lyrics:
							f.write(line + "\n")
						f.close()
					except:
						print("Error: scraping likely prevented")
						return 0
		print("Scraping complete")
		return 1
	
	def scrape_song(self, song_url, song_name):
		print("Scraping ", song_name)
		r = requests.get("https://www.azlyrics.com" + song_url)
		soup = BeautifulSoup(r.content, 'html5lib')
		lyrics = ""
		for br in soup.findAll('br'):  
			possible_lyric = br.nextSibling  
			if possible_lyric:    
				for i in possible_lyric.text:
					lyrics += i
		result = lyrics.split("\n")[1:]
		while("" in result):
			result.remove("")
		print("Scraped ", song_name)
		return result

def main():
	scraper = LyricScraper()
	scraper.scrape_lyrics()

if __name__ == '__main__':
	main()