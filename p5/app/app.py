
from flask import Flask, render_template, request, session, url_for, redirect
import pymongo
from pymongo import MongoClient
import json
from flask import request, jsonify
from bson import ObjectId

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

#http PUT httpbin.org/put X-API-Token:123 name=John
# Cabeceras : X-API-Token , parámetros: name= John
#http POST http://localhost:500/api/movies name=John age=23
# ?name=John&age=23




# para devolver una lista (GET), o añadir (POST)
@app.route('/api/pokemons', methods=['GET', 'POST'])
def api_1():

    if request.method == 'GET':
        try :
            lista = []
            pokemons = db.samples_pokemon.find()
            for pkmn in pokemons:
                lista.append({
                    'id':    str(pkmn.get('id')), # pasa a string el ObjectId
                    'name': pkmn.get('name'), 
                    'img':  pkmn.get('img'),
                    'type':  pkmn.get('type')
                    })
            return jsonify(lista)
        except:
             return jsonify({'error':'Not found'}), 404
    elif request.method == 'POST':
        try:
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

            return jsonify({
                
                    'id':    str(new_pokemon.get('id')),
                    'name': new_pokemon.get('name'), 
                    'img':  new_pokemon.get('img'),
                    'type':  new_pokemon.get('type'),
                    'modified': 'OK'
                })
        except:
            return jsonify({'error':'Couldn\'t create the element'}), 404


# para devolver una, modificar o borrar
@app.route('/api/pokemons/<id>', methods=['GET', 'PUT', 'DELETE'])
def api_2(id):
    if request.method == 'GET':
        try:
            pkmn = db.samples_pokemon.find_one({'_id':ObjectId(id)})
            return jsonify({
                '_id':    id,
                'id':    str(pkmn.get('id')),
                'name': pkmn.get('name'), 
                'img':  pkmn.get('img'),
                'type':  pkmn.get('type')
            })
        except:
          return jsonify({'error':'Not found'}), 404
    elif request.method == 'DELETE':
        try:
            pkmn = db.samples_pokemon.find_one({'_id':ObjectId(id)})
            db.samples_pokemon.remove({'_id':ObjectId(id)})
            return jsonify({
                '_id':    id,
                'id':    str(pkmn.get('id')),
                'name': pkmn.get('name'), 
                'img':  pkmn.get('img'),
                'type':  pkmn.get('type'),
                'deleted': 'OK'
            })
        except:
            return jsonify({'error':'Element to delete not found'}), 404
    elif request.method == 'PUT':
        #Cambiamos el nombre del pokemon
        try:
            #request.args.put("name")
            db.samples_pokemon.update({'_id':ObjectId(id)}, {"$set" : {'name' :  request.form.get('name') }})
            pkmn = db.samples_pokemon.find_one({'_id':ObjectId(id)})
            return jsonify({
                '_id':    id,
                'id':    str(pkmn.get('id')),
                'name': pkmn.get('name'), 
                'img':  pkmn.get('img'),
                'type':  pkmn.get('type'),
                'modified': 'OK'
            })
        except:
            return jsonify({'error':'Couldn\'t find the element to be modified'}), 404




    
#-------------------------------------------------------
# Error 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')

