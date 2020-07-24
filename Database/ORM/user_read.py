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


if  __name__ == '__main__':
    #1
    user = User.get(User.id == 1)
    print(user)
    print()

    #2
    users = User.select() # select * from users;
    for user in users:
        print(user)

    print()

    #Select Especifico
    users = User.select(User.username, User.email) # select  username, email from users
    for user in users:
        print(user)

    print()


    #Con Where
    users = User.select().where(User.id > 2) # select  * from users where id > 2
    for user in users:
        print(user)

    print()
    #Con OrderBy
    users = User.select().order_by(User.email) # select  * from users order by email
    for user in users:
        print(user)

    print()
    print('Order by desc')
    # Order by Desc
    #users = User.select(User.username).order_by(+User.username)  # Otra  forma'
    users = User.select(User.username).order_by( User.username.desc())  # select username  from users order by  username desc'
    for user in users:
        print(user)

    print()

    # Con mas pagado a la realidasu
    users = User.select(User.username,User.email,User.password).where((User.antive == 1) and User.id > 1).order_by(User.email)  # select  username, email, password from users where antive = 1 nd id > 1 order by email
    for user in users:
        print(user)

    print()
    #Distinct
    users = User.select(User.username).distinct()  # select distinct username from users
    for user in users:
        print(user.username)

    print()
    #Count
    users = User.select(User.username).count()  # select  count(username) from users
    print(users)

    print()
    # is null
    users = User.select(User.username).where(User.email >> None)  # select username  from users where email is null
    print(users)
    for user in users:
        print(user.username)

    print()
    # is not  null se utiliza la virgurilla ~ (alt + 126)
    users = User.select(User.username).where(~User.email >> None)  # select username  from users where email is not  null
    print(users)
    for user in users:
        print(user.username)
    print()
    #Utilizacion de In
    users = ['Janer', 'jt']
    users = User.select(User.username).where(User.username << users)  # select username  from users where username in ('Janer', 'jt')
    for user in users:
        print(user)

    print()
    # Like
    users = User.select(User.username).where(User.username.contains('Janer'))  # select username  from users where username like 'Janer'
    for user in users:
        print(user)

    print()
    # Like  2
    users = User.select(User.username).where(
    User.username.startswith('j'))  # select username  from users where username like 'j%'
    for user in users:
        print(user)



    print()
    # Like 3
    users = User.select(User.username).where(User.username.endswith('t'))  # select username  from users where username like '%t'
    for user in users:
        print(user)

    print()
    # Limit
    users = User.select(User.username).limit(3)  # select username  from users where username like '%t'
    for user in users:
        print(user)


    print()
    # Limit
    users = User.select(User.username).order_by(User.id.desc()).limit(1)
    for user in users:
        print(user)

    print()
    # Si el usaurio no existe
    try:
        user = User.get(User.id == 9)
        print(user)
    except User.DoesNotExist:
        print('El usuario no existe')

    exist = User.select().where(User.id == 9).exists()
    if exist:
        print('El usuario existe')
    else:
        print('El usuario no existe')

