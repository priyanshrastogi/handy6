#!/usr/bin/python

import cgi

print "Content-Type: text/html"

form = cgi.FormContent()

username = form['username'][0]
password = form['password'][0]

cUser = "admin"
cPass = "pass"

if username==cUser and password==cPass :
    #print "User Authenticated"
    print "location: ../dashboard.html"
    print

else :
    print "location: ../index.html"
    print
