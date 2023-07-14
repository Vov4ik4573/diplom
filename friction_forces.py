#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import pandas as pd
import pretty_html_table
import base64
from bs4 import BeautifulSoup
import cgi
import cgitb
cgitb.enable()
html=f"""<form action=\"friction_forces2.py\">
<h1 align=center>Задача на тему "Силы трения"</h1>
<h2>
Поезд поднимается по прямолинейному пути, имеющему уклон a, с постоянной скоростью; вес поезда, не
считая электровоза, F кН. Какова сила тяги P электровоза, если сопротивление движению равно q силы
давления поезда на рельсы?
</h2>
a=<input type=\"text\" name=a>
F=<input type=\"text\" name=F>
q=<input type=\"text\" name=q>
<h1>Ответ:</h1>
P=<input type=\"text\" name=P>
<input type=\"submit\" value=\"Решить\">
<input type=\"reset\" value=\"Отмена\">
<form>
"""
print(html.encode('cp1251', 'replace').decode('cp1251', 'replace'))