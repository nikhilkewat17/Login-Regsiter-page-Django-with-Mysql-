from django.shortcuts import render
import  mysql.connector as sql
em=''
pwd=''

def login(request):
    global em,pwd
    if request.method=="POST":
        nik=sql.connect(host="localhost",user="root",password="nik358",database='website')
        cursor=nik.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,'welcome.html')


    return  render(request,'login.html')