#!/usr/bin/python

import commands
import cgi

print "Content-Type: text/html"
print

form = cgi.FormContent()

ip = form['ipWebServer'][0]
password = form['passwdWebServer'][0]

try :
    port = form['portNumber'][0]
except:
    port = ''

try :
    path = form['rootPath'][0]
except:
    path = ''

hoststr = "{} ansible_ssh_user=root ansible_ssh_pass={}".format(ip,password)

commands.getoutput('sudo echo "{}" > /etc/ansible/hosts')

commands.getstatusoutput("sudo ansible-playbook ansible/webserver.yml")

if port != '' :
    command.getstatusoutput('sudo echo "Listen {}\n"'.format(port) > /root/app_files/myapp.conf)

if path != '' :
    command.getstatusoutput('sudo echo "Documentroot {}\n<Directory>\ngrant all \n</Directory>\n"'.format(port) >> /root/app_files/myapp.conf)

if port !='' and path !='' :
    commands.getstatusoutput("sudo ansible-playbook ansible/transferconf.yml")
