# first_flask_api_rest
Primeiro API REST COM FLASK

>Dependecies
* Flask
* flask_restplus nao seu certo


#como rodar este aplicativo
to run with FLASK
<!-- >export FLASK_APP=main.py  @deprecated version 2-->

>export FLASK_APP=wsgi:create_app
>export FLASK_DEBUG=True
>export FLASK_ENV=Development

#TO RUN WITH GUNICORN

>to run with guniorn set:
>gunicorn --bind 0.0.0.0:5000 wsgi:gunicorn_app 

{no argiko wsgi.py importei esse arquivo create_app do modulo app/__initi__.py}