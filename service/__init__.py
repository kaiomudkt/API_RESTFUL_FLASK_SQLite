from flask import Flask


service = Flask(__name__)
service.config["DEBUG"] = True
from service.connectionDB.ConnectionDB import ConnectionDB
db = ConnectionDB()

from service.view import Aluno