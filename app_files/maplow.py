#!/usr/bin/python2

import sys
import re

for i in sys.stdin :
	j = i.split(',')
	if j[6]=='1' and str.find(j[9],'low') != -1 :
		print i,
