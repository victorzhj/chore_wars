from flask import Flask
from routes.leaderboard_route import leaderboard_route
from routes.tasks_route import tasks_route
from routes.user_route import user_route
import os
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

app.register_blueprint(leaderboard_route)
app.register_blueprint(tasks_route)
app.register_blueprint(user_route)

if __name__ == '__main__':
    app.run(debug=True)