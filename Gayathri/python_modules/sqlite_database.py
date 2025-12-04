import sqlite3

from faker import Faker


#create a database connection
def create_database_connect(db_name="school.db"):
    conn = sqlite3.connect(db_name)
    return conn

#above database is cerated, now lets create a table
def create_tables(conn,query):
    conn.execute(query)

#after creating table - elts insert the data
def insert_query(conn,query):
    conn.execute(query)
    conn.commit() #commiting whatever data we are inserting into table

#get teh data from the table for whatver data is inserted
def select_query(conn,query):
    data = conn.execute(query)
    return data

connection = create_database_connect()
# create_table_query = """create table student(name char[10], email char[10], phone int)"""
#
# #call the method now
# create_tables(conn = connection, query=create_table_query)
#
# insert_data_query = """insert into student(name, email, phone) values ('gayathri', 'gayathri@gmail.com', '123456')"""
# insert_query(conn = connection, query= insert_data_query)

# #to check if data is inserted properly - so use select query
select_qury_data = """select * from student"""
data = select_query(conn=connection, query=select_qury_data)
print(data)
for value in data:
     print(value)

"""triple quotes - we can use doubel quotes, but with string formatting and multi line
better to have triple quotes"""

#now if we want to inssert 50 records its not possible to add them manually
#so we make use of the faker module

#insert bulk data
connection = create_database_connect()
#table is already created aboive - so no need to create again
# create_table_query = """create table student(name char[10], email  char[10], phone int)"""
# create_table(con=connection, query=create_table_query)

fk = Faker() #create object for Faker
phone = 35435438989
for i in range(1,50):
    username = fk.user_name()
    email = fk.email()
    #phone = fk.phone_number() #this will generate additional sepcial character liek +
    #we want to avoid that - so hav defined the phon number above and will increment that
    phone += 1
    insert_data_query = f"""insert into student(name,email,phone) values ('{username}','{email}','{phone}')"""
    insert_query(conn=connection, query=insert_data_query)


select_qury_data = """select * from student"""
data = select_query(conn=connection, query=select_qury_data)
print(data)
for value in data:
    print(value)










