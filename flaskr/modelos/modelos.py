from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Cancion(db.Model):
    id=db.Column(db.Integer,primary_key=true)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.titulo, self.minutos, self.segundos, self.interprete)
class Medio(db.Model):
    id=db.Column(db.Integer,primary_key=true)
    Disco= db.Column(db.String(128))
    Casete = db.Column(db.String(128))
    CD = db.Column(db.String(128))

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.Disco, self.Casete, self.CD)
class Album(db.Model):
    id=db.Column(db.Integer,primary_key=true)
    titulo = db.Column(db.String(128))
    año = db.Column(db.Integer)
    descripcion = db.Column(db.String(128))
    medio =Column(Integer, ForeignKey('Medio.id'))

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.titulo, self.año, self.descripcion, self.medio)
class Usuario(db.Model):
    id=db.Column(db.Integer,primary_key=true)
    Nombre_usuario = db.Column(db.String(128))
    contraseña = db.Column(db.String(128))


    def __repr__(self):
        return "{}-{}-{}-{}".format(self.Nombre_usuario, self.contraseña, )