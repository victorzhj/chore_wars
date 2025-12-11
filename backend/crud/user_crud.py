from .config_db_connection import Config

def get_username(username):
    """
    Fetch a user by username. Used to check if a user exists during registration.
    """
    conn = Config().create_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Users WHERE username = %s"
    cursor.execute(query, (username))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def create_user(user_data):
    """
    Create a new user in the database.
    """
    conn = Config().create_connection()
    cursor = conn.cursor()
    insert_query = "INSERT INTO Users (username, user_password) VALUES (%s, %s)"
    cursor.execute(insert_query, (user_data['username'], user_data['password']))
    conn.commit()
    cursor.close()
    conn.close()
    return

def login_user(username, password):
    """
    Authenticate a user with username and password.
    """
    conn = Config().create_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Users WHERE username = %s AND user_password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def get_user_points(user_id):
    """
    Retrieve the points of a user by their ID.
    """
    conn = Config().create_connection()
    cursor = conn.cursor()
    query = "SELECT points FROM Users WHERE user_id = %s"
    cursor.execute(query, (user_id))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def modify_user_settings(user_id, modified_settings):
    return

def modify_user_points(user_id, points):
    """
    Update the points of a user by their ID.
    """
    conn = Config().create_connection()
    cursor = conn.cursor()
    query = "UPDATE Users SET points = %s WHERE user_id = %s"
    cursor.execute(query, (points, user_id))
    conn.commit()
    cursor.close()
    conn.close()
    return

def delete_user(user_id):
    """
    Delete a user from the database by their ID.
    """
    conn = Config().create_connection()
    cursor = conn.cursor()
    query = "DELETE FROM Users WHERE user_id = %s"
    cursor.execute(query, (user_id))
    conn.commit()
    cursor.close()
    conn.close()
    return