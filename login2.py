#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe
import cgitb
import cgi
import math
from connect import *
import gl

cgitb.enable()
form = cgi.FieldStorage()

#!/usr/bin/evn python3

user = form.getfirst('user').encode(
    '1251', 'replace').decode('1251', 'replace')
password = form.getfirst('password').encode(
    '1251', 'replace').decode('1251', 'replace')


cur = con.cursor()
cur._query(
    "Select id FROM `fio` WHERE fio='{}' AND password='{}'".format(str(user), str(password)))
result = cur.fetchone()
if (result == None):
    print("<h1>Неверно указаны логин или(и) пароль</h1>")
    import login
else:
    idp = result[0]
    f = open('gl.py', 'w')
    f.write(f"i={idp}")
    f.close()
    print("<h1>Вход проведен успешно</h1>")
    print("""<a href="http://localhost/diplom/zadanie.py">начать решать задачи</a>""")
con.commit()
