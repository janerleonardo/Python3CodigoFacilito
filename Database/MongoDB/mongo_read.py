from pymongo import MongoClient

client = MongoClient() #Localohost 27017
db = client['minicurso_python']


if __name__ == '__main__':
    #Obtener todos los registros
    users = db.users.find()
    for user in users:
        print(user)

    #Obtener un datos especifico (where)
    users = db.users.find({'age': 32}) #el where se debe manejar como un diccionary
    for user in users:
        print(user)


    #And y OR (where)
    users = db.users.find({"$and":[{"age": 32}, {"username": "Janer"}]}) #el where se debe manejar como un diccionary, donde haya un llave $and y que sea igual a una lista de dicionary
    for user in users:
        print(user)

    # Limit
    users = db.users.find().limit(2)
    for user in users:
        print(user)

    # Count
    num_users = db.users.find().count()
    print(num_users)


    # find_one() Reotrna un solo registros
    user = db.users.find_one({'age': 3})
    print(user)



