#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"
print

#To get namespace ID
nsid =  commands.getoutput('sudo ansible namenode -m shell -a "cat /metadata/current/VERSION"').split('\n')

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
            <p class="disc">Your Hadoop Cluster is ready with following details:</p><br>
'''

print "<p>Your Namespace ID is : {}</p><br>".format(nsid[2].split('=')[1])

print '''
        <button class="btn btn-primary custom-button" onclick="location.href='../upload-file.html'">Upload and Analyse Data</button>
        </div>
    </div>
    <p class="copyright">&copy; Invasive Analysts, 2017</p>
</body>
'''
