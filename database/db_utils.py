import pyodbc
import config


def get_string():
    server = config.server
    database = config.database
    username = config.username
    password = config.password
    result = 'DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password
    return result

def connect():
    # Задайте параметры подключения к вашей базе данных MS SQL
    server = config.server
    database = config.database
    username = config.username
    password = config.password

    # Установите соединение
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    cursor = conn.cursor()
    return cursor

    

def bonus_history(id):

    connection = pyodbc.connect(get_string(), autocommit=True)
    cursor = connection.cursor()

    # Выполните хранимую процедуру с аргументами
    # param1_value = 'some_value'
    cursor.execute("{CALL my_stored_procedure(?)}", (id,))


    cursor.close()
    connection.close()
    return cursor.fetch_all()


def bonus_balance(id):
    connection = pyodbc.connect(get_string(), autocommit=True)
    cursor = connection.cursor()

    # Выполните хранимую процедуру с аргументами
    # param1_value = 'some_value'
    cursor.execute("{CALL my_stored_procedure(?)}", (id,))


    cursor.close()
    connection.close()
    return cursor.fetch_all()


def check_user(number):
    if get_chat_id_by_number(number) is not None:
        print("Authentificated")
    else: 
        print("Not authenticated")





def get_chat_id_by_number(number):
    connection = pyodbc.connect(get_string(), autocommit=True)
    cursor = connection.cursor()

    try:
        # Create a cursor to execute SQL queries
        # cursor = conn.cursor()

        # Define your SQL query to retrieve chat_id based on the number
        query = "SELECT chat_id FROM YOUR_TABLE WHERE number = ?"
        
        # Execute the query with the provided number as a parameter
        cursor.execute(query, (number,))

        # Fetch the result (assuming there is only one row with this number)
        row = cursor.fetchone()

        if row:
            # Extract chat_id from the result
            chat_id = row[0]
            return chat_id
        else:
            return None

    except Exception as e:
        print("Error:", e)
        return None

    finally:
        # Close the cursor and database connection
        cursor.close()
        connection.close()


