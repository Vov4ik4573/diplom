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
Q = form.getfirst('Q')
S=form.getfirst('S')
N=form.getfirst('N')

realS=float(Q)*math.cos(math.radians(float(alfa)))
realS=round(realS,2)
realN=float(Q)*math.cos(math.radians(90-float(alfa)))
realN=round(realN,2)
print(f"<br><b>Введенный ответ:</b> <br>S={S} <br>N={N}<br>")
print(f"<br><b>Правильный ответ:</b><br>S={realS} <br> N={realN}<br>")
rez=0
if(realS==float(S) and realN==float(N)):
    print("<h3>Ответ верный!</h3>")
    rez=1
else:
    print("<h3>Ответ неверный!</h3>")
cur=con.cursor()
cur._query(f"Select max(n) FROM `intersection_forces` WHERE id={gl.i}")
result = cur.fetchone()[0]
if(result==None):
    result=1
else:
    result+=1
cur._query(f"""insert into `intersection_forces` values
	(
		{result},{gl.i},{alfa},{Q},{S},{N},{rez}	
	)""")
con.commit()
print("""<a href="http://localhost/diplom/zadanie.py">Вернуться на главную страницу</a>""")