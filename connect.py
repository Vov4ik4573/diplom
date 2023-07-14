#!C:\Users\79192\AppData\Local\Programs\Python\Python311\python.exe
print("Content-Type: text/html\n\n")

import MySQLdb

con=MySQLdb.connect('127.0.0.1','root','','diplom')
if not con:
    print ("Connection Not Established")