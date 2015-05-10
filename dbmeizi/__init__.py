__author__ = 'Rain'


#!/user/bin/python
#-*-coding:utf-8-*-
#encoding=utf-8

import  urllib2
import urllib
import os
from bs4 import BeautifulSoup

def getAllImageLink():
    html = urllib2.urlopen('http://www.dbmeizi.com').read
    soup = BeautifulSoup(html)
    liResult = soup.findAll('li',attrs={"class":"span3"})
    for li in liResult:
        imageEntityArray = li.findAll('img')

        for image in imageEntityArray:
            link = image.get('data-src')
            imageName = image.get('data-id')
            print imageName
            filesavepath = 'D:\\meizipicture\\%s.jpg' % imageName
            urllib.urlretrieve(link,filesavepath)
            print filesavepath

if __name__ == '__main__':
    getAllImageLink()


