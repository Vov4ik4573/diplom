#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import math
import cgi
import cgitb
import gl
cgitb.enable()
form = cgi.FieldStorage()

#!/usr/bin/evn python3

l=form.getfirst('l')
F = form.getfirst('F')
x=form.getfirst('x')
P=form.getfirst('P')
TC=form.getfirst('TC')
TD=form.getfirst('TD')

realTC=float(P)*(float(l)-float(x))+float(F)*0.5*float(l)
realTC=round(realTC,2)
realTD=float(P)*float(x)+float(F)*0.5*float(l)
realTD=round(realTD,2)
print(f"<br><b>Введенный ответ:</b> <br>TC={TC} <br>TD={TD}<br>")
print(f"<br><b>Правильный ответ:</b><br>TC={realTC} <br> TD={realTD}<br>")
rez=0
if(realTC==float(TC) and realTD==float(TD)):
    print("<h3>Ответ верный!</h3>")
    rez=1
else:
    print("<h3>Ответ неверный!</h3>")
cur=con.cursor()
cur._query(f"Select max(n) FROM `parallel_forces` WHERE id={gl.i}")
result = cur.fetchone()[0]
if(result==None):
    result=1
else:
    result+=1
cur._query(f"""insert into `parallel_forces` values
	(
		{result},{gl.i},{l},{F},{x},{P},{TC},{TD},{rez}	
	)""")
con.commit()
print("""<a href="http://localhost/diplom/zadanie.py">Вернуться на главную страницу</a>""")