from flask import Flask, render_template
from pymongo import MongoClient

# Inicializar la aplicación Flask
app = Flask(__name__)

# Conectar a MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Asegúrate de tener MongoDB corriendo localmente
db = client["miBaseDeDatos"]  # Crear o usar una base de datos llamada 'miBaseDeDatos'
coleccion = db["personas"]  # Crear o usar una colección llamada 'personas'

# Ruta principal de la aplicación
@app.route('/')
def index():
    # Consultar los datos en MongoDB
    personas = coleccion.find()  # Esto obtiene todos los documentos de la colección 'personas'
    
    # Pasar los datos a la plantilla
    return render_template('index.html', personas=personas)

if __name__ == '__main__':
    app.run(debug=True)
