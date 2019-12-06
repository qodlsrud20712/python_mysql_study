import pandas as pd

from dml.coffee_delete import delete_product
from dml.coffee_select import query_with_fetchone, query_with_fetchall, query_with_fetchall2, \
    query_with_fetchall_by_code, query_with_fetchmany

from dml.coffee_insert import insert_product, insert_products
from dml.coffee_update import update_product

from dml.connection_pool import ConnectionPool


def connection_pool_test():
    connect_pool = ConnectionPool.get_instance()
    connection = connect_pool.get_connection()
    print('connection pool:', connect_pool)
    print('connection:', connection)


def fetch_one_test():
    print('fetchone===============')
    query_with_fetchone(sql)
    print('\nsale_table', end='\n')
    query_with_fetchone(sql_sale)


def fetch_all_test_01():
    print('fetchall1===============')
    query_with_fetchall(sql)
    print('\nsale_table', end='\n')
    query_with_fetchall(sql_sale)


def fetch_all_test_02():
    print('fetchall2===============')
    res = query_with_fetchall2(sql)
    print(type(res), 'size = ', len(res))
    for pno, pname in res:
        print(pno, pname)


def fetch_many_test():
    query_with_fetchmany(sql)
    print('\nsale_table', end='\n')
    query_with_fetchmany(sql_sale)


def delete_table_test():
    select_sql = "select code, name from product where code like 'C___'"
    res = query_with_fetchall2(select_sql)
    columns_list = ['code', 'name']
    df = pd.DataFrame(res, columns=columns_list)
    print(df)
    delete_sql = "delete from product where code = %s"
    delete_product(delete_sql, 'C004')
    for code, name in (query_with_fetchall2(select_sql)):
        print(code, "", name)


def update_table_test():
    select_sql_by_code = "select code, name from product where code = '{code}'".format(code='C001')
    query_with_fetchone(select_sql_by_code)
    update_sql = "update product set name = %s where code = %s"
    update_product(update_sql, '라떼수정', 'C001')
    query_with_fetchone(select_sql_by_code)


def insertmany_table_test():
    query_with_fetchall(sql)
    insert_products(insert_sql, products)
    query_with_fetchall(sql)


def insert_table_test():
    query_with_fetchall(sql)
    insert_product(insert_sql, 'C001', '라떼')
    query_with_fetchall(sql)


def use_where_test_02():
    print('\n where절_사용_02====================', end='\n')
    product_select_where02 = "select * from product where code = '{}'".format('A001')
    res = query_with_fetchall(product_select_where02)
    fetch_many_test()


def use_where_test_01():
    print('\n where절_사용_01====================', end='\n')
    product_select_where01 = 'select * from product where code = %s'
    res = query_with_fetchall_by_code(product_select_where01, 'A001')
    print(res)


def options():
    global sql, sql_sale, insert_sql, products
    sql = 'select * from product'
    sql_sale = 'select * from sale'
    insert_sql = 'insert into product values(%s, %s)'
    products = [('C002', '라떼2'), ('C003', '라떼3'), ('C004', '라떼4')]


if __name__ == '__main__':
    connection_pool_test()
    options()

    # fetch_one_test()
    # print()
    # fetch_all_test_01()
    # print()
    # fetch_all_test_02()

    # use_where_test_01()
    #
    # use_where_test_02()
    #
    # insert_table_test()
    #
    # insertmany_table_test()
    #
    # update_table_test()
    #
    # delete_table_test()