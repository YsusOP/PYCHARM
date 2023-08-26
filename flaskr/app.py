from flaskr import create_app
from .modelos import Cancion,Medio,Album,Usuario

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    c = Cancion(titulo='prueba',minutos=2,segundos=25,interprete='Jesus')
    a = Album(Titulo='Aguilas', Año=2025, Descripcion='Lorem ipsum Lorem ipsum', medio=Medio.Disco)
    u = Usuario(Nombre_usuario='alejandro', contraseña='2948734ure')
    u.albumes.append(a)
    a.canciones.append(c)
    db.session.add(u)
    db.session.add(c)
    db.session.commit()
    print(Album.query.all())
    print(Album.query.all()[0].canciones)
    print(Cancion.query.all())
    db.session.delete(a)
    print(Album.query.all())
    print(Cancion.query.all())



