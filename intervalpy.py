import time

def sleep_time(hour,min,sec):
    return hour*3600+min*60+sec

interval = sleep_time(0,0,10)

while 1==1:
    time.sleep(interval)
    print 'test'
