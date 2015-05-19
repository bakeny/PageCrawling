__author__ = 'Rain'


#!/user/bin/python
# -*-coding:utf-8-*-
#encoding=utf-8

import urllib2
import urllib
from bs4 import BeautifulSoup


def getAllImageLink(pagesize):
    if(pagesize == 0):
        print "Size of Need downloaded picture page is zero!"
        return
    for i in range(pagesize):
        #网址请求的异常处理
        req = urllib2.Request('http://www.dbmeizi.com/?p='+str(i))
        try:
            urllib2.urlopen(req)
        except urllib2.URLError, e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason
        else:
            print "OK"

        html = urllib2.urlopen(req);
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
    getAllImageLink(3)


