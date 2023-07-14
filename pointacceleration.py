#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import pandas as pd
import pretty_html_table

html=f"""<form action=\"pointacceleration2.py\">
<h1 align=center>Задача на тему "Ускорение точки</h1>
<h2>Поезд движется равнозамедленно по дуге окружности радиуса R м и проходит путь s м, имея 
начальную скорость v0 км/ч и конечную v км/ч. Определить полное ускорение поезда в начале w0 (м/с<sup><small>2</small></sup>) и в конце 
дуги w (м/с<sup><small>2</small></sup>), а также время движения по этой дуге t.</h2>
R=<input type=\"text\" name=R>
s=<input type=\"text\" name=s>
v0=<input type=\"text\" name=v0>
v=<input type=\"text\" name=v>
<h1>Ответ:</h1>
w0=<input type=\"text\" name=w0> 
w=<input type=\"text\" name=w>
t=<input type=\"text\" name=t>  
<input type=\"submit\" value=\"Решить\">
<input type=\"reset\" value=\"Отмена\">
<form>
"""
print(html)