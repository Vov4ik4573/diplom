#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import math
import cgi
import cgitb
import gl
cgitb.enable()
form = cgi.FieldStorage()

#!/usr/bin/evn python3

m=form.getfirst('m')
l = form.getfirst('l')
alfa=form.getfirst('alfa')
v=form.getfirst('v')
T=form.getfirst('T')

realT=float(m)*9.8/math.cos(math.radians(float(alfa)))
realv=math.sin(math.radians(float(alfa)))*math.sqrt(9.8*float(l)/math.cos(math.radians(float(alfa))))
realT=round(realT)
realv=round(realv,1)
print(f"<br><b>Введенный ответ:</b> <br>v={v} <br>T={T}")
print(f"<br><b>Правильный ответ:</b><br>v={realv} <br>T={realT}<br>")
rez=0
if(realv==float(v) and realT==float(T)):
    print("<h3>Ответ верный!</h3>")
    rez=1
else:
    print("<h3>Ответ неверный!</h3>")
cur=con.cursor()
cur._query(f"Select max(n) FROM `determination_of_forces` WHERE id={gl.i}")
result = cur.fetchone()[0]
if(result==None):
    result=1
else:
    result+=1
cur._query(f"""insert into `determination_of_forces` values
	(
		{result},{gl.i},{m},{l},{alfa},{v},{T},{rez}	
	)""")
con.commit()
print("""<a href="http://localhost/diplom/zadanie.py">Вернуться на главную страницу</a>""")