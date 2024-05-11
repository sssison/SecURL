import sqlite3
from sqlite3 import Error
from datetime import datetime
import pandas as pd

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

def column_to_pd(db, column):

    query = "SELECT "+column+" FROM transactions"

    database = creating_connection(db)

    df = pd.read_sql(query, database)

    return df

# Date should be YYYY-MM-DD HH:MM:SS.SSS
date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
df = column_to_pd("databases/securl_transactions.db","actual")
print(df)