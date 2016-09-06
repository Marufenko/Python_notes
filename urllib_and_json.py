import json
import urllib

# set url for analysis
url = raw_input('Enter location: ')
if len(url)<1: url = "http://python-data.dr-chuck.net/comments_42.json"
print 'Retrieving ', url
# open url
handler = urllib.urlopen(url).read()

# count cherectes in uploaded json
print 'Retrieved ', len(handler), ' characters'

# pars json data from url
info = json.loads(handler)

# count
count_num = 0
sum_num = 0
for item in info["comments"]:
    count_num += 1
    sum_num += item["count"]
print 'Count: ', count_num
print 'Sum: ', sum_num
