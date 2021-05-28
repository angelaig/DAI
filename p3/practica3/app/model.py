from pickleshare import *
import re #para controlar exp regulares
#----------------BASE-DE-DATOS 


##Introduccion de usuarios iniciales:
def start_DB():

    db = PickleShareDB('miBD')
  

    db['usuario1'] = dict()
    db['usuario1']['passw'] = 'ab'
    db['usuario1'] = db['usuario1']

    db['usuario2'] = dict()
    db['usuario2']['passw'] = 'contraseñausuario2'
    db['usuario2'] = db['usuario2']


def sign_up_db( username, password):

    db = PickleShareDB('miBD')
    
    if username in db.keys():
        return False
    else:
        db[username] = dict()
        db[username]['passw'] = password
        db[username] = db[username]
        return True
 
    return False
    
    
    
    
    
def right_db( username, password):

    db = PickleShareDB('miBD')
    
    if username in db.keys():
        return db[username]['passw'] == password
    else:
       return False
 
    return False

def change_username_db(username,username2 ,password):

    db = PickleShareDB('miBD')
    if username2 in db.keys():
        return False
    elif username in db.keys() and db[username]['passw'] == password:
        db[username2] = dict()
        db[username2]['passw'] = password
        db[username2]=db[username2]
        db[username].clear()
        del db[username]
        return True
    else:
    	return False
    return False

def change_password_db(username,password ,password2):

    db = PickleShareDB('miBD')
    if username in db.keys() and db[username]['passw'] == password:
        db[username].clear()
        db[username]['passw'] = password2
        db[username]=db[username]
        return True
    return False 
    
def delete_account_db(username):

    db = PickleShareDB('miBD')
    if username in db.keys():
        db[username].clear()
        del db[username]
        return True
    return False 

#----------------------------------


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


def rectangle():

    r = lambda: random.randint(0,800)
    background_color = '#%02X%02X%02X' % (r(),r(),r())
    border_color = '#%02X%02X%02X' % (r(),r(),r())

    widht = random.randint(40, 140)
    height = random.randint(40, 240)

   

    return '<rect  width="%s" height="%s" style="fill:%s;stroke:%s;stroke-width:2" />' % ( widht, height, background_color,border_color) 
