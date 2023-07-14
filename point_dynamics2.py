#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import math
import cgi
import cgitb
import gl
cgitb.enable()
form = cgi.FieldStorage()

#!/usr/bin/evn python3

v=form.getfirst('v')
z = form.getfirst('z')
vz=form.getfirst('vz')
t=form.getfirst('t')

realt=(float(v)*math.log(float(z))-float(vz))/1.62
realt=round(realt)
print(f"<br><b>Введенный ответ:</b> <br>t={t} <br>")
print(f"<br><b>Правильный ответ:</b><br>t={realt} <br>")
rez=0
if(realt==float(t)):
    print("<h3>Ответ верный!</h3>")
    rez=1
else:
    print("<h3>Ответ неверный!</h3>")
cur=con.cursor()
cur._query(f"Select max(n) FROM `point_dynamics` WHERE id={gl.i}")
result = cur.fetchone()[0]
if(result==None):
    result=1
else:
    result+=1
cur._query(f"""insert into `point_dynamics` values
	(
		{result},{gl.i},{v},{z},{vz},{t},{rez}	
	)""")
con.commit()
print("""<a href="http://localhost/diplom/zadanie.py">Вернуться на главную страницу</a>""")