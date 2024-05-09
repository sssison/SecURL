import sqlite3
from sqlite3 import Error
from datetime import datetime

'''
To-Do:
- Inserting Data into the Database
- Changing the Actual Value
'''

# Creating a connection with the database
def creating_connection(db):

    conn = None                             # Default
    
    try:
        conn = sqlite3.connect(db)          # Establish connection as conn
    except Error as e:
        print(e)

    return conn


def add_transaction(db, transaction_details):
    """"
    Innput: db, transaction details in ('url','date', prediction, actual)
    """
    # Initialize connection
    database = creating_connection(db)

    # Create a Cursor
    sql = ''' INSERT INTO transactions(url, date, prediction, actual) VALUES (?,?,?,?) '''

    current = database.cursor()

    # Execute the Insert Statement
    current.execute(sql, transaction_details)
    database.commit()

    database.close()

    return 

# Date should be YYYY-MM-DD HH:MM:SS.SSS
date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
add_transaction('securl_transactions.db', ('www.reddit.com',date, 0,0))