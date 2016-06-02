#The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

import json, urllib


url = raw_input('Enter - ')
url = "http://python-data.dr-chuck.net/comments_42.json"
print "Retrieving: ", url

response = urllib.urlopen(url)
info = json.loads(response.read())
json_obj= json.dumps(info)
print 'Retrieved:', len(json_obj), "characters"

count = 0
sum = 0
for item in info['comments']:
    count = count +1
    sum = sum+item['count']
    #sum = info['comments'][1]['count']
print "Count: ", count
print "Sum: ", sum