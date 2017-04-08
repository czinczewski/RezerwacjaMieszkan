import sqlite3 as sql
print("SQLite version: ", sql.version, "\n")
import datetime     # datestamp
import random       # real data


# --------------------------------------------------------
def create_db():
    coursor.execute('''CREATE TABLE IF NOT EXISTS client
                        (id_client INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        nickname TEXT NOT NULL,
                        name TEXT,
                        surname TEXT,
                        id_number TEXT,
                        card_number REAL)''')
    print("Table CLIENT created successfully")

    coursor.execute('''CREATE TABLE IF NOT EXISTS city
                        (id_city INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        name TEXT NOT NULL,
                        zip_code TEXT)''')
    print("Table CITY created successfully")

    coursor.execute('''CREATE TABLE IF NOT EXISTS flat
                        (id_flat INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        availabity INTEGER NOT NULL,
                        start_date TEXT,
                        end_date TEXT,
                        price REAL,
                        number_of_rooms INTEGER NOT NULL,
                        amount_of_people INTEGER NOT NULL,
                        animalas TEXT,
                        childs TEXT,
                        parking_space TEXT,
                        id_city INTEGER REFERENCES city(id_city))''')
    print("Table FLAT created successfully")

    coursor.execute('''CREATE TABLE IF NOT EXISTS rent
                        (id_rent INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        id_flat INTEGER REFERENCES flat(id_flat),
                        id_client INTEGER REFERENCES client(id_client),
                        start_date TEXT,
                        end_date TEXT)''')
    print("Table RENT created successfully")


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
# --------------------------------------------------------
db = sql.connect('./database.db')
coursor = db.cursor()

create_db()
data = read_data_from_txt()

db.close()
