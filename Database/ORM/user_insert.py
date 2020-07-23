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

if  __name__ == '__main__':
    if not User.table_exists():
        User.create_table()
    else:
        #Delete Registros
        query = User.delete()
        query.execute()
        #Tambien pude Utilizar el metodos User.drop_table(), para borrar la tabla
        #User.drop_table()


    # Primera forma de crear un usuario
    user = User()
    user.username = 'Leonardo Tegue'
    user.password = 'janer.l'
    user.email = 'l@devapp.com.co'
    user.save()

    #Segunda forma seria
    user = User(username='Janer', password='13456', email='info@devapp.com.co')
    user.save()


    #Se le puede envia un diccionario
    user = {'username': 'jt', 'password': 'Pruebas'}
    user = User(**user)
    user.save()

    #Se pued enviar metodos de clase de nombre Create
    user = User.create(username= 'Codigo', password='Facilito')

    #Utilizando el Metodo Insert (Genera un Query
    query = User.insert(username='Platzi', password='123')
    print(query) # INSERT INTO `users` (`username`, `password`, `antive`, `create_date`) VALUES ('Platzi', '123', 1, '2020-07-22 12:49:14.795480')
    query.execute()

