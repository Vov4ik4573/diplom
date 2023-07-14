#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import math
import cgi
import cgitb
import gl
cgitb.enable()
form = cgi.FieldStorage()

#!/usr/bin/evn python3

l = form.getfirst('l')
ya=form.getfirst('ya')
t=form.getfirst('t')
s=form.getfirst('s')
vm=form.getfirst('vm')
wm=form.getfirst('wm')

cosal=(float(ya)-float(t)**2)/float(l)
sinal=math.sqrt(1-cosal**2)
dal=2*float(t)/float(l)/sinal
ddal=2/float(l)/sinal
vr=2*float(s)*float(t)
dxm=(float(s)*float(t)**2)*dal*cosal
dym=-(float(s)*float(t)**2)*dal*sinal
vx=vr*sinal+dxm
vy=vr*cosal+dym
realvm=math.sqrt(vx**2+vy**2)
wr=2*float(s)
ddxm=(float(s)*float(t)**2)*(ddal*cosal-dal**2*sinal)
ddym=-(float(s)*float(t)**2)*(ddal*sinal-dal**2*cosal)
wcor=2*dal*vr
w1=wcor-ddym*sinal
w2=wcor+ddxm*cosal
realwm=math.sqrt(w1**2+w2**2)

print(f"<br><b>Введенный ответ:</b> <br>vm={vm} <br>wm={wm}")
print(f"<br><b>Правильный ответ:</b><br>vm={realvm} <br>wm={realwm}<br>")
rez=0
if(realwm==float(wm) and realvm==float(vm)):
    print("<h3>Ответ верный!</h3>")
    rez=1
else:
    print("<h3>Ответ неверный!</h3>")
cur=con.cursor()
cur._query(f"Select max(n) FROM `mixed_kinematics_problems` WHERE id={gl.i}")
result = cur.fetchone()[0]
if(result==None):
    result=1
else:
    result+=1
cur._query(f"""insert into `mixed_kinematics_problems` values
	(
		{result},{gl.i},{l},{ya},{t},{s},{vm},{wm},{rez}	
	)""")
con.commit()
print("""<a href="http://localhost/diplom/zadanie.py">начать решать задачи</a>""")