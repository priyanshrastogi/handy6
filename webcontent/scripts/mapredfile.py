import commands
import sys

mapredstr = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>{}:9001</value>
</property>
</configuration>
'''.format(sys.argv[1])

commands.getoutput('echo \'{}\' > /root/app_files/mapred-site.xml'.format(mapredstr))
