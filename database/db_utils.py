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

    try:

        # Выполните хранимую процедуру с аргументами
        # param1_value = 'some_value'
        cursor.execute("{CALL proc_hist_bonus_pokupatel(?)}", (id,))
        return cursor.fetchall()
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        connection.close()


def bonus_balance(chat_id):
    connection = pyodbc.connect(get_string(), autocommit=True)
    cursor = connection.cursor()
    id = get_id_by_chat_id(chat_id)
    try:
        # Выполните хранимую процедуру с аргументами
        # param1_value = 'some_value'
        cursor.execute("{CALL proc_bonus_pokupatel(?)}", (id,))
        return cursor.fetchone()[0]
    
    except Exception as e:
        print(e)
    
    finally:
        cursor.close()
        connection.close()
    


def check_user(number):
    if get_chat_id_by_number(number) is not None:
        return True
    else: 
        return False


def create_user(number, chat_id):
    connection = pyodbc.connect(get_string(), autocommit=True)
    cursor = connection.cursor()
    try: 
        
        query = "INSERT INTO new_users VALUES(?, ?)"

        cursor.execute(query, (chat_id, number))
    
    except Exception as e:
        print("Error:", e)
        return None

    finally:
        # Close the cursor and database connection
        cursor.close()
        connection.close()
     


def get_chat_id_by_number(number):
    connection = pyodbc.connect(get_string(), autocommit=True)
    cursor = connection.cursor()

    try:
        # Create a cursor to execute SQL queries
        # cursor = conn.cursor()

        # Define your SQL query to retrieve chat_id based on the number
        query = "SELECT TelegramId FROM Pokupatel WHERE TelegramNumber =?"
        
        # print(number)
        # Execute the query with the provided number as a parameter
        cursor.execute(query, str(number))
        # Fetch the result (assuming there is only one row with this number)
        row = cursor.fetchone()
        # print(row)


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



def check_user_by_chat_id(chat_id):
    connection = pyodbc.connect(get_string(), autocommit=True)
    cursor = connection.cursor()

    try:
        # Create a cursor to execute SQL queries
        # cursor = conn.cursor()

        # Define your SQL query to retrieve chat_id based on the number
        # Select TelegramId, TelegramNumber from Pokupatel where TelegramNumber=79266390551;
        query = "Select TelegramNumber from Pokupatel WHERE TelegramId=" + str(chat_id)
        
        # Execute the query with the provided number as a parameter
        cursor.execute(query)

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


def get_chat_id_by_number(number):
    connection = pyodbc.connect(get_string(), autocommit=True)
    cursor = connection.cursor()

    try:
        # Create a cursor to execute SQL queries
        # cursor = conn.cursor()

        # Define your SQL query to retrieve chat_id based on the number
        query = "SELECT TelegramId FROM Pokupatel WHERE TelegramNumber =?"
        
        # print(number)
        # Execute the query with the provided number as a parameter
        cursor.execute(query, str(number))
        # Fetch the result (assuming there is only one row with this number)
        row = cursor.fetchone()
        # print(row)


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



def get_id_by_chat_id(chat_id):
    connection = pyodbc.connect(get_string(), autocommit=True)
    cursor = connection.cursor()

    try:
        # Create a cursor to execute SQL queries
        # cursor = conn.cursor()

        # Define your SQL query to retrieve chat_id based on the number
        # Select TelegramId, TelegramNumber from Pokupatel where TelegramNumber=79266390551;
        query = "Select id from Pokupatel WHERE TelegramId=" + str(chat_id)
        
        # Execute the query with the provided number as a parameter
        cursor.execute(query)

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


def get_codes():
    connection = pyodbc.connect(get_string(), autocommit=True)
    cursor = connection.cursor()
    try:
        query = "Select pokupatelId, code, send_date from bot_confirmation_code" #where send_date=NULL
        cursor.execute(query)
        return cursor.fetchall()
                

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()



def get_chat_id_by_id(chat_id):
    connection = pyodbc.connect(get_string(), autocommit=True)
    cursor = connection.cursor()

    try:
        # Create a cursor to execute SQL queries
        # cursor = conn.cursor()

        # Define your SQL query to retrieve chat_id based on the number
        # Select TelegramId, TelegramNumber from Pokupatel where TelegramNumber=79266390551;
        query = "Select TelegramId from Pokupatel WHERE id=" + str(chat_id)
        
        # Execute the query with the provided number as a parameter
        cursor.execute(query)

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



def update_timestamp(id):
    connection = pyodbc.connect(get_string(), autocommit=True)
    cursor = connection.cursor()

    try:
        query = "Update bot_confirmation_code Set send_date=CURRENT_TIMESTAMP Where pokupatelId=" + str(id)
        cursor.execute(query)

    except Exception as e:
        print("Error:", e)
        return None

    finally:
        # Close the cursor and database connection
        cursor.close()
        connection.close()


def get_broadcast():
    connection = pyodbc.connect(get_string(), autocommit=True)
    cursor = connection.cursor()
    try:
        query = "Select pokupatelId, send_date, body, image  from bot_broadcaster" #where send_date=NULL
        cursor.execute(query)
        return cursor.fetchall()
                

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


def update_timestamp_for_broadcast(id):
    connection = pyodbc.connect(get_string(), autocommit=True)
    cursor = connection.cursor()

    try:
        query = "Update bot_broadcaster Set send_date=CURRENT_TIMESTAMP Where pokupatelId=" + str(id)
        cursor.execute(query)

    except Exception as e:
        print("Error:", e)
        return None

    finally:
        # Close the cursor and database connection
        cursor.close()
        connection.close()