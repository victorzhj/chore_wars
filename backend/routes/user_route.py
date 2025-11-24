from flask import Blueprint, render_template, request, redirect, url_for, session
from crud.user_crud import get_username, create_user, login_user, get_user_points, modify_user_settings, modify_user_points, delete_user
user_route = Blueprint('user_route', __name__, template_folder='../../frontend/user_templates')

@user_route.route('/user/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = login_user(username, password)
        if user:
            session['user_id'] = user['user_id']
            return redirect(url_for('tasks_route.tasks'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@user_route.route('/user/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        if (not get_username(username)):
            return render_template('register.html', error='Username already used')
        create_user(request.form.to_dict)
        return render_template('login.html', code='user created successfully')
    return render_template('register.html')

@user_route.route('/user/points', methods=['GET', 'POST'])
def points():
    user_id = session.get('user_id')
    if request.method == 'POST':
        current_points = get_user_points(user_id)
        new_points = current_points + request.get_json()['points']
        modify_user_points(user_id=user_id, points=new_points)
        return redirect(url_for('leaderboard_route.leaderboard'))
    return render_template('points.html')

@user_route.route('/user/logout', methods=['GET'])
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@user_route.route('/user/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        user_id = session.get('user_id')
        delete_user(user_id)
        session.pop('user_id', None)
        return redirect(url_for('login'))
    return render_template('delete.html')