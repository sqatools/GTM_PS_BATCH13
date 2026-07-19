"""
Read JSON
Read CSV
Read TXT
"""

import json

import csv


class FileReader:

    @staticmethod
    def read_json(path):

        with open(path, "r") as file:

            return json.load(file)

    @staticmethod
    def read_csv(path):

        rows = []

        with open(path, newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                rows.append(row)

        return rows

    @staticmethod
    def read_text(path):

        with open(path, "r") as file:

            return file.read()