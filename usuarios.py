#modulo de usuarios

def getUsuarios(mongo):
    users = mongo.db.usuarios;
    output = []
    for item in users.find():
        output.append({'Nombre': item['nombre'], 'Edad': item['edad']})
    return output
