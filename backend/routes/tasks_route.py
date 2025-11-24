from flask import Blueprint, render_template, request, redirect, url_for, session
from crud.tasks_crud import get_open_tasks, get_closed_tasks, get_user_completed_tasks, add_task, update_task, delete_task
tasks_route = Blueprint('tasks_route', __name__, template_folder='../../frontend/tasks_templates')