import numpy as np
import sqlite3
def init_db():
    conn=sqlite3.connect("image_data1.db")
    cursor=conn.cursor()

    # Now we will create a table to store image data 
    cursor.execute('''CREATE TABLE IF NOT EXISTS images(id INTEGER PRIMARY KEY AUTOINCREMENT, person_name TEXT, age INTEGER, email TEXT)''')

    # Now  we will commit the changes and save the connection
    conn.commit()
    conn.close()
# Now we will initialise the dfatabase
init_db()
print("Database and Table Created Successfully")

