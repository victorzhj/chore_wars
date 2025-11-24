from flask import Blueprint, render_template, request, redirect, url_for, session
from crud.user_crud import get_username, create_user, login_user, get_user_points, modify_user_settings, modify_user_points, delete_user
user_route = Blueprint('user_route', __name__, template_folder='../../frontend/user_templates')