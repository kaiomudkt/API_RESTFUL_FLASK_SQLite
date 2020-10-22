from flask import Flask

service = Flask(__name__)

from service.view import Aluno

service.config["DEBUG"] = True
