#COMENT
)#coding: utf8
import urllib2
import re

def get_page(url):
    f = urllib2.urlopen(url)
    return f.read()

def search_tags(page):
    pattern = "<a.*href=.*>.*</a>"
    template = re.compile(pattern)
    lst = template.findall(page)
    return lst
def
    pass