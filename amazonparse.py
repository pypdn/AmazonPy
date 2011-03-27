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
from __future__ import print_function
from lxml import html


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
        return "Title: " + res.strip()

    @property
    def author(self):
        """author may be missing: 9780028631141.html
                    may be multiple:
                    may have dropdown list: """
        res = self.source.get_element_by_id("btAsinTitle").getparent() \
              .getparent()
        res = res.iterlinks()
        res_list = [link[0].text_content() for link in res]
        fmt_res = "Author(s): " + ", ".join(res_list)
        return fmt_res

    @property
    def type_(self):
        """Note that there are two methods for text .text and .text_content
        :( I havent seen any difference between them yet though. Note
        subelement accesss starts from zero"""
        res = self.source.get_element_by_id("btAsinTitle")[0].text_content()
        return res.strip("[]")

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
