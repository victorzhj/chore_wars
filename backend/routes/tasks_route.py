from flask import Blueprint, render_template, request, redirect, url_for, session
from crud.tasks_crud import get_open_tasks, get_closed_tasks, get_user_completed_tasks, add_task, update_task, delete_task
tasks_route = Blueprint('tasks_route', __name__, template_folder='../../frontend/tasks_templates')

@tasks_route.route('/tasks')
def tasks():
    open_tasks = get_open_tasks()
    closed_tasks = get_closed_tasks()
    return render_template('tasks.html', open_tasks=open_tasks, closed_tasks=closed_tasks)

@tasks_route.route('/tasks/user')
def user_completed_tasks(user_id):
    completed_tasks = get_user_completed_tasks(user_id)
    return render_template('user_completed_tasks.html', tasks=completed_tasks)

@tasks_route.route('/tasks/add', methods=['GET', 'POST'])