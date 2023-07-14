#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import math
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()

#!/usr/bin/evn python3


alfa=form.getfirst('alfa')
F = form.getfirst('F')
l=form.getfirst('l')
M=form.getfirst('M')

realM=float(F)*float(l)*math.sin(math.radians(float(alfa)))
realM=round(realM)
print(f"<br><b>Введенный ответ:</b> <br>M={M} <br>")
print(f"<br><b>Правильный ответ:</b><br>M={realM} <br>")
rez=0
if(realM==float(M)):
    print("<h3>Ответ верный!</h3>")
    rez=1
else:
    print("<h3>Ответ неверный!</h3>")
cur=con.cursor()
cur._query(f"Select max(n) FROM `balance_forces` WHERE id={gl.i}")
result = cur.fetchone()[0]
if(result==None):
    result=1
else:
    result+=1
cur._query(f"""insert into `balance_forces` values
	(
		{result},{gl.i},{alfa},{F},{l},{M},{rez}	
	)""")
con.commit()
print("""<a href="http://localhost/diplom/zadanie.py">Вернуться на главную страницу</a>""")