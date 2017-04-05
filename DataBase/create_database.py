import sqlite3 as sql
print("sqllite3 version: ", sql.version)
import datetime     # datestamp
import random       # real data


db = sql.connect('./database.db')
coursor = db.cursor()


# --------------------------------------------------------
def create_db():
    coursor.execute('CREATE TABLE IF NOT EXISTS try(inx REAL, datestamp TEXY, keyword TEXT, value REAL)')


# --------------------------------------------------------
def read_data_from_txt():
    print("Reading data from .txt file")
    data = []
    return data

# # --------------------------------------------------------
# def data_entry(data):
#     print("Dodaje dane")
#     coursor.execute("INSERT INTO try VALUES(1545564, '2016-01-01', 'Python', 5)")
#     db.commit()
#     coursor.close()
#     db.close()


create_db()
data = read_data_from_txt()
