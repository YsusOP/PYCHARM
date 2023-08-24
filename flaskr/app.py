from flaskr import create_app
from .modelos import Cancion

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    c = Cancion(titulo='prueba',minutos=2,segundos=25,interprete='Jesus')
    db.session.add(c)
    db.session.commit()
    print(Cancion.query.all())

with app.app_context():
    c = Medio(Disco='si',Casete='no',CD='si')
    db.session.add(c)
    db.session.commit()
    print(Medio.query.all())

with app.app_context():
    c = Album(Titulo='Aguilas',Año=2025,Descripcion='Lorem ipsum Lorem ipsum',medio=1)
    db.session.add(c)
    db.session.commit()
    print(Album.query.all())

with app.app_context():
    c = Usuario(Nombre_usuario='alejandro',contraseña='2948734ure')
    db.session.add(c)
    db.session.commit()
    print(Usuario.query.all())



