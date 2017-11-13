#!/usr/bin/python

import commands
import cgi

print "Content-Type: text/html"
print

form = cgi.FormContent()

num = len(form)-3

hosts = ''

hosts = "[namenode]\n"

hosts = hosts + form['namenode'][0] + " ansible_ssh_user=root ansible_ssh_pass=redhat\n"

hosts = hosts + "\n[jobtracker]\n" + form['jobtracker'][0] + " ansible_ssh_user=root ansible_ssh_pass=redhat\n"

hosts = hosts + "\n[client]\n" + form['client'][0] + " ansible_ssh_user=root ansible_ssh_pass=redhat\n"

hosts = hosts + "\n[datanode]\n"

for i in range(0,num) :
    hosts = hosts + form['datanode{}'.format(str(i+1))][0] + " ansible_ssh_user=root ansible_ssh_pass=redhat\n"

commands.getoutput('sudo echo "{}" > /etc/ansible/hosts'.format(hosts))

print commands.getstatusoutput('sudo ansible-playbook ansible/installhadoop.yml')

#Set Hostnames in all systems
print commands.getstatusoutput('sudo ansible namenode -a "hostnamectl set-hostname namenode"')
print commands.getstatusoutput('sudo ansible jobtracker -a "hostnamectl set-hostname jobtracker"')
print commands.getstatusoutput('sudo ansible client -a "hostnamectl set-hostname client"')

for i in range(0,num) :
    print commands.getstatusoutput('sudo ansible {} -a "hostnamectl set-hostname datanode{}"'.format(form['datanode{}'.format(str(i+1))],str(i+1)))

#Add all hosts in each node
commands.getstatusoutput('sudo python addhosts.py {}'.format(str(num)))
commands.getstatusoutput('sudo ansible-playbook ansible/setuphosts.yml')

commands.getstatusoutput('sudo python corefile.py {}'.format(form['namemode'])
commands.getstatusoutput('sudo python mapredfile.py {}'.format(form['jobtracker'])

#Configure each node, Setup configuration files
config = commands.getstatusoutput('sudo ansible-playbook ansible/confighadoop.yml')

#Start Services
services = commands.getstatusoutput('sudo ansible-playbook ansible/startservices.yml')

commands.getstatusoutput('sudo ansible-playbook ansible/executemapper.yml')

if services[0] == 0 and config[0] == 0 :
    print "location: hadoop-auto-success.py"
    print

else :
    print
    print "Setup Failed"
