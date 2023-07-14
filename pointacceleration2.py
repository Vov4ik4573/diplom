#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import math
import cgi
import cgitb
import gl
cgitb.enable()
form = cgi.FieldStorage()

#!/usr/bin/evn python3

R=form.getfirst('R')
s=form.getfirst('s')
v0=form.getfirst('v0')
v=form.getfirst('v')
w0=form.getfirst('w0')
w=form.getfirst('w')
t=form.getfirst('t')

v0=float(v0)/3.6
v=float(v)/3.6
realt=2*float(s)/(v+v0)
a=round((v-v0)/realt,3)
an0=round(v0**2/float(R),3)
an=round(v**2/float(R),3)
realw0=round(math.sqrt(a**2+an0**2),3)
realw=round(math.sqrt(a**2+an**2),3)
print(f"<br><b>Введенный ответ:</b> <br>w0={w0} <br>w={w} <br>t={t}<br>")
print(f"<br><b>Правильный ответ:</b><br>w0={realw0} <br>w={realw} <br>t={realt}<br>")
rez=0
if(realt==float(t) and realw0==float(w0) and realw==float(w)):
    print("<h3>Ответ верный!</h3>")
    rez=1
else:
    print("<h3>Ответ неверный!</h3>")
cur=con.cursor()
cur._query(f"Select max(n) FROM `pointacceleration` WHERE id={gl.i}")
result = cur.fetchone()[0]
if(result==None):
    result=1
else:
    result+=1
cur._query(f"""insert into `pointacceleration` values
	(
		{result},{gl.i},{R},{s},{v0},{v},{w0},{w},{t},{rez}	
	)""")
con.commit()
print("""<a href="http://localhost/diplom/zadanie.py">Вернуться на главную страницу</a>""")