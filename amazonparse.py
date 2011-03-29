"""
    Amazon Parser
    Troy Rosenberg and Nkemdirim Dockery
    CIS4930

    -Title
    -Author(s)
    -Price
    -Current Price
    -Avg Review
    -Number of reviews
    -Items the customer also bought (w/ links)
    -Format
    -Publisher
"""
from __future__ import print_function
from lxml import html
import re


class Parser(object):
    """This class represents the entire parsing functionality. The steps of
    the process are broken down into properties for modularity and
    easier access.
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
        """possible design refinement: break down node accesses by larger
            groups. author, format and title etc. are children of the same
            parent"""
        res = self.source.get_element_by_id("btAsinTitle").text
        return res.strip()

    @property
    def author(self):
        """author may be missing: 9780028631141.html
                    may be multiple:
                    may have dropdown list: """
        res = self.source.get_element_by_id("btAsinTitle").getparent() \
              .getparent()
        res = res.iterlinks()
        res_list = [link[0].text for link in res]
        fmt_res = ", ".join(res_list)
        return fmt_res

    @property
    def type_(self):
        """Note that there are two methods for text .text and .text_content
        :( I havent seen any difference between them yet though. Note
        subelement accesss starts from zero"""
        res = self.source.get_element_by_id("btAsinTitle")[0].text_content()
        return res.strip("[]")

    def getPrices(self):
        """"""
        res = self.source.get_element_by_id("priceBlock") \
              .xpath(".//tr")

        price_list = []
        for row in res:
            if len(row) == 2:
                price_list.append(row.text_content().strip().split(":"))

        price_list = [i.strip().partition("\n")[0] for elem in price_list for i in elem]

        
        def pair(test):
            if test:
                yield (test.pop(), test.pop())

        price_list.reverse()
        res = [tup for tup in pair(price_list)]
        return res

    @property
    def listPrice(self):
        res = self.getPrices()
        if self.type_ == "Kindle":
            label = "Digital List Price"
        else:
            label = "List Price"
            
        for elem in res:
            if elem[0].find(label) != -1:
                return elem[1].replace("$", "")
    @property
    def crrntPrice(self):
        res = self.getPrices()
        if self.type_ == "Kindle":
            label = "Kindle Price"
        else:
            label = "Price"
            
        for elem in res:
            if elem[0].find(label) != -1:
                return elem[1].replace("$", "")

    @property
    def numReviews(self):
        res = self.source.find_class("crAvgStars")
        for elem in res:
            check = re.search(r'(?P<reviews>\d+) customer reviews',
                              elem.text_content())
            if check:
                return str(check.group('reviews'))

        return None
    
    @property
    def avgReview(self):
        res = self.source.find_class("crAvgStars")
        for elem in res:
            check = re.search(r'(?P<avg>\d.\d) out of 5',
                              elem.text_content())
            if check:
                return str(check.group('avg'))

        return None

    @property
    def alsoBought(self):
        res = self.source.get_element_by_id("purchaseButtonWrapper") \
            .xpath(".//ul")
        links = res[0].iterlinks()
        res = [elem[2] for elem in links
               if elem[0].get("title") != None]
        return " \n ".join(res)

if __name__ == "__main__":
    import doctest
    doctest.testfile("test.txt")

##url = "http://www.amazon.com/Algorithm-Design-Manual-Steven-Skiena/dp/
##1849967202/ref=sr_1_1?s=books&ie=UTF8&qid=1294839612&sr=1-1 "
##doc = html.parse(url).getroot()
##print (doc.find_class("parseasinTitle")[0].get_element_by_id("btAsinTitle"))

##class Book(object):
##    """
##    spam = Parser("
##    """
##    def __init__(self, data):
##
##select count(type) from sqlite_master where type='table' and
##    name='TABLE_NAME_TO_CHECK';
