from config_db_connection import Config
import pymysql.cursors

def initialize_database():
    conn = Config().create_connection()
    cursor = conn.cursor()
    drop_tables(cursor)
    create_tables(cursor)
    init_data(cursor)
    conn.commit()
    conn.close()

def drop_tables(cursor: pymysql.cursors.Cursor):
    cursor.execute("DROP TABLE IF EXISTS Logs")
    cursor.execute("DROP TABLE IF EXISTS Tasks")
    cursor.execute("DROP TABLE IF EXISTS Users")

def create_tables(cursor: pymysql.cursors.Cursor):
    cursor.execute("""
        CREATE TABLE Users (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            user_password VARCHAR(255) NOT NULL,
            points INT DEFAULT 0
        );
    """)
    cursor.execute("""
        CREATE TABLE Tasks (
            task_id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            description TEXT,
            created_by_user_id INT,
            points INT DEFAULT 0,
            deadline DATETIME,
            completed BOOLEAN DEFAULT FALSE,
            FOREIGN KEY (created_by_user_id) REFERENCES Users(user_id)
            ON DELETE CASCADE
        );
    """)
    cursor.execute("""
        CREATE TABLE Logs (
            log_id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            task_id INT,
            completion_time DATETIME,
            FOREIGN KEY (user_id) REFERENCES Users(user_id)
            ON DELETE CASCADE,
            FOREIGN KEY (task_id) REFERENCES Tasks(task_id)
            ON DELETE CASCADE
        );
    """)

def init_data(cursor: pymysql.cursors.Cursor):
    cursor.execute("""
        INSERT INTO Users (username, user_password, points) VALUES
            ('Tester1', 'testing1', 10),
            ('Tester2', 'testing2', 30),
            ('Tester3', 'testing3', 0)
    """
)
    cursor.execute("""
        INSERT INTO Tasks (title, description, created_by_user_id, points, deadline, completed) VALUES
            ('Wash Dishes', 'Clean all dishes in the sink', 1, 10, '2024-12-01 18:00:00', FALSE),
            ('Mow Lawn', 'Mow the front and back lawn', 2, 20, '2024-12-02 12:00:00', FALSE),
            ('Take Out Trash', 'Take out all household trash', 3, 5, '2024-12-01 20:00:00', TRUE),
            ('Vacuum Living Room', 'Vacuum the entire living room area', 1, 15, '2024-12-03 15:00:00', FALSE),
            ('Clean Bathroom', 'Scrub and clean the bathroom', 2, 25, '2024-12-04 10:00:00', TRUE),
            ('Grocery Shopping', 'Buy groceries for the week', 3, 30, '2024-12-05 17:00:00', FALSE),
            ('Walk the Dog', 'Take the dog for a 30-minute walk', 1, 10, '2024-12-01 19:00:00', TRUE),
            ('Laundry', 'Wash and fold all laundry', 2, 15, '2024-12-02 14:00:00', FALSE)
    """)

    cursor.execute("""
        INSERT INTO Logs (user_id, task_id, completion_time) VALUES
            (1, 3, '2024-11-30 16:00:00'),
            (2, 5, '2024-11-29 11:00:00'),
            (1, 7, '2024-11-30 18:30:00')
    """)

initialize_database()