#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe
import cgitb
import cgi
from bs4 import BeautifulSoup
import base64
import pretty_html_table
import pandas as pd
from connect import *

cgitb.enable()
html = """
<form action=\"login2.py\">
  user=<input type=\"text\" name=user>
  password=<input type=\"text\" name=password>
  <input type=\"submit\" value=\"Войти\">
  <a href="http://localhost/diplom/register.py">Если у вас нет аккаунта, то нужно зарегестрироваться</a>
"""
print(html)
