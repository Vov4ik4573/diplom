#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import pandas as pd
import pretty_html_table
import base64
from bs4 import BeautifulSoup
import cgi
import cgitb
cgitb.enable()
data_uri = base64.b64encode(open(r"C:\xampp\htdocs\diplom\images\dinamic3.png", 'rb').read()).decode('cp1251')

html=f"""<form action=\"relative_motion2.py\">
<h1 align=center>Задача на тему "Относительное движение"</h1>
<img src="data:image/png;base64,{data_uri}">
<h2>
К концу A вертикального упругого стержня AB прикреплен груз C массы m кг. Груз C, будучи выведен из
 положения равновесия, совершает гармонические колебания под влиянием силы, пропорциональной расстоянию 
 от положения равновесия. Стержень AB таков, что для отклонения конца его A на x см нужно приложить силу F Н. 
 Найти амплитуду вынужденных колебаний груза C в том случае, когда точка закрепления стержня B совершает 
 по горизонтальной прямой гармонические колебания амплитуды Av мм и периода T с.
</h2>
m=<input type=\"text\" name=m>
x=<input type=\"text\" name=x>
F=<input type=\"text\" name=F>
Av=<input type=\"text\" name=Av>
T=<input type=\"text\" name=T>
<h1>Ответ:</h1>
A=<input type=\"text\" name=A>
<input type=\"submit\" value=\"Решить\">
<input type=\"reset\" value=\"Отмена\">
<form>
"""
print(html.encode('cp1251', 'replace').decode('cp1251', 'replace'))