from flask import Blueprint, render_template, jsonify
from crud.leaderboard_crud import get_leaderboard_data
leaderboard_route = Blueprint('leaderboard_route', __name__, template_folder='../../frontend/leaderboard_templates')

@leaderboard_route.route('/leaderboard')
def leaderboard():
    """
    Docstring for leaderboard
    Renders the leaderboard page displaying user rankings based on points.
    Returns:
        Rendered HTML template for the leaderboard page.
    To use the returned data in html, you can loop through the leaderboard list.
    Example:
        {% for user in leaderboard %}
            <p>{{ user.username }} - {{ user.points }}</p>
        {% endfor %}
    """
    leaderboard_data = get_leaderboard_data()
    print(leaderboard_data)
    return render_template('leaderboard.html', leaderboard=leaderboard_data)
