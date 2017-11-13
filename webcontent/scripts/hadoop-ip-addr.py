#!/usr/bin/python2

import cgi

print "Content-Type: text/html"
print

num = int(cgi.FormContent()['numdn'][0])

print '''
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Project</title>

    <link rel="stylesheet" href="../bootstrap-3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="../css/hadoop-ip.css">
    <link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet">
</head>

<body>
    <div class="project-title">
        <h1>INSTINCTIVE 6</h1>
    </div>

    <div class="container">
        <div class="row">
            <div class="col-md-4 col-md-offset-4 col-sm-12 custom-panel">
                <div class="panel panel-primary">
                    <div class="panel-heading">
                        <h3 class="panel-title">Enter IP Address</h3>
                    </div>
                    <div class="panel-body center-div">
                        <form action="hadoop-man.py">
                            <div class="input-group form-input-custom">
                                <span class="input-group-addon">Namenode</span>
                                <input type="text" class="form-control" placeholder="e.g. 192.50.0.1" name="namenode">
                            </div>
                            <div class="input-group form-input-custom">
                                <span class="input-group-addon">JobTracker</span>
                                <input type="text" class="form-control" placeholder="e.g. 192.50.0.1" name="jobtracker">
                            </div>
                            <div class="input-group form-input-custom">
                                <span class="input-group-addon">Client</span>
                                <input type="text" class="form-control" placeholder="e.g. 192.50.0.1" name="client">
                            </div>
'''

for i in range(0,num) :
    print '''
                            <div class="input-group form-input-custom">
                                <span class="input-group-addon">Datanode {0}</span>
                                <input type="text" class="form-control" placeholder="e.g. 192.50.0.1" name="datanode{0}"> </div>'''.format(str(i+1))

print '''
                            <input class="btn btn-primary" type="submit" value="Configure">
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <p class="text-center">&copy; Invasive Analysts, 2017</p>
</body>
'''
