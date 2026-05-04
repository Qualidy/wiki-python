# utils/database.py

from bson import ObjectId
from flask_pymongo import PyMongo

mongo = PyMongo()


def init_app(app):
    mongo.init_app(app)


def create_task(title, description, status):
    tasks_collection = mongo.db.tasks
    task_data = {
        "title": title,
        "description": description,
        "status": status
    }
    result = tasks_collection.insert_one(task_data)
    return result.inserted_id


def get_tasks_by_status(status):
    tasks = mongo.db.tasks.find({"status": status})
    return list(tasks)


def update_task(task_id, title, description, status):
    tasks_collection = mongo.db.tasks
    tasks_collection.update_one(
        {'_id': ObjectId(task_id)},
        {'$set': {'title': title, 'description': description, 'status': status}}
    )


def get_task_by_id(task_id):
    tasks_collection = mongo.db.tasks
    task = tasks_collection.find_one({'_id': ObjectId(task_id)})
    return task
