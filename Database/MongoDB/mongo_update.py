from pymongo import MongoClient

client = MongoClient() #Localohost 27017
db = client['minicurso_python']


if __name__ == '__main__':
    #Actalizar registro, el metodo update  recibe 2 parametros, el primero seria la condicion del where y el segundo es el vaor de la actualizacion
    db.users.update({'age': 32}, {'age': 31})


    #Actalizar muchos registros, el metodo update_many  recibe 2 parametros, el primero seria la condicion del where y el segundo es el vaor de la actualizacion
    db.users.update_many({'age': 32}, {'$inc': {'age': 31}}) # con este comando incrementan la edad en 1 año en todos los registro de la condicion



