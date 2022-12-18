import datetime

from peewee import *
from decouple import config

db = MySQLDatabase(
    'tienda_cf',
    user='root',
    password=config('DBPASSWORD'),
    port=3306,
    host='localhost'
)

class User(Model): #Tablas, Model viene de peewee , heredamos 
    email = TextField()
    password = TextField()
    created_at = DateField(default=datetime.datetime.now) 

    class Meta: # Buena practica segun peewee es crear una clase dentro de otra clase para especificar a cual base de datos nos vamos a conectar
        database = db
        db_table = 'users'

    @classmethod
    def create_user(cls, _email, _password):
        # NUESTRO ALGORITMO DE ENCRIPTACION
        _password = 'cody_' + _password
        return User.create(email=_email, password=_password)

db.create_tables([User])