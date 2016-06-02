#Finding Numbers in a Haystack

#In this assignment you will read through and parse a file with text and numbers. 
#You will extract all the numbers in the file and compute the sum of the numbers.
#Data Format
#The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text. 
#Handling The Data
#The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
import re
name = raw_input("Enter file:")
if len(name) < 1 : name = "regex_sum_212308.txt"
handle = open(name)
sum=0
for line in handle:
    stuff=re.findall('[0-9]+',line) #list of strings
    for str in stuff:
        num=int(str)  
        sum=sum+num
print 'Summ', sum