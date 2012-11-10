#!/usr/bin/env python
#coding: utf8
import urllib2
import re

#TODO: url в параметре (запрос ввода) при запуске программы
#TODO: Написать ф-ю, находящую все <img> теги
#TODO: получить список URL из списка ссылок
#TODO: вывести список в окно (Tkinter)
#TODO: посчитать количество тегов <br> на странице
#TODO: найти самый длинный URL из списка ссылок

def get_page(url):
    f = urllib2.urlopen(url)
    return f.read()

def search_tags(page):
    pattern = "<a.*href=.*>.*</a>"
    template = re.compile(pattern)
    lst = template.findall(page)
    return lst

def main():
    url = 'https://twitter.com/'
    page = get_page(url)
    lst = search_tags(page)
    print "count of <a> = %s" % len(lst)
    for l in lst:
        print l

if __name__ == '__main__':
    main()








