create_project:
	sudo docker-compose run web django-admin startproject project .

change_ownership:
	sudo chown -R $(USER):$(USER) .
	#sudo chown -R $USER:$USER .


up:
	sudo docker-compose up

create_app:
	sudo docker-compose run web python manage.py startapp app

mi_aplicacion:
	sudo docker-compose run web python manage.py startapp mi_aplicacion

