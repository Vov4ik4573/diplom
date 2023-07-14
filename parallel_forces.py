#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import pandas as pd
import pretty_html_table
import base64
from bs4 import BeautifulSoup
import cgi
import cgitb
cgitb.enable()
data_uri = base64.b64encode(open(r"C:\xampp\htdocs\diplom\images\static2.png", 'rb').read()).decode('cp1251')
html=f"""<form action=\"parallel_forces2.py\">
<h1 align=center>Задача на тему "Параллельные силы"</h1>
<img src="data:image/png;base64,{data_uri}">
<h2>
Однородный стержень AB, длина которого l м, а вес F Н, подвешен горизонтально на двух параллельных
веревках AC и BD. К стержню в точке E на расстоянии AE=x м подвешен груз P Н. Определить натяжения 
веревок TC и TD.
</h2>
l=<input type=\"text\" name=l>
F=<input type=\"text\" name=F>
x=<input type=\"text\" name=x>
P=<input type=\"text\" name=P>
<h1>Ответ:</h1>
TC=<input type=\"text\" name=TC>
TD=<input type=\"text\" name=TD>
<input type=\"submit\" value=\"Решить\">
<input type=\"reset\" value=\"Отмена\">
<form>
"""
print(html.encode('cp1251', 'replace').decode('cp1251', 'replace'))