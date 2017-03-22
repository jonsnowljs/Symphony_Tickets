# -*- coding:utf-8 -*-
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import time
from wxpy import *

bot = Bot(cache_path='./test.pkl')

#测试用,之后改

my_friend = bot.groups().search('test')[0]
tickets = 0
mon = 10
url = 'http://www.shoac.com.cn/Calendar.aspx?year=2017&month='+str(mon)


def sleep_time(hour,min,sec):
    return hour*3600+min*60+sec
seconds = 10
interval = sleep_time(0,0,seconds)
   
def requesturl(urls):
    time.sleep(interval)
    response = urlopen(urls)
    size_of_page = len(response.read())
    if size_of_page == 56859:
        global tickets
        tickets = 1
        print ('test')
        my_friend.send(url)
try:
    while 1 == 1:
        requesturl(url)
except:
    requesturl(url)
