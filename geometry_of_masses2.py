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
r = form.getfirst('r')
I=form.getfirst('I')

realI=3*float(m)*float(r)**2/2
realF=round(realI,1)
print(f"<br><b>Введенный ответ:</b> <br>I={I} <br>")
print(f"<br><b>Правильный ответ:</b><br>I={realI} <br>")
rez=0
if(realI==float(I)):
    print("<h3>Ответ верный!</h3>")
    rez=1
else:
    print("<h3>Ответ неверный!</h3>")
cur=con.cursor()
cur._query(f"Select max(n) FROM `geometry_of_masses` WHERE id={gl.i}")
result = cur.fetchone()[0]
if(result==None):
    result=1
else:
    result+=1
cur._query(f"""insert into `geometry_of_masses` values
	(
		{result},{gl.i},{m},{r},{I},{rez}	
	)""")
con.commit()
print("""<a href="http://localhost/diplom/zadanie.py">Вернуться на главную страницу</a>""")