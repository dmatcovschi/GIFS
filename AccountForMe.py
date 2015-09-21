import requests
from bs4 import BeautifulSoup
import urllib.request

Links = []

for page in range(1,5):
	
	r = requests.get("http://howshouldweaccountforme.tumblr.com/page/" + str(page))
	soup = BeautifulSoup(r.content)
	gifLinks = soup.find_all("div", {"class" : "cont group"})
	for Link in gifLinks:
		Links.append(Link.img.get('src'))

gifCounter = 1
for link in Links:
	urllib.request.urlretrieve(Link.img.get('src'), "gifs/" + str(gifCounter) + ".gif")
	gifCounter += 1
	print(gifCounter + " " + link)