#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe
import cgitb
import cgi
import math
from connect import *

cgitb.enable()
form = cgi.FieldStorage()

#!/usr/bin/evn python3

user = form.getfirst('user').encode('1251', 'replace').decode('1251', 'replace')
password = form.getfirst('password').encode('1251', 'replace').decode('1251', 'replace')

cur = con.cursor()
cur._query(f"Select max(id) FROM `fio`")
result = cur.fetchone()[0]
if (result == None):
    result=0
cur.execute(f"""INSERT INTO `fio`(`id`, `fio`,`password`) VALUES (%s, %s, %s)""",(result+1, user,password))
idp=result
import login
con.commit()