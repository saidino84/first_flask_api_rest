# from flask import Flask

from flask import Flask
from app.controllers.book import book

# app=Flask(__name__)
# app.register_blueprint(book)

# @app.route('/')
# def index():
#     return 'Hello world'

def create_app():
    app=Flask(__name__)
    # app.register_blueprint(book)
    @app.route('/', methods=["GET",'POST'])
    def index():
        print('Running app with creta_app')
        return 'Hello boys'
    return app



if __name__ == '__main__':
    app=create_app()

'segunda part'