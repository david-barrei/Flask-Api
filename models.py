from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship


db = SQLAlchemy()


class Pokedex(db.Model):
    __tablename__ = 'pokedex'

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    numero: Mapped[int] = mapped_column()
    tipo: Mapped[str] = mapped_column()
    # relaciones
    evolucion = db.relationship('Evolucion')
    ataque = db.relationship('Ataque')
    Caracteristica = db.relationship('Caracteristica')

    def serializer(self):
        return{
            "id":self.id,
            "nombre":self.nombre,
            "numero":self.numero,
            "tipo":self.tipo
        }


class Evolucion(db.Model):
    __tablename__ = 'evolucion'

    id: Mapped[int] = mapped_column(primary_key=True)
    nameEvo: Mapped[str] = mapped_column(String(100),nullable=False)
    evolucion1: Mapped[str] = mapped_column()
    evolucion2: Mapped[str] = mapped_column()
    evolucion3: Mapped[str] = mapped_column()
    pokemon_id:Mapped[int]=mapped_column(ForeignKey('pokedex.id'))

    ataque = db.relationship('Ataque')


    def serializer(self):
        return{
            "id":self.id,
            "nameEvo":self.nameEvo,
            "evolucion1":self.evolucion1,
            "evolucion2":self.evolucion2,
            "evolucion3":self.evolucion3,
            "pokemon_id":self.pokemon_id
        }

class Ataque(db.Model):
    __tablename__ = 'ataque'

    id: Mapped[int] = mapped_column(primary_key=True)
    defensa:Mapped[str] = mapped_column()
    velocidad: Mapped[int] = mapped_column()
    ataque_especial:Mapped[str] = mapped_column()
    poke_id: Mapped[int]=mapped_column(ForeignKey('pokedex.id'))
    evo_id: Mapped[int]=mapped_column(ForeignKey('evolucion.id'))
    debilidad_id: Mapped[int] = mapped_column(ForeignKey('debilidad.id')) 

    debilidad = db.relationship('Debilidad')

class Debilidad(db.Model):
    __tablename__= 'debilidad'

    id:Mapped[int] = mapped_column(primary_key=True)
    debilidad1:Mapped[str] = mapped_column()
    debilidad2:Mapped[str] = mapped_column()
    debilidad3:Mapped[str] = mapped_column()

class Caracteristica(db.Model):
    __tablename__ = 'caracteristica'

    id: Mapped[int]=mapped_column(primary_key=True)
    altura: Mapped[int] = mapped_column()
    peso:Mapped[int] = mapped_column()
    sexo: Mapped[str] = mapped_column()
    habilidad:Mapped[str] = mapped_column()
    devilidad:Mapped[int] = mapped_column(ForeignKey('debilidad.id'))
    pokemon:Mapped[int] = mapped_column(ForeignKey('pokedex.id'))
    evo_id:Mapped[int] = mapped_column(ForeignKey('evolucion.id'))


 
