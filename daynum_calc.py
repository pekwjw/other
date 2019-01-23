# -*- coding:utf-8 -*-
# calc days num between start and end.

import time
def daycmp(start,end):
    timedict = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31,'yyyy':365}
    slist = [start[:4]] + [start[4:6]] + [start[6:]]
    elist = [end[:4]] + [end[4:6]] + [end[6:]]
    basestart = [start[:4]] + [01] + [01]
    daydiff1 = 0
    for tmp in xrange(int(basestart[1]),int(slist[1])):
        daydiff1 += timedict[tmp]
    daydiff1 += int(slist[2]) - int(basestart[2])
    if int(slist[0]) % 4 == 0 and int(slist[1]) > 2 :
        daydiff1 += 1

    daydiff2 = 0
    for tmp in xrange(int(basestart[0]),int(elist[0])):
        daydiff2 += timedict['yyyy']
        if tmp%4 == 0:
            daydiff2 += 1
    for tmp in xrange(int(basestart[1]),int(elist[1])):
        daydiff2 += timedict[tmp]
    daydiff2 += int(elist[2]) - int(basestart[2])
    if int(elist[0]) % 4 == 0 and int(elist[1]) > 2 :
        daydiff2 += 1

    return daydiff2 - daydiff1

def daycmp1(start,end):
    daysecond = 24*60*60
    stamp1 = int(time.mktime(time.strptime(start,"%Y%m%d")))
    stamp2 = int(time.mktime(time.strptime(end,"%Y%m%d")))
    daydiff = (stamp2-stamp1)/daysecond
    return daydiff

print daycmp('20030302','20030303')
print daycmp1('20030302','20030303')
