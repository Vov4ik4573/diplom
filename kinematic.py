#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import pandas as pd
import pretty_html_table
import base64
from bs4 import BeautifulSoup
import cgi
import cgitb
cgitb.enable()
data_uri = base64.b64encode(open(r"C:\xampp\htdocs\diplom\images\kinematic5.png", 'rb').read()).decode('cp1251')
html=f"""<form action=\"kinematic2.py\">
<h1 align=center>Задача на тему "Смешанные задачи на сложное движение точки и твердого тела"</h1>
<img src="data:image/png;base64,{data_uri}">
<h2>
Стержень AB длины l м скользит концом A вниз вдоль оси y, а концом B вдоль оси x направо. Точка
A движется по закону yA=(ya-t<sup><small>2</small></sup>) м. Одновременно вдоль стержня от A к B соскальзывает точка M.
Определить модуль абсолютной скорости и абсолютного ускорения точки M в момент t с, если
уравнение движения точки M вдоль оси s, совмещенной со стержнем, имеет вид s=AM=s*t<sup><small>2</small></sup> м.
</h2>
l=<input type=\"text\" name=l>
ya=<input type=\"text\" name=ya>
t=<input type=\"text\" name=t>
s=<input type=\"text\" name=s>
<h1>Ответ:</h1>
vm=<input type=\"text\" name=vm>
wm=<input type=\"text\" name=wm>
<input type=\"submit\" value=\"Решить\">
<input type=\"reset\" value=\"Отмена\">
<form>
"""
print(html.encode('cp1251', 'replace').decode('cp1251', 'replace'))