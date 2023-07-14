#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import pandas as pd
import pretty_html_table
import base64
from bs4 import BeautifulSoup
import cgi
import cgitb
cgitb.enable()
data_uri = base64.b64encode(open(r"C:\xampp\htdocs\diplom\images\static1.png", 'rb').read()).decode('cp1251')
html=f"""<form action=\"intersection_forces2.py\">
<h1 align=center>Задача на тему "Силы, линии действия которых пересекаются в одной точке"</h1>
<img src="data:image/png;base64,{data_uri}">
<h2>
По направлению стропильной ноги, наклоненной к горизонту под углом alfa°, действует сила Q кН. Какое 
усилие S возникает при этом по направлению горизонтальной затяжки и какая сила N действует на стену 
по отвесному направлению?
</h2>
alfa=<input type=\"text\" name=alfa>
Q=<input type=\"text\" name=Q>
<h1>Ответ:</h1>
S=<input type=\"text\" name=S>
N=<input type=\"text\" name=N>
<input type=\"submit\" value=\"Решить\">
<input type=\"reset\" value=\"Отмена\">
<form>
"""
print(html.encode('cp1251', 'replace').decode('cp1251', 'replace'))