all:
	sudo docker-compose up

build:
	sudo docker-compose build

get_todos:
	http http://localhost:5000/api/pokemons

get_uno:
	http http://localhost:5000/api/pokemons/58f56171ee9d4bd5e610d6d9
	
get_uno_mal:
	http http://localhost:5000/api/pokemons/338473893
	
borrar_uno:
	http DELETE http://localhost:5000/api/pokemons/58f56170ee9d4bd5e610d644

modificar_uno:
	http -f PUT http://localhost:5000/api/pokemons/58f56171ee9d4bd5e610d645 name="Nuevo"
	
registrar_uno:
	http -f POST http://localhost:5000/api/pokemons name="Nuevo"
	
get_todos_extra:

	curl http://localhost:5000/poks
get_uno_extra:
	curl http://localhost:5000/poks/58f56171ee9d4bd5e610d649
get_uno_extra_mal:
	curl http://localhost:5000/poks/58f56171ee9d4b

put_uno_extra:
	curl http://localhost:5000/poks/58f56171ee9d4bd5e610d649 -d name="New name " -X PUT -v

post_uno_extra:
	curl --data "name=Nuevo pokemon" --data "img=Nueva imagen" --data "type=fuego" --data "height=1.5" --data "weight=1.6" --data "candy=caramelito" POST http://localhost:5000/poks
	
delete_uno_extra:
	curl http://localhost:5000/poks/5fcd3827dfe1c704324616d6 -X DELETE -v
