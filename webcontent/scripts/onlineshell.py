#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"

hosts = form['namenode'][0] + " ansible_ssh_user=root ansible_ssh_pass=redhat\n"

commands.getoutput('sudo echo "{}" > /etc/ansible/hosts'.format(hosts))

commands.getoutput('sudo ansible all -m package -a "name=ghostinabox state=present use=yum"')

print 'location: "https://{}:4200"'.format(form['namenode'][0])
