from .config_db_connection import Config

conn = Config().create_connection()

def get_open_tasks():
    cursor = conn.cursor()
    query = "SELECT * FROM Tasks WHERE completed = FALSE;"
    cursor.execute(query)
    tasks = cursor.fetchall()
    cursor.close()
    tasks_dict = []
    for task in tasks:
        temp_dict = {
            'task_id': task[0],
            'title': task[1],
            'description': task[2],
            'created_by_user_id': task[3],
            'points': task[4],
            'deadline': task[5],
            'completed': task[6]
        }
        tasks_dict.append(temp_dict)
    return tasks_dict

def get_closed_tasks():
    cursor = conn.cursor()
    query = "SELECT * FROM Tasks WHERE completed = TRUE;"
    cursor.execute(query)
    tasks = cursor.fetchall()
    cursor.close()
    tasks_dict = []
    for task in tasks:
        temp_dict = {
            'task_id': task[0],
            'title': task[1],
            'description': task[2],
            'created_by_user_id': task[3],
            'points': task[4],
            'deadline': task[5],
            'completed': task[6]
        }
        tasks_dict.append(temp_dict)
    return tasks_dict

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
    tasks_dict = []
    for task in tasks:
        temp_dict = {
            'title': task[0],
            'description': task[1],
            'points': task[2],
            'deadline': task[3]
        }
        tasks_dict.append(temp_dict)
    return tasks_dict

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

def complete_task(task_id, user_id):
    cursor = conn.cursor()
    query = "UPDATE Tasks SET completed=TRUE WHERE task_id=%s;"
    cursor.execute(query, (task_id))
    conn.commit()
    query = "INSERT INTO Logs (user_id, task_id, completion_time) VALUES (%s, %s, NOW());"
    cursor.execute(query, (user_id, task_id))
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


