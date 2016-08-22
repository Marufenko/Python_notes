import urllib
from bs4 import BeautifulSoup

html = urllib.urlopen('http://python-data.dr-chuck.net/comments_42.html').read() #open url
soup = BeautifulSoup(html) #read url by BeautifulSoup

count = 0
tags = soup('span') # Retrieve all of the anchor tags
for tag in tags:
    count += int(tag.contents[0]) # count sum of contant of all tags <span>

print count