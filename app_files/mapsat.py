#!/usr/bin/python2

import sys
import re

a = 0

for i in sys.stdin :
	j = i.split(',')

	if float(j[0]) < 0.50 :
		print '1'

	elif float(j[0]) >= 0.50 and float(j[0]) < 0.75 :
		print '2'

	elif float(j[0]) >= 0.75 :
		print '3'
