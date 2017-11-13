#!/usr/bin/python2

import random
import commands
import cgi

print "content-type: text/html"
print

form = cgi.FormContent()
operation = form['opt'][0]
ifile = form['infile'][0]

f = open('uploads/hrdata.csv','w')
f.write(ifile)
f.close()

commands.getstatusoutput('sudo ansible-playbook ansible/transferupload.yml')

#Upload csv file
commands.getstatusoutput('sudo ansible client -m command -a "hadoop fs -put hrdata.csv /"')

#Generate random numbers to make different output folders in hadoop fs
rnum1 = str(random.randint(1,10000))
rnum2 = str(random.randint(1,10000))

commands.getstatusoutput('sudo ansible client -m command -a \'hadoop jar /usr/share/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar -input /hrdata.csv -mapper cat -reducer "wc -l" -output /out{}\''.format(rnum1))

if operation == 'lefthigh' :
    commands.getstatusoutput('sudo ansible client -m command -a "hadoop jar /usr/share/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar -input /hrdata.csv -file maphigh.py -mapper ./maphigh.py -file reducer.py -reducer ./reducer.py -output /out{}"'.format(rnum2))

elif operation == 'leftmed' :
    commands.getstatusoutput('sudo ansible client -m command -a "hadoop jar /usr/share/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar -input /hrdata.csv -file mapmed.py -mapper ./mapmed.py -file reducer.py -reducer ./reducer.py -output /out{}"'.format(rnum2))

elif operation == 'leftlow' :
    commands.getstatusoutput('sudo ansible client -m command -a "hadoop jar /usr/share/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar -input /hrdata.csv -file maplow.py -mapper ./maplow.py -file reducer.py -reducer ./reducer.py -output /out{}"'.format(rnum2))

elif operation == 'sat' :
    commands.getstatusoutput('sudo ansible client -m command -a "hadoop jar /usr/share/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar -input /hrdata.csv -file mapsat.py -mapper ./mapsat.py -file reducersat.py -reducer ./reducersat.py -output /out{}"'.format(rnum2))

#To save mapreduce results in local client machine
commands.getoutput('sudo ansible client -m shell -a "hadoop fs -cat /out{}/part-00000 > total.txt"'.format(rnum1))
commands.getoutput('sudo ansible client -m shell -a "hadoop fs -cat /out{}/part-00000 > result.txt"'.format(rnum2))

#To transfer results file from client to our server.
commands.getstatusoutput('sudo ansible client -m fetch -a "src=/root/result.txt dest=/root/app_files/"')
commands.getstatusoutput('sudo ansible client -m fetch -a "src=/root/total.txt dest=/root/app_files/"')

#To open results file
result = commands.getoutput('sudo cat /root/app_files/172.17.0.4/root/result.txt')
total = commands.getoutput('sudo cat /root/app_files/172.17.0.4/root/total.txt')

print '''
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Project</title>

    <link rel="stylesheet" href="../bootstrap-3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="../css/hadoop-auto-success.css">
    <link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet">
</head>

<body>
    <div class="container">
        <div class=" project-title">
            <h1>HR ANALYSIS WITH HANDY 6</h1>
        </div>
        <div class="row content-box">
            <p class="success">SUCCESS</p><br>
            <p class="disc">Your Analysis Report is Here:</p><br>
'''

print "<p> Total Number of Employees : {}</p><br>".format(total.strip('\t\n'))

if operation == 'lefthigh' :
    print "<p> Total Employees who left the job despite high salary  : {}</p><br>".format(result.strip('\t\n'))

elif operation == 'leftmed' :
    print "<p> Total Employees left the job with medium salary  : {}</p><br>".format(result.strip('\t\n'))

elif operation == 'leftlow' :
    print "<p> Total Employees,left the job with low salary  : {}</p><br>".format(result.strip('\t\n'))

elif operation == 'sat' :
    print "<p> Total Employees, with satisfaction 0-49% : {}</p><br>".format(result.split('\t\n')[0])
    print "<p> Total Employees, with satisfaction 50-74%  : {}</p><br>".format(result.split('\t\n')[1])
    print "<p> Total Employees, with satisfaction 75-100%  : {}</p><br>".format(result.split('\t\n')[2].strip('\n'))

print '''
        <button class="btn btn-primary custom-button" onclick="location.href='../upload-file.html'">Upload and Analyse Data</button>
        </div>
    </div>
    <p class="copyright">&copy; Invasive Analysts, 2017</p>
</body>
'''
