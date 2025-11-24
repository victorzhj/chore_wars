from flask import Blueprint, render_template, jsonify
from crud.leaderboard_crud import get_leaderboard_data
leaderboard_route = Blueprint('leaderboard_route', __name__, template_folder='../../frontend/leaderboard_templates')

@leaderboard_route.route('/leaderboard')
def leaderboard():
    leaderboard_data = get_leaderboard_data()
    return jsonify(leaderboard_data)
    #return render_template('leaderboard.html', leaderboard=leaderboard_data)