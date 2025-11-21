from config_db_connection import Config

conn = Config().create_connection()

def get_open_tasks():
    cursor = conn.cursor()
    query = "SELECT * FROM Tasks WHERE completed = FALSE;"
    cursor.execute(query)
    tasks = cursor.fetchall()
    cursor.close()
    return tasks

def get_closed_tasks():
    cursor = conn.cursor()
    query = "SELECT * FROM Tasks WHERE completed = TRUE;"
    cursor.execute(query)
    tasks = cursor.fetchall()
    cursor.close()
    return tasks

def get_user_completed_tasks(user_id):
    cursor = conn.cursor()
    query = """
        SELECT t.title, t.description, t.points, t.deadline FROM 
            Users as u 
            INNER JOIN
            Logs as l
            ON u.user_id=l.user_id
            LEFT OUTER JOIN
            Tasks as t
            ON l.task_id=t.task_id
        WHERE u.user_id=%s;
    """
    cursor.execute(query, (user_id))
    tasks = cursor.fetchall()
    cursor.close()
    return tasks

def add_task(task_data):
    cursor = conn.cursor()
    query = """
        INSERT INTO Tasks (title, description, created_by_user_id, points, deadline)
        VALUES (%s, %s, %s, %s, %s);
    """
    cursor.execute(query, (
        task_data['title'],
        task_data['description'],
        task_data['created_by_user_id'],
        task_data['points'],
        task_data['deadline']
    ))
    conn.commit()
    cursor.close()
    return

def update_task(task_id, task_data):
    cursor = conn.cursor()
    query = """
        UPDATE Tasks
        SET title=%s, description=%s, points=%s, deadline=%s, completed=%s
        WHERE task_id=%s;
    """
    cursor.execute(query, (
        task_data['title'],
        task_data['description'],
        task_data['points'],
        task_data['deadline'],
        task_data['completed'],
        task_id
    ))
    conn.commit()
    cursor.close()
    return

def delete_task(task_id):
    cursor = conn.cursor()
    query = "DELETE FROM Tasks WHERE task_id=%s;"
    cursor.execute(query, (task_id))
    conn.commit()
    cursor.close()
    return


