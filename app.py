from flask import Flask, request, jsonify
from models import db,Pokedex,Evolucion
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///pokemon.db"
Migrate(app,db)
db.init_app(app) #establecer la coneccion con flask y sqlalchemy

@app.route('/pokemon',methods=['POST'])
def create_pokemon():
    pokemon = Pokedex()
    pokemon.nombre = request.json.get('nombre')
    pokemon.numero = request.json.get('numero')
    pokemon.tipo = request.json.get('tipo')

    db.session.add(pokemon)
    db.session.commit()

    return jsonify(
        {
            "message":"Usuario guardado"
        }
    ),200

@app.route('/evolucion',methods=['POST'])
def create_evolucion():
    evo = Evolucion()
    evo.nameEvo = request.json.get('nameEvo')
    evo.evolucion1 = request.json.get('evolucion1')
    evo.evolucion2 = request.json.get('evolucion2')
    evo.evolucion3 = request.json.get('evolucion3')
    evo.pokemon_id = request.json.get('pokemon_id')

    db.session.add(evo)
    db.session.commit()

    return jsonify(
        {
            "message":"Usuario guardado"
        }
    ),200



if __name__=="__main__":
    app.run(host="localhost", port=5000, debug=True)









