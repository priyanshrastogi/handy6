#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"
print

print '''
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Project</title>

    <link rel="stylesheet" href="../bootstrap-3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="../css/index.css">
    <link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet">
</head>

<body>
    <div class="container">
        <div class=" project-title">
            <h1>INSTINCTIVE 6</h1>
        </div>
        <div class="col-md-4 col-md-offset-4 col-sm-12 custom-panel">
            <div class="panel panel-primary">
                <div class="panel-heading">
                    <h3 class="panel-title">Add New Container</h3>
                </div>
                <div class="panel-body center-div">
                    <form action="docker-run.py">
                        <div class="input-group form-input-custom">
                            <span class="input-group-addon">Container Name</span>
                            <input type="text" class="form-control" placeholder="Please Enter" name="cname" required>
                        </div>
                        <div class="input-group form-input-custom">
                            <span class="input-group-addon">Select Image</span>
                            <select class="form-control" name="iname">
'''

a = 1
for i in commands.getoutput("sudo docker images").split('\n') :
    if a == 1:
        a+=1
        pass

    else :
        j = i.split()
        print '<option>{}:{}</option>'.format(j[0],j[1])
print '''
                            </select>
                        </div>
                        <input class="btn btn-primary" type="submit" value="Add">
                    </form>
                </div>
            </div>
        </div>
    </div>
    <p class="copyright">&copy; Invasive Analysts, 2017</p>
</body>
'''
