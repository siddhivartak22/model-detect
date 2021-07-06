#! /usr/bin/python3

print("content-type: text/html")
print()

import cgi
import subprocess


f = cgi.FieldStorage()

plate_no = f.getvalue("Number")
if plate_no == "KA 05 NB 1786":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:lightblue;" >VECHICLE DETAILS</h1>')
    print('''<pre>
    Registration Name : SIDDHI VARTAK 
    License No : 985471221114
    Make / Model : PULSER 200
    Registration Date : 05/02/2011\4
    Registering Authority : MAH , INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2022
    Fitness Upto : 4/8/2030
    </pre>''')
    print("</body>")
