from flask import Flask, jsonify, render_template
from flask_cors import CORS
from conn_mongo import getConnection

app = Flask(__name__)


#conexion a la base de datos de mongo
mongo =  getConnection(app);


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/api/usuarios", methods=['Get'])
def getusuarios():
    users = mongo.db.usuarios;
    output = []
    print ("realizaron una peticion")
    for s in users.find():
        output.append({'nombre': s['nombre'], 'edad': s['edad']})

    return jsonify({'response': output})

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == "__main__":
    print("run server")
    app.run(debug = True)
