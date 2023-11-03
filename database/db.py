import sqlite3
import datetime as d

now = d.datetime.utcnow()

CREATE_GROCERIES = "CREATE TABLE IF NOT EXISTS groceries (id INT PRIMARY KEY, item TEXT, price INTEGER, date DATE);"
CREATE_HOUSEHOLD = "CREATE TABLE IF NOT EXISTS household (id INT PRIMARY KEY, item TEXT, price INTEGER, date DATE);"
CREATE_ENTERTAINMENT = "CREATE TABLE IF NOT EXISTS entertainment (id INT PRIMARY KEY, item TEXT, price INTEGER, date DATE);"
CREATE_OTHER = "CREATE TABLE IF NOT EXISTS other (id INT PRIMARY KEY, item TEXT, price INTEGER, date DATE);"

INSERT_GROCERIES = "INSERT INTO groceries (item, price, date) VALUES(?, ?, ?);"
INSERT_HOUSEHOLD = "INSERT INTO household (item, price, date) VALUES(?, ?, ?);"
INSERT_ENTERTAINMENT = "INSERT INTO entertainment (item, price, date) VALUES(?, ?, ?);"
INSERT_OTHER = "INSERT INTO other (item, price, date) VALUES(?, ?, ?);"

SELECT_ALL1 = "SELECT * FROM groceries;"
SELECT_ALL2 = "SELECT * FROM household;"
SELECT_ALL3 = "SELECT * FROM entertainment;"
SELECT_ALL4 = "SELECT * FROM other;"

SELECT_GROCERIES = "SELECT * FROM groceries WHERE item = ? AND price = ?;"
SELECT_HOUSEHOLD = "SELECT * FROM household WHERE item = ? AND price = ?;"
SELECT_ENTERTAINMENT = "SELECT * FROM entertainment WHERE item = ? AND price = ?;"
SELECT_OTHER = "SELECT * FROM other WHERE item = ? AND price = ?;"

list_db = [
    CREATE_ENTERTAINMENT,
    CREATE_GROCERIES, 
    CREATE_HOUSEHOLD, 
    CREATE_OTHER
    ]

def create_tables():
    conn = sqlite3.connect("data.db")
    with conn:
        for db in list_db:
            conn.execute(db)

# def insert_groceries(good, price, date):
#     conn = sqlite3.connect("data.db")
#     with conn
#         c = conn.cursor()
#         c.exceute(INSERT_GROCERIES, (good, price, date))
#         conn.commit()
    
# def insert_household(good, price, date):
#     conn = sqlite3.connect("data.db")
#     with conn
#         c = conn.cursor()
#         c.exceute(INSERT_HOUSEHOLD, (good, price, date))
#         conn.commit()

# def insert_entertainment(good, price, date):
#     conn = sqlite3.connect("data.db")
#     with conn
#         c = conn.cursor()
#         c.exceute(INSERT_ENTERTAINMENT, (good, price, date))
#         conn.commit()


    
    