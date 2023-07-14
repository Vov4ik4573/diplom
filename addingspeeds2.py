#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import math
import cgi
import cgitb
import gl
cgitb.enable()
form = cgi.FieldStorage()

#!/usr/bin/evn python3

t=form.getfirst('t')
s=form.getfirst('s')
t1=form.getfirst('t1')
l=form.getfirst('l')
u=form.getfirst('u')
v=form.getfirst('v')

realv=float(s)/float(t)
reall=realv*float(t)*float(t1)/math.sqrt(float(t1)**2-float(t)**2)
realu=reall/float(t)
print(f"<br><b>Введенный ответ:</b> <br>l={l} <br>u={u} <br>v={v}")
print(f"<br><b>Правильный ответ:</b><br>l={reall} <br>u={realu}<br> v={realv}<br>")
rez=0
if(reall==float(l) and realu==float(u) and realv==float(v)):
    print("<h3>Ответ верный!</h3>")
    rez=1
else:
    print("<h3>Ответ неверный!</h3>")
cur=con.cursor()
cur._query(f"Select max(n) FROM `addingspeeds` WHERE id={gl.i}")
result = cur.fetchone()[0]
if(result==None):
    result=1
else:
    result+=1
cur._query(f"""insert into `addingspeeds` values
	(
		{result},{gl.i},{t},{s},{t1},{l},{u},{v},{rez}	
	)""")
con.commit()
print("""<a href="http://localhost/diplom/zadanie.py">Вернуться на главную страницу</a>""")