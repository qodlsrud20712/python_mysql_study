from mysql.connector import Error, MySQLConnection

from connection.python_mysql_dbconfig import read_db_config


def connect():
    try:
        con = MySQLConnection(host='localhost', database = 'mysql', user ='root', password ='rootroot')


        if con.is_connected():
            print('Connected to MySQL database')
            print(type(con), con)

    except Error as er:
        print(er)

    finally:
        con.close()
        print('Connection closed.')


def connect_use_config():
    db_config = read_db_config()

    try:
        print('Connection to MySQL database...')
        con = MySQLConnection(**db_config)

        if con.is_connected():
            print('connection established.')
            print(type(con),con)
        else:
            print('connection failed')

    except Error as error:
        print(error)

    finally:
        con.close()
        print('Connection closed.')