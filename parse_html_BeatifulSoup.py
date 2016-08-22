import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')

html = urllib.urlopen(url).read() #open url
soup = BeautifulSoup(html) #read url by BeautifulSoup

count = 0
sum = 0
tags = soup('span') # Retrieve all of the anchor tags
for tag in tags:
    count += 1
    sum += int(tag.contents[0]) # count sum of contant of all tags <span>

print 'Count ' + str(count)
print 'Sum ' + str(sum)
