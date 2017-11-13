#!/usr/bin/python2

import sys
import re

x = 0
y = 0
z = 0
for i in sys.stdin :
    if str.find(i,'1')!=-1 :
        x = x+1

    elif str.find(i,'2')!=-1 :
        y = y+1

    elif str.find(i,'3')!=-1 :
        z = z+1
print x
print y
print z
