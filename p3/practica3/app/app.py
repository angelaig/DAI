
from flask import Flask, flash, redirect, request, url_for, session
from flask import render_template
from random import randrange
import sys
import time
import re #para controlar exp regulares
import random
from model import *
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

start_DB()





#------------------------------------------------------------------
correct = random.randint(1,100)
count=0

@app.route('/adivina')
def adivina():
    return render_template("adivina.html") # this should be the name of your html file

@app.route('/adivina', methods=['POST'])
def adivina_post():
    global correct
    global count
    msg = ''
    print(count)
    if count<10:
        count+=1
        n_in= request.form['n']
        n_in = int(n_in)

        if n_in < correct:
            msg = 'El numero es mayor que el introducido'
            return render_template("adivina.html", msg=msg)
        elif n_in > correct:
            msg = 'El numero es menor que el introducido '
            return render_template("adivina.html", msg=msg)
        else:
            if n_in == correct:
                msg = 'Adivinaste el número en  '+ str(count)+ ' intentos'
                count = 0
                correct = random.randint(1,100)
                return render_template("adivina.html", msg=msg)
    else:
        num = 'Lo siento, acabaste tus intentos , el número era  ' + str(correct)
        correct = random.randint(1,20)
        msg = ''
        count=0
        return render_template("adivina.html", num=num)
  
#------------------------------------------------------------------------        
@app.route('/')
def inicio():
	
    return render_template("index.html")

#------------------------------------------------------------------------
#------------------------------------------------------------------------
@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():

    error = None


    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if sign_up_db( username, password):
            session['username'] = username
            session['passw'] = password
            flash('New user '+request.form['username']+'created')
            return redirect('/ ')
        else:
            error = 'Try another username '
            return redirect('sign-up')
    else:
        error= 'Try another username '   
    
    return render_template('sign-up.html',error=error)
    
#------------------------------------------------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':

        if right_db( request.form['username'], request.form['password']) : 
                    username =request.form['username']
                    password = request.form['password']
                    session['username'] = username
                    session['passw'] = password
                    flash('Welcome'+ username )
                    return redirect('/')
       
        else:
            error = 'Sorry , there aren\'t users with that username and password '
    return render_template('login.html', error=error)


#------------------------------------------------------------------------
@app.route('/logout')
def log_out():
    if 'username' in session:
        session.clear()
        flash('Sesión cerrada')
    return redirect('/')
    

#------------------------------------------------------------------------

@app.route('/profile')
def profile():
    if 'username' in session:
        username = session['username']
    else:
        username = ''
    if 'passw' in session:
        password = session['passw']
    else:
        password = ''
    return render_template('/profile.html',username=username,password=password)
 
#----------------------------------------------------------------------


@app.route('/change-username', methods=['GET', 'POST'])
def change_username():

    error = None


    if request.method == 'POST':
        
        if change_username_db(request.form['username'], request.form['username2'], request.form['password']):
            flash('User'+request.form['username2']+' added')
            return redirect(url_for('log_out'))
        else:
            error= 'Coudlnt change username , try another username or log out '
        session['username']=request.form['username']
        session['passw']=request.form['password']
    else:
        if 'username' not in session:
            flash("log in ")
        return render_template('change-username.html', error=error)
    
    return render_template('change-username.html', error=error)
#-------------------------------------------------------------------------
@app.route('/change-password', methods=['GET', 'POST'])
def change_password():
    error = None


    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if 'username' in session and session['passw'] == request.form['password']:
            

            if request.form['password2'] == request.form['password3']:
                
                if change_password_db(request.form['username'],password ,request.form['password2']):
                    flash("Password changed")
                    session['username']= username
                    session['passw'] = request.form['password2']
                    return redirect(url_for('log_out'))

                else:
                  error= 'Couldnt change password'
                  return render_template('change-password.html', error=error)
            
                session['passw']=request.form['password']
                error= 'Couldnt change password'
                return render_template('change-password.html', error=error)
            else:
                error = 'Passwords don\'t match'
        else:
            error = 'Incorrect password'
            
    else:
      
        return render_template('change-password.html', error=error)
            
    return render_template('change-password.html', error=error)

#----------------------------------------------------------------------
@app.route('/delete-account', methods=['GET', 'POST'])
def delete_account():
    error = None


    if request.method == 'POST':
        if 'username' in session and session['passw'] == request.form['password']:
            username = session['username']
            if delete_account_db(username):
                
                flash('User deleted')
                return redirect(url_for('log_out'))
            
            else:
                error= 'Wrong password'
        else:
            if 'username' not in session:
                error = 'Session expired. Please log in '
                flash("You should be logged in")
                return redirect('/')
            error= 'Error , you need to log in'
 
    else:
        return render_template('delete-account.html', error=error)

    return render_template('delete-account.html', error=error)

    
    
@app.after_request
def store_visted_urls(response):
    if 'username' in session:
        if session.get('urls') is None:
            session['urls'] = []    
        session['urls'].append(request.url)
        if(len(session['urls']) > 3):
            session['urls'].pop(0)
        session.modified = True

    
    return response

@app.context_processor
def LastVisited():
    if session.get('urls') is not None:
        last = session['urls']
    else:
        last = []
    return dict(lastUrls = last)



#------------------------------------------------------------------------
@app.route('/ordenar/<string:array>')
def ordenar(array):
    
    arrayList = [int(x) for x in array.split(',')]
    burbuja = arrayList.copy()
    insercion = arrayList.copy()
    seleccion= arrayList.copy()


    init = time.time()
    bubbleSort(burbuja)
    t_burbuja = time.time() - init



    init = time.time()
    insertionSort(insercion)
    t_insercion = time.time() - init

    
    init = time.time()
    selectionSort(seleccion)
    t_seleccion= time.time() - init

    return render_template("ordenar.html", original=arrayList, burbuja=burbuja,  insercion=insercion,seleccion=seleccion, tiempo_burbuja=t_burbuja, tiempo_insercion=t_insercion,tiempo_seleccion=t_seleccion)


#------------------------------------------------------------------------
@app.route('/criba/<int:num>')
def criba(num):
    return render_template("criba.html",n=len(
criba_eratostenes(num)), original=criba_eratostenes(num), num=num)


#------------------------------------------------------------------------
@app.route('/fibonacci/<int:num>')
def fibo(num):
    return render_template("fibonacci.html", posicion=num, resultado=fibonacci(num))

#------------------------------------------------------------------------
@app.route('/anidados')
def anidados():
    n = randrange(40)
    list = ['[',']']
    array = []
    for i in range(n):
        array.append(list[randrange(len(list))])
    return render_template('anidados.html',lista=array, boolean=corchetes_anidados(array))


#------------------------------------------------------------------------
@app.route('/palabra/<string:array>')
def palabra(array):
    return render_template('palabra.html',text=detect_word_uppercase( array ))

#------------------------------------------------------------------------
@app.route('/email/<string:array>')
def email(array):
    return render_template('email.html',text=detect_email(array))
#------------------------------------------------------------------------
@app.route('/numeros/<string:array>')
def numeros(array):
    return render_template('numeros.html',text=detect_credit_card_number(array))

#------------------------------------------------------------------------
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
#------------------------------------------------------------------------


#------------------------------------------------------------------
@app.route('/svg/')
def dibujar ():
	principio ='<svg height="10000" width="5000000">'
	final = '</svg>'
	aux_bool = random.randint(0,1)
	if aux_bool :
		return principio+ellipse() +final 
	else :
		return principio+rectangle() +final 



