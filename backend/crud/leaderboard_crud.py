from config_db_connection import Config

conn = Config().create_connection()

def get_leaderboard_data():
    cursor = conn.cursor()
    query = """
        SELECT u.user_id, u.nickname, points, COUNT(l.log_id) 
            FROM Users AS u 
            LEFT OUTER JOIN Logs as l 
            ON u.user_id=l.user_id 
        GROUP BY u.user_id, u.nickname, u.points
        ORDER BY u.points DESC
        """
    cursor.execute(query)
    results = cursor.fetchall()
    print(results)
    return results

get_leaderboard_data()