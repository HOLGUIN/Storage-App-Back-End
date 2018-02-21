from bson.objectid import ObjectId
#modulo de usuarios

def getUsuarios(mongo):
    users = mongo.db.usuarios;
    output = []
    for item in users.find():
        output.append({'Nombre': item['nombre'], 'Edad': item['edad']})
    return output


def postUsuario(mongo, usuario):
    _id = mongo.db.usuarios.insert(usuario)
    modelo = mongo.db.usuarios.find({"_id": ObjectId(_id)})
    return modelo
