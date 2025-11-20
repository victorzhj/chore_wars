from config_db_connection import Config

conn = Config().create_connection()

def get_username(username):
    """
    Fetch a user by username. Used to check if a user exists during registration.
    """
    cursor = conn.cursor()
    query = "SELECT * FROM Users WHERE username = %s"
    cursor.execute(query, (username))
    result = cursor.fetchone()
    cursor.close()
    return result

def create_user(user_data):
    """
    Create a new user in the database.
    """
    cursor = conn.cursor()
    insert_query = "INSERT INTO Users (username, user_password, nickname) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (user_data['username'], user_data['password'], user_data['nickname']))
    conn.commit()
    cursor.close()
    return

def login_user(username, password):
    """
    Authenticate a user with username and password.
    """
    cursor = conn.cursor()
    query = "SELECT * FROM Users WHERE username = %s AND user_password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    cursor.close()
    return result

def get_user_points(user_id):
    """
    Retrieve the points of a user by their ID.
    """
    cursor = conn.cursor()
    query = "SELECT points FROM Users WHERE user_id = %s"
    cursor.execute(query, (user_id))
    result = cursor.fetchone()
    cursor.close()
    return result

def modify_user_settings(user_id, modified_settings):
    return

def modify_user_points(user_id, points):
    """
    Update the points of a user by their ID.
    """
    cursor = conn.cursor()
    query = "UPDATE Users SET points = %s WHERE user_id = %s"
    cursor.execute(query, (points, user_id))
    conn.commit()
    cursor.close()
    return