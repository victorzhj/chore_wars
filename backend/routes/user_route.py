from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from crud.user_crud import get_username, create_user, login_user, get_user_points, modify_user_settings, modify_user_points, delete_user
user_route = Blueprint('user_route', __name__, template_folder='../../frontend/user_templates')

@user_route.route('/user/login', methods=['GET', 'POST'])
def login():
    """
    Docstring for login
    Renders the login page and handles user authentication.
    Returns:
        Rendered HTML template for the login page or redirects to tasks page upon successful login.
        To use this function, submit a POST request with 'username' and 'password' form data.
    Example:
        <form method="POST" action="/user/login">
            <input type="text" name="username" required />
            <input type="password" name="password" required />
            <button type="submit">Login</button>
        </form>
    If the credentials are valid, the user is redirected to the tasks page.
    Else, an error is returned
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = login_user(username, password)
        if user:
            session['user_id'] = user[0]
            return redirect(url_for('tasks_route.tasks'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@user_route.route('/user/register', methods=['GET', 'POST'])
def register():
    """
    Docstring for register
    Renders the registration page and handles new user creation.
    Returns:
        Rendered HTML template for the registration page or redirects to login page upon successful registration.
        To use this function, submit a POST request with user registration form data.
    Example:
        <form method="POST" action="/user/register">
            <input type="text" name="username" required />
            <input type="password" name="password" required />
            <input type="email" name="email" required />
            <button type="submit">Register</button>
        </form>
    If the username is already taken, an error message is returned
    """
    if request.method == 'POST':
        username = request.form['username']
        if (get_username(username)):
            return render_template('register.html', error='Username already used')
        create_user(request.form.to_dict())
        return render_template('login.html', code='user created successfully')
    return render_template('register.html')

@user_route.route('/user/points', methods=['POST'])
def points():
    """
    Docstring for points
    Updates the user's points based on completed tasks.
    Returns:
        Redirects to the leaderboard page after updating points.
        To use this function, submit a POST request with JSON data containing 'points'.
    Example:
        fetch('/user/points', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ points: 10 })
        });
    """
    user_id = session.get('user_id')
    if request.method == 'POST':
        current_points = get_user_points(user_id)[0]
        print(session['user_id'])
        print(current_points)
        new_points = int(current_points) + request.get_json()['points']
        modify_user_points(user_id=user_id, points=new_points)
        return redirect(url_for('leaderboard_route.leaderboard'))

@user_route.route('/user/logout', methods=['POST'])
def logout():
    """
    Docstring for logout
    Logs out the current user by clearing the session.
    Returns:
        Redirects to the login page after logging out.
    """
    session.pop('user_id', None)
    return redirect(url_for('user_route.login'))

@user_route.route('/user/delete', methods=['GET', 'POST'])
def delete():
    """
    Docstring for delete
    Deletes the current user account and logs out the user.
    Returns:
        Redirects to the login page after deleting the user account.
    """
    if request.method == 'POST':
        user_id = session.get('user_id')
        delete_user(user_id)
        session.pop('user_id', None)
        return redirect(url_for('user_route.login'))
    return render_template('delete.html')