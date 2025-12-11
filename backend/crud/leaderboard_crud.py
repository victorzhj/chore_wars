from .config_db_connection import Config


def get_leaderboard_data():
    conn = Config().create_connection()
    cursor = conn.cursor()
    query = """
        SELECT u.user_id, u.username, u.points, COUNT(l.log_id) 
            FROM Users AS u 
            LEFT OUTER JOIN Logs as l 
            ON u.user_id=l.user_id 
        GROUP BY u.user_id, u.username, u.points
        ORDER BY u.points DESC
        """
    cursor.execute(query)
    results = cursor.fetchall()
    print(results)
    cursor.close()
    conn.close()
    return results