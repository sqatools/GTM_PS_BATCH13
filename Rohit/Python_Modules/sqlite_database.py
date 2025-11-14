import sqlite3

def create_database_conection(db_name="Employee.db"):
    conn = sqlite3.connect(db_name)
    return conn

def create_table(con,query):
    con.execute(query)

def insert_into_table(con,query):
    con.execute(query)
    con.commit()

def select_from_tabe(con,query):
    data = con.execute(query)
    return data

connection = create_database_conection()
create_table_query = """Create table Employee(Emp_id int(10),Emp_name varchar(20),Emp_Department varchar(20),Emp_phone int(10))"""
create_table(con=connection, query=create_table_query)

insert_data_query = """Insert into Employee(Emp_id,Emp_name,Emp_Department,Emp_phone) values('4102','Rohit','CSE','9158520006')"""
insert_into_table(con=connection, query=insert_data_query)

select_data_query = """select * from Employee"""
data =select_from_tabe(con=connection , query=select_data_query)
print(data)

for value in data:
    print(value)

###################################################
#If we want insert data in bulk i.e. 50 data insertion

import sqlite3
from faker import Faker

def create_database_conection(db_name="customer_master2.db"):
    conn = sqlite3.connect(db_name)
    return conn

def create_table(con,query):
    con.execute(query)

def insert_into_table(con,query):
    con.execute(query)
    con.commit()

def select_from_tabe(con,query):
    data = con.execute(query)
    return data

connection = create_database_conection()
#create_table_query = """Create table customer_master2(Name varchar(20),email varchar(20))"""
#create_table(con=connection, query=create_table_query)

fk = Faker()
Emp_phone = 3456789982
for i in range(1,50):
    Name = fk.name()
    email = fk.email()
    insert_data_query = f"""Insert into customer_master2(Name,email) values('{Name}','{email}')"""
    insert_into_table(con=connection, query=insert_data_query)

select_data_query = """select * from customer_master2"""
data =select_from_tabe(con=connection , query=select_data_query)
print(data)

for value1 in data:
    print(value1)

