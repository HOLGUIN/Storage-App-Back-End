from flask_pymongo import PyMongo

def getConnection(app):
    app.config['MONGO_DBNAME'] = 'Prueba'
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/Prueba'
    mongo = PyMongo(app)
    return mongo
