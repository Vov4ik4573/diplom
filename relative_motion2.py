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
x = form.getfirst('x')
F=form.getfirst('F')
Av=form.getfirst('Av')
T=form.getfirst('T')
A=form.getfirst('A')

w=2*math.pi/float(T)
w=round(w,1)
c=float(F)/(float(x))*100
sqrk=float(c)/float(m)
Ao=float(Av)*w**2/(sqrk-w**2)
realA=Ao+float(Av)
realA=round(realA)
print(f"<br><b>Введенный ответ:</b> <br>A={A} <br>")
print(f"<br><b>Правильный ответ:</b><br>A={realA} <br>")
rez=0
if(realA==float(A)):
    print("<h3>Ответ верный!</h3>")
    rez=1
else:
    print("<h3>Ответ неверный!</h3>")
cur=con.cursor()
cur._query(f"Select max(n) FROM `relative_motion` WHERE id={gl.i}")
result = cur.fetchone()[0]
if(result==None):
    result=1
else:
    result+=1
cur._query(f"""insert into `relative_motion` values
	(
		{result},{gl.i},{m},{x},{F},{Av},{T},{A},{rez}	
	)""")
con.commit()
print("""<a href="http://localhost/diplom/zadanie.py">Вернуться на главную страницу</a>""")