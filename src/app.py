from flask import Flask
import sys
from Prueba.saludo import saludo_api
app = Flask(__name__)
app.register_blueprint(saludo_api)

@app.errorhandler(404)
def page_not_found(e):
	""" """
    return "Lol Error"
if __name__ == '__main__':
	app.run(debug = True,port = 4000)
