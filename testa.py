from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import time
from wxpy import *

bot = Bot(cache_path='./test.pkl')

#测试用,之后改
my_mps = bot.mps().search('T00ls')[0]
print(my_mps)
my_friend = bot.friends().search('Dave')[0]
test_console = bot.groups().search('test')[0]
print(my_friend)
tickets = 0
mon = 10
url = 'http://www.shoac.com.cn/Calendar.aspx?year=2017&month='+str(mon)


def sleep_time(hour,min,sec):
    return hour*3600+min*60+sec

seconds = 30
interval = sleep_time(0,0,seconds)
time_passed = 0

def requesturl(urls):
    time.sleep(interval)
    response = urlopen(urls)
    size_of_page = len(response.read())
    global time_passed
    time_passed += seconds
    test_console.send(time_passed)
    if size_of_page == 56859:
	    my_friend.send(url)
		
def Tls(time):
    print(time)
    if time%86400 == 0:
        print('it work')
        my_mps.send('3')
        my_mps.send('4')
    
try:
    while 1 == 1:
        requesturl(url)
        Tls(time_passed)
    
except:
    my_friend.send('an error occur')
    requesturl(url)
