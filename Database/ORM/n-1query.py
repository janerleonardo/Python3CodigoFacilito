import peewee
import datetime

HOST = 'localhost'
USER = 'root'
PASSWORD = 'Sistemas$12'
DATABASE = 'minicurso_python'


database = peewee.MySQLDatabase(DATABASE, host=HOST, port=3306, user=USER, password=PASSWORD)

class User (peewee.Model):
    username = peewee.CharField(unique=True, max_length=50, index=True)
    password =peewee.CharField(max_length=50)
    email = peewee.CharField(max_length=50, null=True)
    antive = peewee.BooleanField(default=True)
    create_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'users'

    def __str__(self):
        return f' {self.username}, {self.email}, {self.antive}, {self.password}'

class Store(peewee.Model):
    user = peewee.ForeignKeyField(User, primary_key=True) # Esto hace una Realacion 1 a 1, se le pasa la clase y el parametro primary_key=True
    name = peewee.CharField(max_length=50)
    address = peewee.TextField()
    active = peewee.BooleanField(default=True)
    create_date = peewee.DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = database
        db_table = 'stores'

    def __str__(self):
        return f' Usuario : {self.user}, Name: {self.name}, Activo : {self.active}, Address: {self.address} '

class Client(peewee.Model):
    store = peewee.ForeignKeyField(Store,related_name='stores') # Esto es una relacion de 1 a muchos
    name = peewee.CharField(max_length=50)
    active = peewee.BooleanField(default=True)
    create_date = peewee.DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = database
        db_table = 'clients'
    def __str__(self):
        return f'Cliente :{self.name}, Active: {self.active}'

class Product(peewee.Model):
    name = peewee.CharField(max_length=100)
    description = peewee.TextField()
    store = peewee.ForeignKeyField(Store,related_name='products')
    price = peewee.DecimalField(max_digits=5,decimal_places=2) #100.00
    stock = peewee.IntegerField()
    create_date= peewee.DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = database
        db_table = 'products'

    def __str__(self):
        return f'Produtos {self.name}, Descripcion {self.description}, store {self.price}'

if __name__ == '__main__':
    #Product.drop_table() #Elimina la tabla productos
    #Product.create_table() # crear la tabla
    #Product.create(store_id=1, name='Pan', description = 'Pan Integral', price = 5.5, stock= 30)
    #Product.create(store_id=1, name='Leche', description = 'Leche', price = 15.5, stock= 20)
    #Product.create(store_id=1, name='Te', description = 'Te helado', price = 1.5, stock= 30)


    #Product.create(store_id=2, name='Jamon', description = 'Jamo de Pavo', price = 30.45, stock= 30)
    #Product.create(store_id=2, name='Huevos', description = 'Huevos AAA', price = 10.30, stock= 20)
    #Product.create(store_id=2, name='Queso', description = 'Queso costeño', price = 6.87, stock= 30)

    products = Product.select().where(Product.store_id == 1)
    for product in products:
        print(product)


