from pymongo import MongoClient

client = MongoClient() #Localohost 27017
db = client['minicurso_python']


if __name__ == '__main__':
    #El Metodo delete_one recibe un parametro que es un directorio que corresponderia a la condicional
    db.users.delete_one({'age': 32})

    #El Metodo delete_many recibe un parametro que es un directorio que corresponderia a la condicional
    db.users.delete({'age': 23})


