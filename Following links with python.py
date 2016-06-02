#Following Links in Python

#In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py.
#The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
import urllib
from BeautifulSoup import *
url = raw_input('Enter - ')
position=int(raw_input('Enter Position'))
count=int(raw_input('Enter Count'))

#
#times the process is repeated
tpr = 4

# url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Madilyn.html'
for i in range(tpr):
    url = BeautifulSoup(urllib.request.urlopen(url).read())('a')[lp - 1].get('href', None)
    print(url)