from flask import Flask, jsonify, request, Response
import mysql.connector
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect (
    host="localhost",
    user="root",
    password="",
    database="mapalexico"
)

if db.is_connected():
    print("La conexión a la base de datos se estableció correctamente")
else:    
    print("La conexión a la base de datos no se pudo establecer")

@app.route('/')
def inicio():
    return 'servidor escuchando'

@app.route('/api/comunas/<comuna>/palabras', methods=['GET'])
def obtener_palabras(comuna):
    cursor = db.cursor()
    query = "SELECT palabras FROM palabras"
    
    if comuna.lower() == 'monteria':
        query = "SELECT DISTINCT palabras FROM palabras"
        cursor.execute(query)
    else:
        query = "SELECT palabras FROM palabras WHERE comuna = %s"
        cursor.execute(query, (comuna,))
    
    palabras = [row[0] for row in cursor.fetchall()]  # Convertir a lista
    cursor.close()
    print(palabras)
    return jsonify(palabras)

@app.route('/api/palabras', methods=['POST'])
def guardar_palabras():
    data = request.json
    termino = data.get('nuevoTermino')
    comunas = data.get('comunasSeleccionadas')
    print(termino, comunas)
    if comunas and isinstance(comunas, list):
        cursor = db.cursor()

        for comuna in comunas:
            insert_query = "INSERT INTO palabras (palabras, comuna) VALUES (%s, %s)"
            values = (termino, comuna)
            cursor.execute(insert_query, values)

        db.commit()
        cursor.close()

        return jsonify({'message': 'Palabras agregadas correctamente'})

    return jsonify({'error': 'No se proporcionaron comunas seleccionadas'}), 400


@app.route('/api/terminos', methods=['GET'])
def obtener_terminos():
    cursor = db.cursor()
    query = "SELECT * FROM palabras"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()

    # Crear un diccionario anidado para almacenar los términos y sus comunas asociadas
    terminos_dict = {}
    
    for row in rows:
        palabra = row[2]
        comuna = row[1]

        # Si el término ya existe en el diccionario, agregar la comuna a la lista de comunas
        if palabra in terminos_dict:
            terminos_dict[palabra].append(comuna)
        else:
            # Si el término no existe en el diccionario, crear una nueva entrada con la comuna en una lista
            terminos_dict[palabra] = [comuna]
    
    return jsonify(terminos_dict)

@app.route('/api/palabras/editar', methods=['POST'])
def editar_palabras():
    data = request.json
    termino = data.get('palabraEditada')
    comunas = data.get('comunasSeleccionadas')
    print(termino, comunas)
    if comunas and isinstance(comunas, list):
        cursor = db.cursor()

        for comuna in comunas:
            insert_query = "INSERT INTO palabras (palabras, comuna) VALUES (%s, %s)"
            values = (termino, comuna)
            cursor.execute(insert_query, values)

        db.commit()
        cursor.close()

        return jsonify({'message': 'Palabras editada correctamente'})

    return jsonify({'error': 'No se proporcionaron comunas seleccionadas'}), 400

@app.route('/api/palabras/eliminar', methods=['POST'])
def eliminar_palabras():
    data = request.json
    termino = data.get('palabraEditada')
    comunas = data.get('comunasSeleccionadas')
    print(termino, comunas)
    
    if termino and comunas and isinstance(comunas, list):
        cursor = db.cursor()

        for comuna in comunas:
            delete_query = "DELETE FROM palabras WHERE palabras = %s AND comuna = %s"
            values = (termino, comuna)
            cursor.execute(delete_query, values)

        db.commit()
        cursor.close()

        return jsonify({'message': 'Palabras eliminadas correctamente'})

    return jsonify({'error': 'No se proporcionaron datos válidos'}), 400
