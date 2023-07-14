#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import math
import cgi
import cgitb
import gl
cgitb.enable()
form = cgi.FieldStorage()

#!/usr/bin/evn python3

alfa=form.getfirst('alfa')
v=form.getfirst('v')
g=form.getfirst('g')
h=form.getfirst('h')
v1=form.getfirst('v1')
print(alfa)
print(v)

realh=float(v)*math.cos(math.radians(float(alfa)))
realh=round(realh)
realv1=-float(g)
print(f"<br><b>Введенный ответ:</b> <br>h={h} <br>v1={v1}")
print(f"<br><b>Правильный ответ:</b><br>h={realh} <br>v1={realv1}<br>")
rez=0
if(realh==float(h) and realv1==float(v1)):
    print("<h3>Ответ верный!</h3>")
    rez=1
else:
    print("<h3>Ответ неверный!</h3>")
cur=con.cursor()
cur._query(f"Select max(n) FROM `point speed` WHERE id={gl.i}")
result = cur.fetchone()[0]
if(result==None):
    result=1
else:
    result+=1
cur._query(f"""insert into `point speed` values
	(
		{result},{gl.i},{alfa},{v},{g},{h},{v1},{rez}	
	)""")
con.commit()
print("""<a href="http://localhost/diplom/zadanie.py">Вернуться на главную страницу</a>""")