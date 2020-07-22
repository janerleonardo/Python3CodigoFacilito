import pymysql

HOST = 'localhost'
USER = 'root'
PASSWORD = 'Sistemas$12'
DATABASE = 'minicurso_python'

USERSTABLE = """CREATE TABLE users ( 
         id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
         username VARCHAR(50) NOT NULL,
         password VARCHAR(50) NOT NULL
         )"""

DROPUSERTABLE = "DROP TABLE IF EXISTS `users`"
SHOWTABLES = "SHOW TABLES"

INSERTUSER = "INSERT INTO users (username, password) VALUES( '{username}', '{password}' );"
SELECTUSER = "SELECT * FROM users"

if __name__ == '__main__':
    connection = pymysql.connect(HOST,USER,PASSWORD,DATABASE)

    cursor = connection.cursor()

    cursor.execute(DROPUSERTABLE)
    cursor.execute(USERSTABLE)
    cursor.execute(SHOWTABLES)
    tables = cursor.fetchall()

    for table in tables:
        print(table[0])

    query = INSERTUSER.format(username='codigofacilito', password='codigo123')
    print(query)

    try:
        cursor.execute(query)
        connection.commit()
    except:
        connection.rollback()

    query = SELECTUSER
    cursor.execute(query)

    results = cursor.fetchall()
    print(results)
    for user in results:
         print( user)

    connection.close()