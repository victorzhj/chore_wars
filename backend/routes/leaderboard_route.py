from flask import Blueprint, render_template, request, redirect, url_for, session
from crud.leaderboard_crud import get_leaderboard_data
leaderboard_route = Blueprint('leaderboard_route', __name__, template_folder='../../frontend/leaderboard_templates')