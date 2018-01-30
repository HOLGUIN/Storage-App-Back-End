from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from conn_mongo import getConnection
from conn_mongo import getConnection
from usuarios import getUsuarios
app = Flask(__name__)

app.config["JSON_SORT_KEYS"] = False
#conexion a la base de datos de mongo
mongo =  getConnection(app);

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/api/usuarios", methods=['GET', 'POST'])
def usuariosApi():
    if request.method == 'GET':
        modelo = getUsuarios(mongo)
        return jsonify({'response': modelo})

CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == "__main__":
    print("run server")
    app.run(debug = True)
