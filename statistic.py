#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe
from connect import *
import gl
import MySQLdb
import html

res=[]
cur=con.cursor()
cur._query(f"Select max(n) FROM `point speed` WHERE id={gl.i}")
result = cur.fetchone()[0]
if result==None:
    result=0
else:
    res.append(result)
