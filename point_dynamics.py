#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import pandas as pd
import pretty_html_table
import base64
from bs4 import BeautifulSoup
import cgi
import cgitb
cgitb.enable()
html=f"""<form action=\"point_dynamics2.py\">
<h1 align=center>Задача на тему "Динамика точки и системы переменной массы (переменного состава)"</h1>
<h2>
Ракета стартует с Луны вертикально к ее поверхности. Эффективная скорость истечения ve=v м/с. Число
Циолковского z. Определить, какое должно быть время сгорания топлива, чтобы ракета достигла скорости
v=vz м/с (принять, что ускорение силы тяжести вблизи Луны постоянно и равно 1,62 м/с2).
</h2>
v=<input type=\"text\" name=v>
z=<input type=\"text\" name=z>
vz=<input type=\"text\" name=vz>
<h1>Ответ:</h1>
t=<input type=\"text\" name=t>
<input type=\"submit\" value=\"Решить\">
<input type=\"reset\" value=\"Отмена\">
<form>
"""
print(html.encode('cp1251', 'replace').decode('cp1251', 'replace'))