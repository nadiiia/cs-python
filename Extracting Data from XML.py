#The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
#You are to look through all the <comment> tags and find the <count> values sum the numbers.
#Sample Execution


#Enter location: http://python-data.dr-chuck.net/comments_42.xml
#Retrieving http://python-data.dr-chuck.net/comments_42.xml
#Retrieved 4204 characters
#Count: 50
#Sum: 2482

import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_212310.xml'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    #url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
   
    tree = ET.fromstring(data)
    cnt = 0
    sum=0
    counts = tree.findall('.//count')
    for count in counts:
        count_int = int(count.text)
        cnt = cnt+1
        sum = sum+count_int

    print "Count", cnt
    print 'Sum', sum
