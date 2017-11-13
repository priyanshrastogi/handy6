#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"

cname = cgi.FormContent()['cname'][0]
iname = cgi.FormContent()['iname'][0]

#Run Docker Container
status = commands.getstatusoutput("sudo docker run -dit --name {} {}".format(cname,iname))

if status[0] == 0 :
    print "location: docker.py"
    print

else :
    print
    print "Cannot Run Container"
