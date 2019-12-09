from dml.coffee_select import query_with_fetchall
from dml_ddl_blob.blob_query import insert_blob, read_blob, update_blob, delete_blob
from dml_ddl_blob.blob_read_write import read_file_blob
from dml_ddl_blob.create_table_blob import create_table

if __name__ == '__main__':
    create_table()
    data = read_file_blob('img/python-logo.png')
    print(type(data))

    insert_query = "INSERT INTO images (name, pic) VALUES(%s, %s)"
    update_query = "UPDATE images SET name = %s, pic= %s WHERE no = %s"
    read_query = "SELECT pic FROM images WHERE no = %s"
    delete_query = "DELETE from images where no =%s"
    select_query = "select no, name from images"

    insert_blob(insert_query, 'python-logo', 'img/python-logo.png')
    insert_blob(insert_query, 'google-logo', 'img/google-logo.png')
    query_with_fetchall(select_query)
    print()

    read_blob(read_query, 1, 'img/read_python.png')
    read_blob(read_query, 2, 'img/read-google.png')

    update_blob(update_query, 'pycharm-logo', 'img/pycharm-logo.png', 1)
    query_with_fetchall(select_query)
    print()
    read_blob(read_query, 1, 'img/read-pycharm.png')

    delete_blob(delete_query, 1)
    query_with_fetchall(select_query)