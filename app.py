from flask import Flask
from models import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///pokemon.db"
Migrate(app,db)
db.init_app(app) #establecer la coneccion con flask y sqlalchemy




if __name__=="__main__":
    app.run(host="localhost", port=5000, debug=True)









