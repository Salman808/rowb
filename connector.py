# import mysql.connector
import sqlite3
import plac
# from mysql.connector import errorcode


class conn:
    def __init__(self):
        # try:
            # self.cnx = mysql.connector.connect(user='root',
            #                           password='anjums_786',
            #                           database='chatbot', port=3306, host='localhost')
        with sqlite3.connect('chatbot') as cnx:
            print("Databse connected...")
        # except mysql.connector.Error as err:
        #     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        #         print("Something is wrong with your user name or password")
        #     elif err.errno == errorcode.ER_BAD_DB_ERROR:
        #         print("Database does not exist")
        #     else:
        #         print(err)
    def checkemail(self,email):
        with sqlite3.connect('chatbot') as cnx:
            try:
                cursor = cnx.cursor()
                query = ("SELECT *  FROM users where email ='{}'" .format(email))
                print(query)
                cursor.execute(query)
                results = cursor.fetchall()
                return len(results) > 0
            except sqlite3.Error as err:
                if err == sqlite3.DatabaseError:
                    print("Something is wrong with your user name or password")
                elif err == sqlite3.ProgrammingError:
                    print ("Database does not exist")
                else:
                    print(err)
    def signin(self,email,key):
        with sqlite3.connect('chatbot') as cnx:
            try:
                cursor = cnx.cursor()
                query = ("SELECT *  FROM users where users.email ='{}' and users.secretkey = {};" .format(email,key))
                cursor.execute(query)
                results = cursor.fetchall()
                return len(results) > 0
            except sqlite3.Connection.Error as err:
                if err.errno == sqlite3.DatabaseError:
                    print("Something is wrong with your user name or password")
                elif err.errno == sqlite3.ProgrammingError:
                    print ("Database does not exist")
                else:
                    print(err)
    def signup(self,email,username,key):
        with sqlite3.connect('chatbot') as cnx:
            try:
                cursor = cnx.cursor()
                query = ("INSERT INTO users (email,username,secretkey) VALUES (%s,%s,%s);")
                data = (email,username,str(key))
                print(query)
                cursor.execute(query,data)
                cnx.commit()
                return True
            except sqlite3.Connection.Error as err:
                cnx.rollback()
                if err.errno == sqlite3.DatabaseError:
                    print("Something is wrong with your user name or password")
                elif err.errno == sqlite3.DatabaseError:
                    print ("Database does not exist")
                else:
                    print(err)
                return False
    def fetchoffers(self):
        with sqlite3.connect('chatbot') as cnx:
            try:
                cursor = cnx.cursor()
                query = ("SELECT *  FROM offers ")
                cursor.execute(query)
                results = cursor.fetchall()
                return results
            except sqlite3.Connection.Error as err:
                if err.errno == sqlite3.DatabaseError:
                    print("Something is wrong with your user name or password")
                elif err.errno == sqlite3.DatabaseError:
                    print ("Database does not exist")
                else:
                    print(err)

