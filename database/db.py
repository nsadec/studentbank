import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def create_table(conn,table,column):
    cursor = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS {} ({}) ".format(table, column)
    print(query)
    try:
        cursor.execute(query)
    except Exception as e:
        print("Something went wrong, Details: {}".format(e))
    else:
        conn.commit()
        print("A Table created successfully")

def select_data(conn,column, table, condition=None, fetchall=False):
    cursor = conn.cursor()
    query = "SELECT {} FROM {} ".format(column, table)
    if condition is not None:
        query += "WHERE {}".format(condition)
        print(query)
    try:
        cursor.execute(query)
    except Exception as e:
        print("Something went wrong, Details: {}".format(e))
    else:
        if fetchall:
            result = cursor.fetchall()
            return result
        else:
            result = cursor.fetchone()
            return result

def insert_date(conn,table, column, value):
    cursor = conn.cursor()
    query = "INSERT INTO {} ({}) VALUES ({}) ".format(table, column, value)
    print(query)
    try:
        cursor.execute(query)
    except Exception as e:
        print("Something went wrong, Details: {}".format(e))
    else:
        conn.commit()
        print("A row has been inserted successfully")

def update_data(conn,table,column, condition=None):
    cursor = conn.cursor()
    query = 'UPDATE {} SET {} ' .format(table,column)
    if condition is not None:
        query+='WHERE {}'.format(condition)
        print(query)
    try:
        cursor.execute(query)
    except Exception as e:
        print("Something went wrong, Details: {}".format(e))
    else:
        conn.commit()
def delete_data(conn,table, condition):
    cursor = conn.cursor()
    query = 'DELETE FROM {} WHERE {}'.format(table, condition)
    print(query)
    try:
        cursor.execute(query)
    except Exception as e:
        print("Something went wrong, Details: {}".format(e))
    else:
        conn.commit()