#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe
from connect import *
import math
import cgi
import cgitb
import gl
cgitb.enable()
form = cgi.FieldStorage()

#!/usr/bin/evn python3

a=form.getfirst('a')
F = form.getfirst('F')
q=form.getfirst('q')
P=form.getfirst('P')

realP=float(F)*(((math.sin(math.radians(float(a)))) if float(a)>=1 else float(a)) + (float(q)*math.cos(math.radians(float(a))) if float(a)>=1 else float(q)))
realP=round(realP)
print(f"<br><b>Введенный ответ:</b> <br>P={P}<br>")
print(f"<br><b>Правильный ответ:</b><br>P={realP}<br>")
rez=0
if(realP==float(P)):
    print("<h3>Ответ верный!</h3>")
    rez=1
else:
    print("<h3>Ответ неверный!</h3>")
cur=con.cursor()
cur._query(f"Select max(n) FROM `friction_forces` WHERE id={gl.i}")
result = cur.fetchone()[0]
if(result==None):
    result=1
else:
    result+=1
cur._query(f"""insert into `friction_forces` values
	(
		{result},{gl.i},{a},{F},{q},{P},{rez}	
	)""")
con.commit()
print("""<a href="http://localhost/diplom/zadanie.py">Вернуться на главную страницу</a>""")