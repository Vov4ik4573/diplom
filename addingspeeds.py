#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe

from connect import *
import pandas as pd
import pretty_html_table

html=f"""<form action=\"addingspeeds2.py\">
<h1 align=center>Задача на тему "Сложение скоростей"</h1>
<h2>Берега реки параллельны; лодка вышла из точки A и, держа курс перпендикулярно берегам, достигла 
противоположного берега через t мин после отправления. При этом она попала в точку C, лежащую на s м
ниже точки A по течению реки. Чтобы, двигаясь с прежней относительной скоростью, попасть из точки A в точку
B, лежащую на прямой AB, перпендикулярной берегам, лодке надо держать курс под некоторым углом к прямой
AB и против течения; в этом случае лодка достигает противоположного берега через t1 мин. Определить
ширину реки l(м), относительную скорость u(м/мин) лодки по отношению к воде и скорость v(м/мин) течения реки.</h2>
t=<input type=\"text\" name=t>
s=<input type=\"text\" name=s>
t1=<input type=\"text\" name=t1>
<h1>Ответ:</h1>
l=<input type=\"text\" name=l>
u=<input type=\"text\" name=u>
v=<input type=\"text\" name=v> 
<input type=\"submit\" value=\"Решить\">
<input type=\"reset\" value=\"Отмена\">
<form>
"""
print(html)