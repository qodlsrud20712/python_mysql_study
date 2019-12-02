from mysql.connector import Error, MySQLConnection


try:
    con = MySQLConnection(host='localhost', database = 'mysql', user ='root', password ='rootroot')

    print(con)

except Error as er:
    print(er)