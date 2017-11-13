import commands
import sys

#To get IP address of each container and save them in etc/ansible/hosts
hosts = "[namenode]\n"
ip = commands.getstatusoutput("docker inspect namenode | jq '.[].NetworkSettings.Networks.bridge.IPAddress'")
hosts = hosts + ip[1].strip('"') + " ansible_ssh_user=root ansible_ssh_pass=redhat\n"

ip = commands.getstatusoutput("docker inspect jobtracker | jq '.[].NetworkSettings.Networks.bridge.IPAddress'")
hosts = hosts + "\n[jobtracker]\n" + ip[1].strip('"') + " ansible_ssh_user=root ansible_ssh_pass=redhat\n"

ip = commands.getstatusoutput("docker inspect client | jq '.[].NetworkSettings.Networks.bridge.IPAddress'")
hosts = hosts + "\n[client]\n" + ip[1].strip('"') + " ansible_ssh_user=root ansible_ssh_pass=redhat\n"

hosts = hosts + "\n[datanode]\n"
num = int(sys.argv[1])
for i in range(0,num) :
    ip = commands.getstatusoutput("docker inspect datanode{} | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(str(i+1)))
    hosts = hosts + ip[1].strip('"') + " ansible_ssh_user=root ansible_ssh_pass=redhat\n"

commands.getoutput('echo "{}" > /etc/ansible/hosts'.format(hosts))
