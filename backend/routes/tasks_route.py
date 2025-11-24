from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from crud.tasks_crud import get_open_tasks, get_closed_tasks, get_user_completed_tasks, add_task, update_task, delete_task
tasks_route = Blueprint('tasks_route', __name__, template_folder='../../frontend/tasks_templates')

@tasks_route.route('/tasks', methods=['GET'])
def tasks():
    open_tasks = get_open_tasks()
    closed_tasks = get_closed_tasks()
    return render_template('tasks.html', open_tasks=open_tasks, closed_tasks=closed_tasks)

@tasks_route.route('/tasks/user', methods=['GET'])
def user_completed_tasks():
    user_id = session['user_id']
    completed_tasks = get_user_completed_tasks(user_id)
    return render_template('user_completed_tasks.html', tasks=completed_tasks)

@tasks_route.route('/tasks/add', methods=['GET', 'POST'])
def add_tasks():
    if request.method == 'POST':
        task = request.get_json()
        task['created_by_user_id'] = session['user_id']
        task['deadline'] = task['deadline'].replace('T', ' ') + ':00'
        add_task(task)
        return render_template('add_task.html')
    return render_template('add_task.html')

@tasks_route.route('/tasks/modify', methods=['GET', 'POST'])
def modify_task():
    if request.method == 'POST':
        modified_task = request.get_json()
        modified_task['deadline'] = modified_task['deadline'].replace('T', ' ') + ':00'
        modified_task_id = modified_task['task_id']
        update_task(modified_task_id, modified_task)
        return render_template('task_modify.html')
    return render_template('task_modify.html')

@tasks_route.route('/tasks/delete', methods=['POST'])
def delete_task_route():
    task_id = request.get_json()['task_id']
    delete_task(task_id)
    return redirect(url_for('tasks_route.tasks'))