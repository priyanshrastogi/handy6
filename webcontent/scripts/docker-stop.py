#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"

cname = cgi.FormContent()['cname'][0]

status = commands.getstatusoutput("sudo docker stop {}".format(cname))

if status[0] == 0 :
    print "location: docker.py"
    print

else :
    print
    print "Cannot Stop Container"
