#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import pandas as pd
import pretty_html_table


html=f"""<form action=\"addition_of_accelerations2.py\">
<h1 align=center>Задача на тему "Сложение ускорений"</h1>
<h2>На токарном станке обтачивается цилиндр диаметра l мм. Шпиндель делает T об/мин. Скорость продольной 
подачи постоянна и равна v мм/с. Определить скорость vr и ускорение резца относительно обрабатываемого цилиндра wr и wc (м/с<sup><small>2</small></sup>).(результат округлить до десятых)
</h2>
l=<input type=\"text\" name=l>
T=<input type=\"text\" name=T>
v=<input type=\"text\" name=v>
<h1>Ответ:</h1>
vr=<input type=\"text\" name=vr>
wr=<input type=\"text\" name=wr>
wc=<input type=\"text\" name=wc> 
<input type=\"submit\" value=\"Решить\">
<input type=\"reset\" value=\"Отмена\">
<form>
"""
print(html)