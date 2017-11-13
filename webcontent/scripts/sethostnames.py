import commands
import sys

print commands.getstatusoutput('ansible namenode -a "hostname -b namenode"')

print commands.getstatusoutput('ansible jobtracker -a "hostname -b jobtracker"')

commands.getstatusoutput('ansible client -a "hostname -b client"')

num = int(sys.argv[1])
for i in range(0,num) :
    ip = commands.getstatusoutput("docker inspect datanode{} | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(str(i+1)))
    print commands.getstatusoutput('ansible {} -a "hostname -b datanode{}"'.format(ip[1].strip('"'),str(i+1)))
