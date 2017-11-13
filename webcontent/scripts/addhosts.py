import commands
import sys

hosts = ""
ip = commands.getstatusoutput("docker inspect namenode | jq '.[].NetworkSettings.Networks.bridge.IPAddress'")
hosts = hosts + ip[1].strip('"') + "\tnamenode\n"

ip = commands.getstatusoutput("docker inspect jobtracker | jq '.[].NetworkSettings.Networks.bridge.IPAddress'")
hosts = hosts + ip[1].strip('"') + "\tjobtracker\n"

ip = commands.getstatusoutput("docker inspect client | jq '.[].NetworkSettings.Networks.bridge.IPAddress'")
hosts = hosts + ip[1].strip('"') + "\tclient\n"

num = int(sys.argv[1])
for i in range(0,num) :
    ip = commands.getstatusoutput("docker inspect datanode{} | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(str(i+1)))
    hosts = hosts + ip[1].strip('"') + "\tdatanode{}\n".format(str(i+1))

commands.getstatusoutput('sudo echo "{}" > /root/app_files/hosts.txt'.format(hosts))
