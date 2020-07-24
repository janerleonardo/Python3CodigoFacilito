from pymongo import MongoClient

client = MongoClient() #Localohost 27017
db = client['minicurso_python']


if __name__ == '__main__':
    #Insertar un solo registros
    user = { 'username': 'Janer', 'age':32, 'password': '123'}
    db.user.insert(user)

    # Insertar Varios dicconarios
    user  = {'username': 'Janer', 'age': 32, 'password': '123'}
    user1 = { 'username': 'CodigoFacilito', 'age':5, 'password': '123'}
    user2 = { 'username': 'Platzi', 'age':9, 'password': '123'}

    db.user.insert_many([user,user1,user2])


    #si quieres e Id del objeto insertado

    user3 = {'username': 'Jan3r', 'age': 32, 'password': '123'}
    result = db.user.insert_one(user3) #Inserta y Retorna el Id del registro insertado