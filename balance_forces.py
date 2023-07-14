#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import pandas as pd
import pretty_html_table
import base64
from bs4 import BeautifulSoup
import cgi
import cgitb
cgitb.enable()
data_uri = base64.b64encode(open(r"C:\xampp\htdocs\diplom\images\static3.png", 'rb').read()).decode('cp1251')

html=f"""<form action=\"balance_forces2.py\">
<h1 align=center>Задача на тему "Равновесие произвольной системы сил"</h1>
<img src="data:image/png;base64,{data_uri}">
<h2>
На круглой наклонной площадке, ось которой ACD наклонена к вертикали под углом alfa°, укреплено в точке B тело веса F Н.
Определить момент относительно оси AD, создаваемый силой тяжести тела, если радиус CB=l м горизонтален.
</h2>
alfa=<input type=\"text\" name=alfa>
F=<input type=\"text\" name=F>
l=<input type=\"text\" name=l>
<h1>Ответ:</h1>
M=<input type=\"text\" name=M>
<input type=\"submit\" value=\"Решить\">
<input type=\"reset\" value=\"Отмена\">
<form>
"""
print(html.encode('cp1251', 'replace').decode('cp1251', 'replace'))