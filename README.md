# first_flask_api_rest
Primeiro API REST COM FLASK

>Dependecies
* Flask
* flask_restplus nao seu certo


#como rodar este aplicativo
>export FLASK_APP=main.py
>export FLASK_DEBUG=True
>export FLASK_ENV=Development

>to run with guniorn set:
>gunicorn --bind 0.0.0.0:5000 wsgi:app {no argiko wsgi.py importei esse arquivo app do modulo app/__initi__.py}