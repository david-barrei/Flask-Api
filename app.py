from flask import Flask, request, jsonify
from models import db,Pokedex
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///pokemon.db"
Migrate(app,db)
db.init_app(app) #establecer la coneccion con flask y sqlalchemy

@app.route('/user',methods=['POST'])
def create_user():
    user = Pokedex()
    user.nombre = request.json.get('nombre')
    user.numero = request.json.get('numero')
    user.tipo = request.json.get('tipo')

    db.session.add(user)
    db.session.commit()

    return jsonify(
        {
            "message":"Usuario guardado"
        }
    ),200

if __name__=="__main__":
    app.run(host="localhost", port=5000, debug=True)









