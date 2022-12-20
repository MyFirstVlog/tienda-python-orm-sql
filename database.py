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

class Product(Model): #Tablas, Model viene de peewee , heredamos 
    name = TextField()
    price = IntegerField()
    user = ForeignKeyField(User, backref='products') #El backref permitira que un usuario pueda acceder a sus productos, un usuario tiene muchos productos
    created_at = DateField(default=datetime.datetime.now) 

    @property
    def price_format(self):
        return f"{self.price // 100} doláres"
    class Meta: # Buena practica segun peewee es crear una clase dentro de otra clase para especificar a cual base de datos nos vamos a conectar
        database = db
        db_table = 'products'

db.create_tables([User, Product])

#Migraciones permiten modificar la tabla sin tener que borrarla previamente al agregar un atributo nuevo a la tabla