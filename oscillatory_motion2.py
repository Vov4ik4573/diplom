#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import math
import cgi
import cgitb
import gl
cgitb.enable()
form = cgi.FieldStorage()

#!/usr/bin/evn python3

option = form.getlist('radio_fio')
m=form.getfirst('M')
v = form.getfirst('v')
c=form.getfirst('c')
F=form.getfirst('F')

realF=float(m)*(9.8+float(v)*math.sqrt(float(c)/float(m)*10**3))
realF=round(realF,1)
print(f"<br><b>Введенный ответ:</b> <br>F={F} <br>")
print(f"<br><b>Правильный ответ:</b><br>F={realF} <br>")
rez=0
if(realF==float(F)):
    print("<h3>Ответ верный!</h3>")
    rez=1
else:
    print("<h3>Ответ неверный!</h3>")
cur=con.cursor()
cur._query(f"Select max(n) FROM `oscillatory_motion` WHERE id={gl.i}")
result = cur.fetchone()[0]
if(result==None):
    result=1
else:
    result+=1
cur._query(f"""insert into `oscillatory_motion` values
	(
		{result},{gl.i},{m},{v},{c},{F},{rez}	
	)""")
con.commit()
print("""<a href="http://localhost/diplom/zadanie.py">Вернуться на главную страницу</a>""")