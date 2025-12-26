import sqlite3
from ..Page_objects.Banking_website.banking_datafile import *
'''
class DBUtils:

    def create_database_connection(self,db_name="Bank.db"):
        self.conn = sqlite3.connect(db_name)
        return self.conn


    def create_Add_branch_table(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()
        cursor.close()


    def insert_branch(self,data):
        conn = DBUtils.create_database_connection(db_name="Bank.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO branch 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, data)

        conn.commit()
        conn.close()
'''

import sqlite3

class DBUtils:

    DB_NAME = "bank.db"

    @staticmethod
    def get_connection():
        return sqlite3.connect(DBUtils.DB_NAME)

    @staticmethod
    def create_branch_table():
        conn = DBUtils.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS add_branch (
            branch_id INTEGER PRIMARY KEY,
            branch_name TEXT,
            branch_address TEXT,
            branch_city TEXT,
            branch_state TEXT,
            branch_zip TEXT,
            branch_phone TEXT
        )
        """)

        conn.commit()
        conn.close()

    @staticmethod
    def insert_branch(branch_data):
        conn = DBUtils.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO add_branch 
        (branch_id, branch_name, branch_address, branch_city, branch_state, branch_zip, branch_phone)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            branch_data["branch_id"],
            branch_data["branch_name"],
            branch_data["branch_address"],
            branch_data["branch_city"],
            branch_data["branch_state"],
            branch_data["branch_zip"],
            branch_data["branch_phone"]
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def get_branch_by_id(branch_id):
        conn = DBUtils.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM add_branch WHERE branch_id=?",
            (branch_id,)
        )
        data = cursor.fetchone()

        conn.close()
        return data
