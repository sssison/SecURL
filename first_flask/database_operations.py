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

    database.close()

    return df

def update_database(db, url):
    """
    The function `update_database` retrieves the latest transaction prediction for a given URL from a
    database, toggles the prediction value, and updates the database with the new prediction.
    
    :param db: The `db` parameter in the `update_database` function is likely a database connection
    object or a path to the database file. It is used to establish a connection to the database where
    the transactions are stored. The function then queries the database to retrieve the latest
    transaction ID and prediction for a given URL
    :param url: The function `update_database` takes two parameters: `db` which represents the database
    connection and `url` which is the URL used to query the database for the latest transaction
    prediction
    :return: The function `update_database` does not explicitly return any value. It updates the
    prediction value in the database for a specific transaction based on the provided URL.
    """
    
    database = creating_connection(db)

    query_id = "SELECT transaction_id, prediction from transactions WHERE url = \'"+url+"\' ORDER BY date DESC LIMIT 1"

    current = database.cursor()

    # Execute the Insert Statement
    current.execute(query_id)

    records = current.fetchall()

    query_update = "UPDATE transactions SET prediction = ? WHERE transaction_id = ?"

    for row in records:
        trans_id = row[0]
        current_prediction = row[1]

    new_prediction = 1 if (current_prediction == 0) else 0

    # Execute the Update Statement
    current.execute(query_update, (new_prediction, trans_id))
    database.commit()

    database.close()

    return



# Date should be YYYY-MM-DD HH:MM:SS.SSS
# date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')