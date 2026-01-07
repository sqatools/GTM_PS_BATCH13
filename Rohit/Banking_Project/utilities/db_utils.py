
from ..Page_objects.Banking_website.banking_datafile import *

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
        required_keys = [
            "branch_id", "branch_name", "branch_address",
            "branch_city", "branch_state", "branch_zip", "branch_phone"
        ]

        for key in required_keys:
            if key not in branch_data:
                raise KeyError(f"Missing key in branch_data: {key}")

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

    @staticmethod
    def delete_branch_by_id(branch_id):
        conn = DBUtils.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM employee WHERE branch_id = ?",
            (branch_id,)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def branch(branch_id, branch_data):
        conn = DBUtils.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE branch
            SET
                branch_name = ?,
                branch_address = ?,
                branch_city = ?,
                branch_state = ?,
                branch_zip = ?,
                branch_phone = ?
            WHERE branch_id = ?
        """, (
            branch_data["branch_name"],
            branch_data["branch_address"],
            branch_data["branch_city"],
            branch_data["branch_state"],
            branch_data["branch_zip"],
            branch_data["branch_phone"],
            branch_id
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def create_employee_table():
        conn = DBUtils.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
            branch_id INTEGER,
            employee_id INTEGER,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            phone TEXT,
            position TEXT,
            hire_date TEXT,
            password TEXT,
            FOREIGN KEY (branch_id) REFERENCES add_branch(branch_id)
        )
        """)

        conn.commit()
        conn.close()

    @staticmethod
    def insert_employee(employee_data):
        DBUtils.create_employee_table()
        conn = DBUtils.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO employee
        (branch_id,employee_id, first_name, last_name, email, phone, position, hire_date, password)
        VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            employee_data["branch_id"],
            employee_data["employee_id"],
            employee_data["E_firstname"],
            employee_data["E_lastname"],
            employee_data["E_email"],
            employee_data["E_phone"],
            employee_data["E_position"],
            employee_data["E_hire_date"],
            employee_data["E_password"]
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def get_employee_by_id(employee_id):
        conn = DBUtils.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM employee WHERE employee_id=?",
            (employee_id,)
        )

        data = cursor.fetchone()
        conn.close()
        return data

    @staticmethod
    def delete_employee_by_id(employee_id):
        conn = DBUtils.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM employee WHERE employee_id = ?",
            (employee_id,)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def update_employee(employee_id, employee_data):
        conn = DBUtils.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE employee
        SET
            branch_id = ?,
            first_name = ?,
            last_name = ?,
            email = ?,
            phone = ?,
            position = ?,
            hire_date = ?,
            password = ?
        WHERE employee_id = ?
        """, (
            employee_data["branch_id"],
            employee_data["E_firstname"],
            employee_data["E_lastname"],
            employee_data["E_email"],
            employee_data["E_phone"],
            employee_data["E_position"],
            employee_data["E_hire_date"],
            employee_data["E_password"],
            employee_id
        ))

        conn.commit()
        conn.close()
