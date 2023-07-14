#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import pandas as pd
import pretty_html_table
import base64
from bs4 import BeautifulSoup
import cgi
import cgitb
cgitb.enable()
data_uri = base64.b64encode(open(r"C:\xampp\htdocs\diplom\images\dinamic1.png", 'rb').read()).decode('cp1251')
html=f"""<form action=\"dinamic12.py\">
<h1 align=center>Задача на тему "Определение сил по заданному движению"</h1>
<img src="data:image/png;base64,{data_uri}">
<h2>
Груз М массы m кг, подвешенный на нити длины l м в неподвижной точке О, представляет собой
конический маятник, т. е. описывает окружность в горизонтальной плоскости, причем нить составляет с
вертикалью угол alfa°. Определить скорость v груза и натяжение T нити.
</h2>
m=<input type=\"text\" name=m>
l=<input type=\"text\" name=l>
alfa=<input type=\"text\" name=alfa>
<h1>Ответ:</h1>
v=<input type=\"text\" name=v>
T=<input type=\"text\" name=T>
<input type=\"submit\" value=\"Решить\">
<input type=\"reset\" value=\"Отмена\">
<form>
"""
print(html.encode('cp1251', 'replace').decode('cp1251', 'replace'))