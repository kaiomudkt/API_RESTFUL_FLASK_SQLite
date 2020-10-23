'''importa o flask'''
from flask import Flask

'''instancia o flask'''
service = Flask(__name__)
'''importa o modulo view/Aluno'''
from service.view import Aluno

'''ativo modo de depuracao'''
service.config["DEBUG"] = True
