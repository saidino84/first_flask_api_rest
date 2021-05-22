from flask import Flask
from flask_restplus import  APi

class Server():
    def __init__(self,):
        self.app=Flask(__name__)
        # self.api=App(self.app,
        #     version='1.0',title='Um api simples',
        #     description="este api foi criado de um jeitinho muito massa",
        #     doc='/docs'
        # )

    def run(self,):
        self.app.run(debug=True)

server=Server()

