from django.shortcuts import render
import  mysql.connector as sql
fn=''
ln=''
g=''
em=''
pwd=''

def signup(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        nik=sql.connect(host="localhost",user="root",password="nik358",database='website')
        cursor=nik.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="gender":
                g=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c="insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,g,em,pwd)
        cursor.execute(c)
        nik.commit()
    return  render(request,'signup.html')




