#!/usr/bin/python

import cgi
import commands

print "content-type: text/html"
print

print '''
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Project</title>

    <link rel="stylesheet" href="../bootstrap-3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="../css/docker.css">
    <link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet">
</head>

<body>
    <div class="container">
        <div class=" project-title">
            <h1>HANDY 6</h1>
        </div>
        <table class="table-responsive table table-bordered custom-table">
            <thead>
                <tr>
                    <th>Image Name</th><th>Container Name</th><th>IP Address</th><th>Status</th><th>Stop</th><th>Start</th><th>Delete</th>
                </tr>
            </thead>
            <tbody>
'''
a = 1
for i in commands.getoutput("sudo docker ps -a").split('\n') :
    #To pass first line of our output
    if a==1 :
        a+=1
        pass

    else :
        j = i.split()
        cStatus = commands.getoutput("sudo docker inspect {0} | jq '.[].State.Status'".format(j[-1]))
        ip = commands.getstatusoutput("sudo docker inspect {0} | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(j[-1]))
        print '<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td><button class="btn btn-warning" value="{1}" onclick="cstop(this.value)">Stop</button></td><td><button class="btn btn-success" value="{1}" onclick="cstart(this.value)">Start</button></td><td><button class="btn btn-danger" value="{1}" onclick="cremove(this.value)">Delete</button></td></tr>'.format(j[1],j[-1],ip[1].strip('"'),cStatus)

print '''
            </tbody>
        </table>
        <div class="row">
            <div class="col-md-4 col-sm-12 col-md-offset-4 button-panel">
                <button class="btn btn-primary" onclick="location.href='docker-add.py'">Add New Container</button>
            </div>
        </div>
    <p class="copyright">&copy; Invasive Analysts, 2017</p>
    <script>
        function cstart(cname) {
        document.location='docker-start.py?cname='+cname;
        }
        function cstop(cname) {
        document.location='docker-stop.py?cname='+cname;
        }
        function cremove(cname) {
        var c = confirm("Are you sure?")
        if (c == true) {
            document.location='docker-remove.py?cname='+cname;
        }
        }
    </script>
</body>
'''
