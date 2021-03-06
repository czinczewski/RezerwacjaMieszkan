import sqlite3 as sql
print("SQLite version: ", sql.version, "\n")

# --------------------------------------------------------
def create_db():
    coursor.execute('''CREATE TABLE IF NOT EXISTS client
                        (id_client INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        nickname TEXT NOT NULL,
                        name TEXT,
                        surname TEXT,
                        id_number TEXT,
                        card_number TEXT)''')
    print("Table CLIENT created successfully")

    coursor.execute('''CREATE TABLE IF NOT EXISTS city
                        (id_city INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        name TEXT NOT NULL,
                        zip_code TEXT)''')
    print("Table CITY created successfully")

    coursor.execute('''CREATE TABLE IF NOT EXISTS flat
                        (id_flat INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        availability TEXT NOT NULL,
                        start_date TEXT,
                        end_date TEXT,
                        price REAL,
                        number_of_rooms INTEGER NOT NULL,
                        amount_of_people INTEGER NOT NULL,
                        animals TEXT,
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
    print("Table RENT created successfully \n")
    db.commit()


# --------------------------------------------------------
def insert_data():
    clients = [('andrzej123', 'Andrzej', 'Dobrowolski', 'AAA 305462', '1234123412341234'),
               ('slodkajola', 'Joanna', 'Plichta', 'ABC 658942', '1235123512351235'),
               ('kubon', 'Jakub', 'Turewicz', 'FDA 652374', '4567456745674895'),
               ('rudy', 'Janusz', 'Cebula', 'CEB 154621', '5641523647895245'),
               ('karolix', 'Karol', 'Sobisz', 'GHB 564895', '5123486432165494')]
    coursor.executemany('''INSERT INTO client(nickname, name, surname, id_number, card_number)
                            VALUES (?, ?, ?, ?, ?)''', (clients))

    city = [('Gdansk', '80-404'),
            ('Sopot', '81-701'),
            ('Gdynia', '12-213'),
            ('Tokyo', '132-4315')]
    coursor.executemany('''INSERT INTO city(name, zip_code) VALUES (?, ?)''', (city))

    flats = [('YES', '2017-03-21', '2017-08-20', 120, 2, 4, 'YES', 'YES', 'YES', 1),
             ('YES', '2017-03-21', '2017-08-20', 100, 2, 3, 'YES', 'YES', 'NO', 2),
             ('YES', '2017-03-21', '2017-08-20', 30, 1, 2, 'NO', 'NO', 'NO', 1),
             ('NO', '2017-03-21', '2017-08-20', 45, 1, 2, 'YES', 'YES', 'NO', 0),
             ('YES', '2017-03-21', '2017-08-20', 36, 1, 2, 'NO', 'YES', 'NO', 0),
             ('YES', '2017-03-21', '2017-08-20', 135, 3, 7, 'YES', 'YES', 'YES', 2),
             ('NO', '2017-03-21', '2017-08-20', 500, 6, 8, 'NO', 'NO', 'YES', 3)]
    coursor.executemany('''INSERT INTO flat(availability, start_date, end_date,
                            price, number_of_rooms, amount_of_people, animals,
                            childs, parking_space, id_city)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (flats))

    rents = [(5, 4, "2017-03-22", "2017-03-30"),
             (1, 1, "2017-03-22", "2017-03-30"),
             (5, 2, "2017-04-01", "2017-04-8"),
             (13, 10, "2017-06-10", "2017-06-22")]
    coursor.executemany('''INSERT INTO rent(id_flat, id_client, start_date, end_date)
                        VALUES (?, ?, ?, ?)''', (rents))

    db.commit()


# --------------------------------------------------------
def show_data():
    coursor.execute("SELECT * FROM client")
    print("\n ID_CLIENT |    NICKNAME  |        NAME |              SURNAME |",
          " ID_NUMBER |      CARD_NUMBER |")
    for row in coursor:
        print('{:>10}'.format(row[0]), "|", '{:>12}'.format(row[1]), "|", '{:>11}'.format(row[2]), "|",
              '{:>20}'.format(row[3]), "|", '{:>10}'.format(row[4]), "|", '{:>16}'.format(row[5]), "|")

    coursor.execute("SELECT * FROM city")
    print("\n ID_CITY |       NAME |   ZIP_CODE |")
    for row in coursor:
        print('{:>8}'.format(row[0]), "|", '{:>10}'.format(row[1]), "|", '{:>10}'.format(row[2]), "|")

    coursor.execute("SELECT * FROM flat ORDER BY id_city")
    print("\n ID_FLAT | AVAILABILITY |  START_DATE |    END_DATE |   PRICE | NUMBER_OF_ROOMS",
          "| AMOUNT_OF_PEOPLE | ANIMALS | CHILDS | PARKING_SPACE | ID_CITY |")
    for row in coursor:
        print('{:>8}'.format(row[0]), "|", '{:>12}'.format(row[1]), "|", '{:>11}'.format(row[2]), "|",
              '{:>11}'.format(row[3]), "|", '{:>7}'.format(row[4]), "|", '{:>15}'.format(row[5]), "|",
              '{:>16}'.format(row[6]), "|", '{:>7}'.format(row[7]), "|", '{:>6}'.format(row[8]), "|",
              '{:>13}'.format(row[9]), "|", '{:>7}'.format(row[10]), "|")

    coursor.execute("SELECT * FROM rent")
    print("\n ID_RENT | ID_FLAT | ID_CLIENT |  START_DATE |    END_DATE |")
    for row in coursor:
        print('{:>8}'.format(row[0]), "|", '{:>7}'.format(row[1]), "|", '{:>9}'.format(row[2]), "|",
              '{:>11}'.format(row[3]), "|", '{:>11}'.format(row[3]), "|")


# --------------------------------------------------------
db = sql.connect('./database.db')
print("Connected :)")
coursor = db.cursor()

create_db()
insert_data()
show_data()

coursor.close()
db.close()
