#!/usr/bin/python

import commands
import cgi

print "Content-Type: text/html"

num = int(cgi.FormContent()['numdatanode'][0])

#Start Docker containers
commands.getstatusoutput('sudo docker run -dit -h namenode --privileged=true --name namenode centoshadoop:2')
commands.getstatusoutput('sudo docker run -dit -h jobtracker --privileged=true --name jobtracker centoshadoop:2')
commands.getstatusoutput('sudo docker run -dit -h client --privileged=true --name client centoshadoop:2')

for i in range(0,num) :
    commands.getstatusoutput('sudo docker run -dit -h datanode{0} --privileged=true --name datanode{0} centoshadoop:2'.format(str(i+1)))

#Get IP address of all nodes and set'em in /etc/ansible/hosts
commands.getstatusoutput('sudo python getip.py {}'.format(str(num)))

#Set hostnames of all nodes
commands.getstatusoutput('sudo python sethostnames.py {}'.format(str(num)))

#Add all hosts in each node
commands.getstatusoutput('sudo python addhosts.py {}'.format(str(num)))
commands.getstatusoutput('sudo ansible-playbook ansible/setuphosts.yml')

ipName = commands.getstatusoutput("sudo docker inspect namenode | jq '.[].NetworkSettings.Networks.bridge.IPAddress'")
ipJob = commands.getstatusoutput("sudo docker inspect jobtracker | jq '.[].NetworkSettings.Networks.bridge.IPAddress'")

commands.getstatusoutput('sudo python corefile.py {}'.format(ipName[1].strip('"')))
commands.getstatusoutput('sudo python mapredfile.py {}'.format(ipJob[1].strip('"')))

#Configure each node, Setup configuration files
config = commands.getstatusoutput('sudo ansible-playbook ansible/confighadoop.yml')

#Start Services
services = commands.getstatusoutput('sudo ansible-playbook ansible/startservices.yml')

commands.getstatusoutput('sudo ansible-playbook ansible/executemapper.yml')

if services[0] == 0 and config[0] == 0 :
    print "location: hadoop-auto-success.py"
    print

else :
    print "location: ../hadoop-failed.html"
    print
