import pymongo
import webbrowser

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["pedia"]
mycol = mydb["vita"]

stud = []

tbl = ""
stud.append(tbl)

for y in mycol.find():
    a = "<tr><td>NAME :%s</td></tr>"%y['name']
    stud.append(a)
    b = "<tr><td><br>PLANTS :%s</td></tr>"%y['plants']
    stud.append(b)
    c = "<tr><td><br>FUNCTION :%s</td></tr>"%y['function']
    stud.append(c)
    d = "<tr><td><br>DEFICIENCY :%s</td></tr>"%y['deficiency']
    stud.append(d)
    e = "<tr><td><br>WHAT IS VITAMIN A:%s</td></tr>"%y['what']
    stud.append(e)
    f = "<tr><td><br>FUNCTION OF VITAMIN A:%s</td></tr>"%y['fun']
    stud.append(f)
    g = "<tr><td><br>HEALTH BENIFITES OF VITAMIN A:%s</td></tr>"%y['health']
    stud.append(g)
    h = "<tr><td><br>DEFICIENCY IN VITAMIN A:%s</td></tr>"%y['defi']
    stud.append(h)
    i = "<tr><td><br>FOOD SOURCES FOR VITAMIN A:%s</td></tr>"%y['food']
    stud.append(i)



contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<title>Python Webbrowser</title>
</head>
<body>
<table>
%s
</table>
</body>
</html>
'''%(stud)

filename = 'webbrowser.html'

def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

main(contents, filename)    
webbrowser.open(filename)