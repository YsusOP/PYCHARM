from flask_sqlalchemy import SQLAlchemy
import enum
from sqlalchemy.orm import relationship
db = SQLAlchemy()


albumes_cancion = db.Table('album_cancion',\
                          db.Column('album_id',db.ForeignKey('album.id'),primari_key=True),\
                          db.Column('cancion_id',db.ForeignKey('cancion.id'),primari_key=True))
class Cancion(db.Model):
    id=db.Column(db.Integer,primary_key=true)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))
    albumes = db.relationship('Album',secondary='album_cancion',back_populates='canciones')

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.titulo, self.minutos, self.segundos, self.interprete)
class Medio(enum.Enum):
    Disco =1
    Casete=2
    CD    =3

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.Disco, self.Casete, self.CD)
class Album(db.Model):
    id=db.Column(db.Integer,primary_key=true)
    titulo = db.Column(db.String(128))
    año = db.Column(db.Integer)
    descripcion = db.Column(db.String(128))
    medio =db.Column(db.Enum(Medio))
    usuario =db.Column(db.Integer,db.ForeignKey("usuario.id"))
    canciones =db.relationship
    __table_args__=(db.UniqueConstraint('usuario','titulo',name='titulo_unico_album'))
    def __repr__(self):
        return "{}-{}-{}-{}".format(self.titulo, self.año, self.descripcion, self.medio)
class Usuario(db.Model):
    id=db.Column(db.Integer,primary_key=true)
    Nombre_usuario = db.Column(db.String(128))
    contraseña = db.Column(db.String(128))
    albumes= db.realationship('Album',cascada='all,delete,delete-orphan')


    def __repr__(self):
        return "{}-{}-{}-{}".format(self.Nombre_usuario, self.contraseña, )
