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
    >>> test = Parser(r"http://www.amazon.com/Algorithm-Design-Manual-Steven-
    Skiena/dp/1849967202/ref=sr_1_1?s=books&ie=UTF8&qid=1294839612&sr=1-1")
    >>> test.title
    Title: The Algorithm Design Manual
    >>> test.getAuthor()
    Authors: Steven S. Skiena
    >>> test.getListPrice()
    List Price: $87.00
    >>> test.getCrrntPrice()
    Current Price: $71.97
    >>> test.getACReview()
    Average Customer Review: 4.5
    >>> test.getNumReviews()
    Number of Reviews: 40
    >>> test.getCABought()
    Customers Also Bought:
    >>> test.getNumLinks()
    Number of Links: 6
    http://www.amazon.com/Cracking-Coding-Interview-Fourth-Programming/dp/145157827X/ref=pd_sim_b_1,
    http://www.amazon.com/Programming-Pearls-2nd-Jon-Bentley/dp/0201657880/ref=pd_sim_b_2,
    http://www.amazon.com/Introduction-Algorithms-Third-Thomas-Cormen/dp/0262033844/ref=pd_sim_b_3,
    http://www.amazon.com/Concrete-Mathematics-Foundation-Computer-Science/dp/0201558025/ref=pd_sim_b_4,
    http://www.amazon.com/Algorithms-Interviews-Adnan-Aziz/dp/1453792996/ref=pd_sim_b_5,
    http://www.amazon.com/Hackers-Delight-Henry-S-Warren/dp/0201914654/ref=pd_sim_b_6
    >>> test.getFBT()
    Frequently Bought Together:
    Number of Links: 2
    http://www.amazon.com/Cracking-Coding-Interview-Fourth-Programming/dp/145157827X/ref=pd_bxgy_b_img_b,
    http://www.amazon.com/Programming-Pearls-2nd-Jon-Bentley/dp/0201657880/ref=pd_bxgy_b_img_c
    >>> test.getType()
    Type: Paperback
    >>> test.getPages()
    Pages: 736
    >>> test.getLanguage()
    Language: English
    >>> test.getPublisher()
    Publisher: Springer
    >>> test.getEdition()
    Edition: 2nd
    >>> test.getDate()
    Date Published: 11/5/2010
    >>> test.getISBN10()
    ISBN-10: 1849967202
    >>> test.getISBN13()
    ISBN-13: 978-1849967204
    >>> test.getDims()
    Product Dimensions: 9.1 x 7 x 1.9 inches
    >>> test.SWeight()
    Shipping Weight: 3.1 pounds
    >>> test.getSubject()
    Subjects: Mathematics, Algorithms & data structures, Combinatorics & graph theory, Mathematical theory of computation, Numerical analysis, Computers - General Information, Computer Science, Computers / Computer Science, Computers / Programming / General, Discrete Mathematics, Mathematics / Applied, Mathematics / Combinatorics, Mathematics / Discrete Mathematics, Programming - General 
    """
    def __init__(self, in_line):
        if in_line.find("http://") == -1:
            f_ile = open(in_line).readlines()
            link = ""
            for line in f_ile:
                link = link + line
        else:
            link = urlopen(in_line).read()

        self.source = html.parse(url).getroot()

    @property 
    def title():
        return source.get_element_by_id("btAsinTitle").tail()

if __name__ == "__main__":
    import doctest
    doctest.testmod()

##    
##    
##class Book(object):
##    """
##    spam = Parser("
##    """
##    def __init__(self, data):
##        
##select count(type) from sqlite_master where type='table' and name='TABLE_NAME_TO_CHECK';

