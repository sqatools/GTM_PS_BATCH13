import sqlite3
from faker import Faker


def create_database_connect(db_name="school.db"):
    conn = sqlite3.connect(db_name)
    return conn


def create_table(con, query):
    con.execute(query)


def insert_query(con, query):
    con.execute(query)
    con.commit()


def select_query(con, query):
    data = con.execute(query)
    return data


connection = create_database_connect()
create_table_query = """create table student(name char[10], email  char[10], phone int)"""
create_table(con=connection, query=create_table_query)

insert_data_query = """insert into student(name, email, phone) values('Rohan', 'rohan@gmail.com', 56546456456)"""
insert_query(con=connection, query=insert_data_query)
select_data_query = """select * from student"""
data = select_query(con=connection, query=select_data_query)
print(data)
for value in data:
    print(value)

# insert bulk data

#connection = create_database_connect()
create_table_query = """create table student(name char[10], email  char[10], phone int)"""
create_table(con=connection, query=create_table_query)

#fk = Faker()
#phone = 35435438989
#for i in range(1, 50):
 #   username = fk.user_name()
  #  email = fk.email()
   # phone += 1
   # insert_data_query = f"""insert into student(name, email, phone) values('{username}', '{email}', {phone})"""
   # insert_query(con=connection, query=insert_data_query)






select_data_query = """select * from student"""
data = select_query(con=connection, query=select_data_query)
print(data)
for value in data:
    print(value)




