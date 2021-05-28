
from flask import Flask
import pymongo
from pymongo import MongoClient
import json
from flask import request, jsonify
from bson import ObjectId
from flask_restful import Api, Resource, reqparse, abort


app = Flask(__name__)

app.secret_key = 'keyidontknow'
api = Api(app)
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


#id	num	name	img	type	height	weight	candy	candy_count	egg	spawn_chance	avg_spawns	spawn_time	multipliers	weaknesses	next_evolution	prev_evolution
class pok(Resource):


	def get(self, poke_id):
		try:
			pkmn = db.samples_pokemon.find_one({'_id': ObjectId(poke_id)})
			return {'_id' : poke_id , 'id' : str(pkmn.get('id')) ,'name': pkmn.get('name'),
					'img':  pkmn.get('img'),
					'type':  pkmn.get('type')}
		except:
			abort(404, message="Couldn't return the element")

	#---------------------------------------------------------------------------------------------------------------------------------------------
	def put(self, poke_id):
		try:
			db.samples_pokemon.update({'_id': ObjectId(poke_id)}, {"$set" : {'name' :  request.form.get('name')}})
			pkmn = db.samples_pokemon.find_one({'_id' : ObjectId(poke_id)})
			return {'_id' : poke_id , 'id' : str(pkmn.get('id')) , 'name' : pkmn.get('name'), 'img' :  pkmn.get('img'), 'type' :  pkmn.get('type')}
		except:
			abort(404, message="Couldn't modify the element")
		#--------------------------------------------------------------------------------------------------------------------------------------------
	def delete(self,poke_id):
		try:
			pkmn = db.samples_pokemon.find_one({'_id':ObjectId(poke_id)})
			db.samples_pokemon.remove({'_id':ObjectId(poke_id)})
			return { '_id': poke_id, 'id': str(pkmn.get('id')), 'name': pkmn.get('name'), 'img':  pkmn.get('img'), 'type':  pkmn.get('type'), 'deleted': 'OK'}
		except:
			abort(404, message="Couldn't delete that element")



class pok_todos(Resource):
	def get(self):
		try:
			lista = []
			pokemons = db.samples_pokemon.find()
			for pkmn in pokemons:
				lista.append({
					#id	num	name	img	type	height	weight	candy	candy_count	egg	spawn_chance	avg_spawns	spawn_time	multipliers	weaknesses	next_evolution	prev_evolution
					'id':    str(pkmn.get('id')), # pasa a string el ObjectId
					'name': pkmn.get('name'), 
					'img':  pkmn.get('img'),
					'type':  pkmn.get('type')
					})
			return jsonify(lista)
		except:
			abort(404, message="Couldn't return the list")


	def post(self):
		
		name= request.form["name"]
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
		return { 'id' : str(new_pokemon.get('id')) , 'name' : new_pokemon.get('name'), 'img' :  new_pokemon.get('img'), 'type' :  new_pokemon.get('type'),
		'height' :  new_pokemon.get('height'),'weight' :  new_pokemon.get('weight')}


api.add_resource(pok, '/poks/<poke_id>')
api.add_resource(pok_todos, '/poks')