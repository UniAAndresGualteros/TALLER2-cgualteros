from flask import Flask, jsonify, render_template
from models.main import obtener_sonido_por_animal,obtener_sonidos

app = Flask(__name__)

@app.route('/api/sonidos', methods=['GET'])
def get_sonidos():
    sonidos = obtener_sonidos()
    return jsonify(sonidos)

@app.route('/api/sonidos/<string:nombre_animal>', methods=['GET'])
def get_sonido(nombre_animal):
    sonido = obtener_sonido_por_animal(nombre_animal)
    if sonido is None:
        return jsonify({'error': 'Animal no encontrado'}), 404
    return jsonify({nombre_animal: sonido})

@app.route('/')
def index():
    return render_template('index.html', sonidos=obtener_sonidos())

if __name__ == '__main__':
    app.run(debug=True)