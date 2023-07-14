#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import pandas as pd
import pretty_html_table


html=f"""<form action=\"pointspeed2.py\">
<h1 align=center>Задача на тему "Скорость точки</h1>
<h2>Из орудия, ось которого образует угол (alfa)° с горизонтом, выпущен снаряд со скоростью (v)м/с. 
Предполагая, что снаряд имеет только ускорение силы тяжести (g)м/с<sup><small>2</small></sup>, найти годограф скорости снаряда(h) м и скорость точки, 
вычерчивающей годограф(v1) м/с.</h2>
alfa=<input type=\"text\" name=alfa>
v=<input type=\"text\" name=v>
g=<input type=\"text\" name=g>
<h1>Ответ:</h1>
h=<input type=\"text\" name=h> 
v1=<input type=\"text\" name=v1> 
<input type=\"submit\" value=\"Решить\">
<input type=\"reset\" value=\"Отмена\">
<form>
"""
print(html)