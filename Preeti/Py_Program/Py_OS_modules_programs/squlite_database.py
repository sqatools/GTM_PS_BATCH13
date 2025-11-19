import sqlite3
import faker_module
from multiprocessing import connection


def create_databse_connect(db_name="school.db"):
    conn = sqlite3.connect(db_name)
    return conn
def create_table(con,query):
    con.exceute_query(query)

def insert_query(con,query):
    con.exceute_query(query)
    con.commit()

def select_query(con,query):
    data=con.execute_query(query)
    return data

con=create_databse_connect()
create_table_query="""create table student(name char[10],email char[10],phone int)"""
create_table(con=connection, query=create_table_query)

