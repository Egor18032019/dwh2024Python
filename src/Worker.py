import csv

from src.DBConnector import DBConnector


def save_data(data):
    db = DBConnector()
    db.get_all_tables()
    with open(data, 'r', newline='') as csvfile:
        spreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        isFirstLine = True
        for row in spreader:
            print(', '.join(row))
            if isFirstLine:
                isFirstLine = False
                continue
            db.insert_data(row)
