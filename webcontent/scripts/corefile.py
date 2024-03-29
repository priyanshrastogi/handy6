import commands
import sys

corestr = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:10001</value>
</property>
</configuration>
'''.format(sys.argv[1])

commands.getoutput('echo \'{}\' > /root/app_files/core-site.xml'.format(corestr))
