import sqlite3

#connection to the database
sql_connection = sqlite3.connect("data.db")
cursor = sql_connection.cursor()

#query data based on a condition
cursor.execute("SELECT * FROM events WHERE date = '2088.10.15'")
rows = cursor.fetchall() #prints the rows that match the query
print(type(rows)) #type is a list

#qeuery ceratin collumns based on a condition
cursor.execute("SELECT band, date FROM events WHERE date = '2088.10.15'")
rows = cursor.fetchall() #prints the rows that match the query
print(rows)

#insert new rows
new_rows = [('The Beatles', 'London', '2088.10.15'), 
            ('Lions', 'Paris', '2088.10.15')]

cursor.executemany("INSERT INTO events VALUES (?, ?, ?)", new_rows)
sql_connection.commit()  #commit the changes to the database

#query the new rows
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall() #prints the rows that match the query
print(rows) 