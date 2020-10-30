from django.shortcuts import render 
from sqlserverconnect.models import sqlserverconn
import pyodbc

def connsql(request):
    conn = pyodbc.connect('Driver={sql server};'
                          'Server=ABP-DR-INTEDW\DATA_ANALYTICS;'
                          'Database=Django_Abdulrahman;'
                          'uid=sa;'
                          'pwd=Analytics10$;'
                          'Trusted_Connections=yes;')
    cursor=conn.cursor()
    cursor.execute("select * from Employee")
    result=cursor.fetchall()
    return render(request,'index.html',{'sqlserverconn':result})