from pymongo import MongoClient
import re

client = MongoClient() #Localohost 27017
db = client['minicurso_python']


if __name__ == '__main__':
    regex = re.compile('Janer') # LIKE %Janer%
    users = db.users.find({'username': regex})
    for user in users:
        print(user)


    regex = re.compile('^C') # LIKE %C
    users = db.users.find({'username': regex})
    for user in users:
        print(user)


    regex = re.compile('r$') # LIKE r%
    users = db.users.find({'username': regex})
    for user in users:
        print(user)


