from flask import Blueprint
saludo_api = Blueprint('saludo_api',__name__)

@saludo_api.route('/')
def Api():
    return 'Apis'

@saludo_api.route('/Hola')
def hello_world():
    return 'Hello, World!'
