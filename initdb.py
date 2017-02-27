import sqlite3

connection = sqlite3.connect('database.db')
print ('Opened database successfully')

connection.execute('CREATE TABLE movie (name TEXT, releaseyear INTEGER)')
print ('Table created successfully')

connection.close()
