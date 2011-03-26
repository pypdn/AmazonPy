from __future__ import print_function
from lxml import html
from urllib2 import urlopen
##
##url = "http://www.amazon.com/Algorithm-Design-Manual-Steven-Skiena/dp/1849967202/ref=sr_1_1?s=books&ie=UTF8&qid=1294839612&sr=1-1 "
##doc = html.parse(url).getroot()
##print (doc.find_class("parseasinTitle")[0].get_element_by_id("btAsinTitle"))
"""
  -Title
  -Author(s)
  -Price
  -Current Price
  -Avg Review
  -Number of reviews
  -Items the customer also bought (w/ links)
  -Items frequently bought w/book (w/likes)
  -Format
  -Pages
  -Language
  -Publisher
  -Edition
  -Date Published
  -ISBN (10/13)
  -Product Dimensions
  -Shipping weight
  -Subjects

"""
class Parser(object):
    """
    """
    def __init__(self, in_line):
        if in_line.find("http://") == -1:
            f_ile = open(in_line).readlines()
            link = ""
            for line in f_ile:
                link = link + line
        else:
            link = in_line

        self.source = html.parse(link).getroot()

    @property 
    def title(self):
        res = self.source.get_element_by_id("btAsinTitle").text
        return "Title: " + res.strip()

if __name__ == "__main__":
    import doctest
    doctest.testfile("test.txt")

##    
##    
##class Book(object):
##    """
##    spam = Parser("
##    """
##    def __init__(self, data):
##        
##select count(type) from sqlite_master where type='table' and name='TABLE_NAME_TO_CHECK';

