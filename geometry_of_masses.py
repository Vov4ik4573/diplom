#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import pandas as pd
import pretty_html_table
import base64
from bs4 import BeautifulSoup
import cgi
import cgitb
cgitb.enable()
html=f"""<form action=\"geometry_of_masses2.py\">
<h1 align=center>Задача на тему "Геометрия масс: центр масс материальной системы, моменты инерции твердых тел"</h1>
<h2>
Вычислить момент инерции стального вала радиуса r см и массы m кг относительно его образующей. Вал
считать однородным сплошным цилиндром.
</h2>
m=<input type=\"text\" name=m>
r=<input type=\"text\" name=r>
<h1>Ответ:</h1>
I=<input type=\"text\" name=I>
<input type=\"submit\" value=\"Решить\">
<input type=\"reset\" value=\"Отмена\">
<form>
"""
print(html.encode('cp1251', 'replace').decode('cp1251', 'replace'))