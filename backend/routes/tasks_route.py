from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from crud.tasks_crud import get_open_tasks, get_closed_tasks, get_user_completed_tasks, add_task, add_multiple_tasks_crud, update_task, delete_task, complete_task, multi_delete_tasks
from crud.user_crud import get_user_points, modify_user_points
tasks_route = Blueprint('tasks_route', __name__, template_folder='../../frontend/tasks_templates')

@tasks_route.route('/tasks', methods=['GET'])
def tasks():
    """
    Docstring for tasks
    Renders the main tasks page displaying open and closed tasks.
    Returns:
        Rendered HTML template for the tasks page.
    To use the returned data in html, you can loop through the open_tasks and closed_tasks lists.
    Example:
        {% for task in open_tasks %}
            <p>{{ task.title }} - {{ task.deadline }}</p>
        {% endfor %}
    """
    open_tasks = get_open_tasks()
    closed_tasks = get_closed_tasks()
    return render_template('tasks.html', open_tasks=open_tasks, closed_tasks=closed_tasks)

@tasks_route.route('/tasks/user', methods=['GET'])
@tasks_route.route('/tasks/user/<int:user_id>', methods=['GET'])
def user_completed_tasks(user_id=None):
    """
    Docstring for user_completed_tasks
    Renders a page displaying all tasks completed by the current user.
    Returns:
        Rendered HTML template for the user completed tasks page.
    To use the returned data in html, you can loop through the tasks list.
    Example:
        {% for task in tasks %}
            <p>{{ task.title }} - {{ task.deadline }}</p>
        {% endfor %}
    """
    if user_id == None:
        user_id = session['user_id']
    completed_tasks = get_user_completed_tasks(user_id)
    return render_template('user_completed_tasks.html', tasks=completed_tasks)

@tasks_route.route('/tasks/add', methods=['GET', 'POST'])
def add_tasks():
    """
    Docstring for add_tasks
    Handles adding a new task. Supports both GET and POST requests.
    Returns:
        Rendered HTML template for adding a task.
    To add task to the database, send a POST request with JSON body containing task details.
    Example JSON body:
        {
            "title": "Task Title",
            "description": "Task Description",
            "deadline": "2024-12-31T23:59"
        }
    """
    if request.method == 'POST':
        task = request.get_json()
        task['created_by_user_id'] = session['user_id']
        task['deadline'] = task['deadline'].replace('T', ' ') + ':00'
        add_task(task)
        return render_template('add_task.html')
    return render_template('add_task.html')

@tasks_route.route('/tasks/add_multiple', methods=['POST'])
def add_multiple_tasks():
    if request.method == 'POST':
        tasks_data = request.get_json()['tasks']
        for task in tasks_data:
            task['created_by_user_id'] = session['user_id']
            task['deadline'] = task['deadline'].replace('T', ' ') + ':00'
        add_multiple_tasks_crud(tasks_data)
        return jsonify({'status': 'success'})

@tasks_route.route('/tasks/completed', methods=['POST'])
def complete_task_endpoint():  # <--- 이름을 바꿔서 충돌 해결
    if 'user_id' not in session:
        return jsonify({'status': 'error', 'message': 'Login required'}), 401

    user_id = session['user_id']
    current_points = get_user_points(user_id)[0]
    points = request.get_json()['points']
    new_points = current_points + points
    modify_user_points(user_id, new_points)
    task_id = request.get_json()['task_id']
    
    # 이제 crud의 complete_task를 정상적으로 호출함
    complete_task(task_id, user_id)

    return jsonify({'status': 'success'})

@tasks_route.route('/tasks/modify', methods=['GET', 'POST'])
def modify_task():
    """
    Docstring for modify_task
    Handles modifying an existing task. Supports both GET and POST requests.
    Returns:
        Rendered HTML template for modifying a task.
    To modify a task in the database, send a POST request with JSON body containing modified task details.
    Example JSON body:
        {
            "task_id": 1,
            "title": "Modified Task Title",
            "description": "Modified Task Description",
            "deadline": "2024-12-31T23:59"
        }
    """
    if request.method == 'POST':
        modified_task = request.get_json()
        modified_task['deadline'] = modified_task['deadline'].replace('T', ' ') + ':00'
        modified_task_id = modified_task['task_id']
        update_task(modified_task_id, modified_task)
        return render_template('task_modify.html')
    return render_template('task_modify.html')

@tasks_route.route('/tasks/delete', methods=['POST'])
def delete_task_route():
    """
    Docstring for delete_task_route
    Handles deleting an existing task. Supports POST requests.
    Returns:
        Redirects to the main tasks page after deletion.
    To delete a task from the database, send a POST request with JSON body containing the task ID.
    Example JSON body:
        {
            "task_id": 1
        }
    """
    task_id = request.get_json()['task_id']
    delete_task(task_id)
    return redirect(url_for('tasks_route.tasks'))

@tasks_route.route('/tasks/multi_delete', methods=['POST'])
def multi_delete_tasks_route():
    """
    Docstring for multi_delete_tasks_route
    Handles deleting multiple tasks. Supports POST requests.
    Returns:
        Redirects to the main tasks page after deletion.
    To delete multiple tasks from the database, send a POST request with JSON body containing a list of task IDs.
    Example JSON body:
        {
            "task_ids": [1, 2, 3]
        }
    """
    task_ids = request.get_json()['task_ids']
    multi_delete_tasks(task_ids)
    return redirect(url_for('tasks_route.tasks'))