
from flask import Flask, render_template, request, session, url_for, redirect
import pymongo
from pymongo import MongoClient
import json

app = Flask(__name__)
    
app.secret_key = 'keyidontknow'

if __name__ == '__main__':
   
    app.run(debug = True)

client = MongoClient("mongo", 27017) 
db = client.SampleCollections       


#modificación parcial, borrado, y adicción de nuevos documentos
#http://0.0.0.0:5000/mongo
#sudo docker-compose up
#sudo docker-compose exec mongo /bin/bash
#mongo restore--drop dump
# mongon:   http://0.0.0.0:8081/




@app.route("/")
def index():
    return render_template("index.html")

#-------------------------------------------------------
@app.route("/buscar", methods=['GET'])
def buscar():
    try:
        pkmn = db.samples_pokemon.find({"id" : int(request.args.get("id"))})
       
        return render_template('index.html', name=pkmn[0]["name"], img=pkmn[0]["img"])
    except:
        return render_template('index.html')
    
    
#-------------------------------------------------------

#-------OK
@app.route("/modificar", methods=['POST','GET'])
def modificar():


     if request.method == 'POST':

        try:
            db.samples_pokemon.update({"id" : request.form.get('id',type=int)}, {"$set" : {"name" : request.form.get('name')}})
            pkmn = db.samples_pokemon.find({"id" : request.form.get('id',type=int)})
            return render_template('index.html', name=pkmn[0]["name"], img=pkmn[0]["img"])
        except:
            return render_template('page_not_found.html')
        
     else:
         return render_template('modificar.html')
       


#-------OK
@app.route("/borrar",methods=['POST','GET'])
def borrar():
    

      if request.method == 'POST':

        db.samples_pokemon.remove({"id" :  request.form.get('id',type=int)})
        return render_template('index.html')
     
      else:
        return render_template('borrar.html')
    
        
@app.route("/registrar", methods=['POST','GET'])
def registrar():
#id	num	name	img	type	height	weight	candy	candy_count	egg	spawn_chance	avg_spawns	spawn_time	multipliers	weaknesses	next_evolution	prev_evolution

    if request.method == 'POST':
        
        name= request.form.get('name')
        img = request.form.get('img')
        type_ = request.form.get('type')
        height = request.form.get('height')
        weight = request.form.get('weight')
        candy = request.form.get('candy') 
       


        pok = db.samples_pokemon.find()
        lista_pok = []
        for p in pok:
            app.logger.debug(p) # salida consola
            lista_pok.append(p)
        
        #Índice del ultimo elemento de la base de datos 
        n=lista_pok[-1]["num"]
        n_int= int(n)
        n_int=n_int+1
        n=str(n_int)
        new_pokemon = {"id": n_int, 'num': n, 'name': name, 'img': img, 'type': type_, 'height': height, 'weight': weight, 'candy': candy}
        
        db.samples_pokemon.insert_one(new_pokemon)
        return redirect(url_for("index"))
    else:
       return render_template('registrar.html')
    
#-------------------------------------------------------
# Error 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')

