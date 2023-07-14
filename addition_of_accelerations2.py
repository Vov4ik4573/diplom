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
T=form.getfirst('T')
v=form.getfirst('v')
vr=form.getfirst('vr')
wr=form.getfirst('wr')
wc=form.getfirst('wc')


w=math.pi*float(T)/30
vf=w*float(l)/2
realvr=round(math.sqrt(vf**2+float(v)**2),1)
realwr=round(w**2*40,1)
realwc=round((w**2)*float(l),1)
print(f"<br><b>Введенный ответ:</b> <br>vr={vr} <br>wr={wr} <br>wc={wc}")
print(f"<br><b>Правильный ответ:</b><br>vr={realvr} <br>wr={realwr}<br> wc={realwc}<br>")
rez=0
if(realwc==float(wc) and realvr==float(vr) and realwr==float(wr)):
    print("<h3>Ответ верный!</h3>")
    rez=1
else:
    print("<h3>Ответ неверный!</h3>")
cur=con.cursor()
cur._query(f"Select max(n) FROM `addition_of_accelerations` WHERE id={gl.i}")
result = cur.fetchone()[0]
if(result==None):
    result=1
else:
    result+=1
cur._query(f"""insert into `addition_of_accelerations` values
	(
		{result},{gl.i},{l},{T},{v},{vr},{wr},{wc},{rez}	
	)""")
con.commit()
print("""<a href="http://localhost/diplom/zadanie.py">Вернуться на главную страницу</a>""")