
from flask import Flask
from flask import render_template
from random import randrange
import sys
import time
import re #para controlar exp regulares
import random

#-----------------------------------------------------------
#Burbuja
def bubbleSort(array): 
    n = len(array) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if array[j] > array[j+1] : 
                array[j], array[j+1] = array[j+1], array[j] 
  
#----------------------------------------------------------
#Insercion
def insertionSort(array): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(array)): 
  
        aux = array[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and aux < array[j] : 
                array[j+1] = array[j] 
                j -= 1
        array[j+1] = aux

#-----------------------------------------------------------
#Seleccion 
def selectionSort(array):
  n = len(array)
  for i in range(n):
    # Initially, assume the first element of the unsorted part as the minimum.
    minimum = i

    for j in range(i+1, n):
      if (array[j] < array[minimum]):
        # Update position of minimum element if a smaller element is found.
        minimum = j

    # Swap the minimum element with the first element of the unsorted part.     
    temp = array[i]
    array[i] = array[minimum]
    array[minimum] = temp


#-------------------------------------------------------------
#
#Criba de erastotenes 

def criba_eratostenes(n):

	not_primes = []

   
	for i in range(2, int(n ** .5) + 1):
	    if i not in not_primes:
	        for j in range(i, int(n / i) + 1): not_primes.append(i * j)
	        
	
	primes = [p for p in range(2, n + 1) if p not in not_primes and p!=n]


	return primes


#---------------------------------------------------------------
#Fibonacci
def fibonacci(n):
    if n<=0:
        print("Error input")
    # First fibonacci number is 0
    elif n==1:
        return 0
    # Second fibonacci number is 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


#---------------------------------------------------------------
# Corchetes correctamente anidados 
def corchetes_anidados(array):
    i = 0
    for x in array:
        if x == '[':
            i = i + 1
        else:
            i = i - 1
            if i < 0:
                return False
    return i==0

#-------------------------------------------------------------------
#Expresiones regulares 

def detect_word_uppercase( array ):
	
	return re.findall(r'[a-zA-Z_]+\s[A-Z_]', array)

def detect_email(array):
	
	return re.findall(r'[\w\.-]+@[\w\.-]+(?:\.[\w]+)+', array)


def detect_credit_card_number(array):
	
	 return re.findall(r'\d{4}[\s|-]+\d{4}[\s|-]+\d{4}[\s|-]+\d{4}', array)





#------------------------------------------------------------------
#####Los Routings
app = Flask(__name__)
  
#------------------------------------------------------------------------        
@app.route('/')
def inicio():
	
    return render_template("index.html")

#------------------------------------------------------------------------

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


'''example
<svg height="140" width="500">
  <ellipse cx="200" cy="80" rx="100" ry="50"
  style="fill:yellow;stroke:purple;stroke-width:2" />
</svg>
'''
def ellipse():
  

    r = lambda: random.randint(0,255)
    background_color = '#%02X%02X%02X' % (r(),r(),r())
    border_color = '#%02X%02X%02X' % (r(),r(),r())
    cx = random.randint(20, 400)
    cy = random.randint(20, 400)

    rx = random.randint(20, 140)
    ry = random.randint(20, 140)

   

    return '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" style="fill:%s;stroke:%s;stroke-width:2" />' % (cx, cy, rx, ry, background_color, border_color)

#------------------------------------------------------------------
''' Example 
	<svg width="400" height="110">
  <rect width="300" height="100" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
</svg>
'''

def rectangle():

    r = lambda: random.randint(0,800)
    background_color = '#%02X%02X%02X' % (r(),r(),r())
    border_color = '#%02X%02X%02X' % (r(),r(),r())

    widht = random.randint(40, 140)
    height = random.randint(40, 240)

   

    return '<rect  width="%s" height="%s" style="fill:%s;stroke:%s;stroke-width:2" />' % ( widht, height, background_color,border_color) 

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



