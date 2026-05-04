# app.py

from flask import Flask, flash, redirect, render_template, request, url_for
from forms.tasks import TaskForm
from forms.update_task import UpdateTaskForm
from utils.database import create_task, get_task_by_id, init_app, get_tasks_by_status, update_task

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


# Konfiguration für die MongoDB-Verbindung
app.config['MONGO_URI'] = 'mongodb://root:example@localhost:27017/admin'


# Initialisierung der Datenbankverbindung
init_app(app)


@app.route('/')
def index():
    return redirect(url_for('kanban_board'))



@app.route('/board')
def kanban_board():
    todo_tasks = get_tasks_by_status('todo')
    in_progress_tasks = get_tasks_by_status('in_progress')
    done_tasks = get_tasks_by_status('done')
    return render_template('kanban_board.html', todo_tasks=todo_tasks, in_progress_tasks=in_progress_tasks, done_tasks=done_tasks)


@app.route('/create_task', methods=['GET', 'POST'])
def create_task_route():
    form = TaskForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        status = form.status.data
        create_task(title, description, status)
        flash('Task created successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('create_task.html', form=form)



@app.route('/update_task/<task_id>', methods=['GET', 'POST'])
def update_task_route(task_id):
    task = get_task_by_id(task_id)
    if task is None:
        flash('Task not found!', 'error')
        return redirect(url_for('index'))

    form = UpdateTaskForm(obj=task)
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        status = form.status.data
        print("hier")
        update_task(task_id, title, description, status)
        flash('Task updated successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('update_task.html', form=form, task_id=task_id)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
