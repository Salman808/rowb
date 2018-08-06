import sqlite3

class DB :
    def __init__(self):
        try:
            conn = sqlite3.connect('chatbot')
            print ("Opened database successfully")
            conn.execute('''CREATE TABLE IF NOT EXISTS users
                         (ID INT PRIMARY KEY     NOT NULL,
                         username           TEXT    NOT NULL,
                         email            CHAR(50)     NOT NULL,
                         secretkey        CHAR(50));''')
            print("user table created successfully")
            conn.execute('''CREATE TABLE IF NOT EXISTS offers
                                 (ID INT PRIMARY KEY     NOT NULL,
                                 offer_desc           TEXT    NOT NULL,
                                 price            CHAR(50)     NOT NULL);''')
            print("offers table created successfully")
            conn.close()
        except:
            print("Database already created...")