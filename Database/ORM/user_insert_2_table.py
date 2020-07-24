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
    user = peewee.ForeignKeyField(User, primary_key=True)
    name = peewee.CharField(max_length=50)
    address = peewee.TextField()
    active = peewee.BooleanField(default=True)
    create_date = peewee.DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = database
        db_table = 'stores'

    def __str__(self):
        return f' Usuario : {self.user}, Name: {self.name}, Activo : {self.active}, Address: {self.address} '

if __name__ == '__main__':
    if not Store.table_exists():
        Store.create_table()
    else:
        #Store.drop_table()
        #Store.create_table()
        pass

    #user = User.create(username='Platzi3', password='Master', email='platzi@gmail.com')

    #Creacion por e save()
    store = Store()
    store.user_id = 2
    store.name = 'Pruebas3'
    store.address= 'Pruebas1'
    store.save(force_insert=True)

    store = Store.create(name='Tienda3', address='Pruebas3', user_id=3)
