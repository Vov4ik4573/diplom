#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import pandas as pd
import pretty_html_table
import base64
from bs4 import BeautifulSoup
import cgi
import cgitb
cgitb.enable()
data_uri = base64.b64encode(open(r"C:\xampp\htdocs\diplom\images\dinamic2.png", 'rb').read()).decode('cp1251')
html=f"""<form action=\"oscillatory_motion2.py\">
<h1 align=center>Задача на тему "Колебательное движение"</h1>
<img src="data:image/png;base64,{data_uri}">
<h2>
При равномерном спуске груза массы M т со скоростью v м/с произошла неожиданная задержка верхнего
конца троса, на котором опускался груз, из-за защемления троса в обойме блока. Пренебрегая массой троса,
определить его наибольшее натяжение при последующих колебаниях груза, если коэффициент жесткости троса c·10<sup><small>6</small></sup> Н/м.
(Ответ дайте в кН)
</h2>
M=<input type=\"text\" name=M>
v=<input type=\"text\" name=v>
c=<input type=\"text\" name=c>
<h1>Ответ:</h1>
F=<input type=\"text\" name=F>
<input type=\"submit\" value=\"Решить\">
<input type=\"reset\" value=\"Отмена\">
<form>
"""
print(html.encode('cp1251', 'replace').decode('cp1251', 'replace'))