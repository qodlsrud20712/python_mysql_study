import inspect
from connection_pool.connection_pool_study02 import ExplicitlyConnectionPool, get_implicitly_connection


def explicitly_connection_pool():
    print('\n == {}()=='.format(inspect.stack()[0][3]))
    connectionPool = ExplicitlyConnectionPool.get_instance()
    print(type(connectionPool), connectionPool)
    connection = connectionPool.get_connection()
    print(type(connection), connection)
    connection.close()

def implicitly_connection_pool():
    print('\n == {}()=='.format(inspect.stack()[0][3]))
    connectionPool = get_implicitly_connection()
    print(type(connectionPool), connectionPool)
    connection = connectionPool.get_connection()
    connection.close()

if __name__ == '__main__':
    explicitly_connection_pool()
    implicitly_connection_pool()

    explicitly_connection_pool()
    implicitly_connection_pool()