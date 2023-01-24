from django.shortcuts import render
import mysql.connector as sql

fn = '' # Primeiro nome
ln = '' # Ultimo nome
s = '' # Sexo 
em = '' # Email
pwd = '' # Senha

def signaction(request):

    global fn, ln, s, em, pwd

    if request.method=="POST":
        m = sql.connect(host="localhost", user="root", passwd="1234", database="website")   #SE DER ERRADO VERIFICAR AQUI !!!!
        
        cursor = m.cursor()
        
        d = request.POST

        for key, value in d.items():
            if key == "first_name":
                fn = value
            if key == "last_name":
                ln = value
            if key == "sex":
                s = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value
        
        c = "insert into users Values('{}', '{}', '{}', '{}', '{}')".format(fn,ln,s,em,pwd)

        cursor.execute(c)

        m.commit()
    
    return render(request, 'signup_page.html')


