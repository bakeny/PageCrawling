__author__ = 'Rain'


#!/user/bin/python
# -*-coding:utf-8-*-
#encoding=utf-8

import urllib2
import urllib
import os
import bs4
from bs4 import BeautifulSoup


def getAllImageLink():
    # if(pagesize == 0):
    #     print "Size of Need downloaded picture page is zero!"
    #     return
    # for i in range(pagesize):
        html = urllib2.urlopen('http://www.dbmeizi.com')

        print html
        soup = BeautifulSoup(html)
        liResult = soup.findAll('li', attrs={"class": "span3"})
        for li in liResult:
            imageEntityArray = li.findAll('img')

            for image in imageEntityArray:
                link = image.get('data-bigimg')
                imageName = image.get('data-id')
                print imageName
                filesavepath = 'D:\\meizipicture\\%s.jpg' % imageName
                urllib.urlretrieve(link, filesavepath)
                print filesavepath


if __name__ == '__main__':
    getAllImageLink()


