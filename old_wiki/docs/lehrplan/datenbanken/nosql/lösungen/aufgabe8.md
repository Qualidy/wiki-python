# TODO-App


Hinweis: Das geht auch schöner ;)

```python
import pymongo
from pymongo import MongoClient

# 1. Datenbank und Sammlung erstellen
client = MongoClient()
db = client.ToDoDB
tasks_collection = db.tasks

# 3. Funktionen für CRUD-Operationen erstellen
def create_task(title, description, status):
    task = {
        "title": title,
        "description": description,
        "status": status
    }
    result = tasks_collection.insert_one(task)
    return result.inserted_id

def get_tasks():
    return list(tasks_collection.find())

def update_task(task_id, new_title, new_description, new_status):
    query = {"_id": task_id}
    update_data = {"$set": {"title": new_title, "description": new_description, "status": new_status}}
    result = tasks_collection.update_one(query, update_data)
    return result.modified_count > 0

def delete_task(task_id):
    result = tasks_collection.delete_one({"_id": task_id})
    return result.deleted_count > 0

# 5. Zusätzliche Funktionen (optional)
def search_tasks(query):
    # Sucht nach Aufgaben anhand von Titel oder Status
    return list(tasks_collection.find({"$or": [{"title": {"$regex": query, "$options": "i"}},
                                                {"status": {"$regex": query, "$options": "i"}}]}))

def count_tasks_by_status(status):
    # Zählt die Anzahl der Aufgaben nach ihrem Status
    return tasks_collection.count_documents({"status": status})

def assign_task_to_user(task_id, user_id):
    # Erweitert die Datenbankstruktur, um Benutzerinformationen zu speichern und weist Aufgaben bestimmten Benutzern zu
    tasks_collection.update_one({"_id": task_id}, {"$set": {"assigned_user": user_id}})

# 4. CLI-Benutzerschnittstelle erstellen
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python todo_app.py <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "add" and len(sys.argv) == 5:
        title, description, status = sys.argv[2], sys.argv[3], sys.argv[4]
        task_id = create_task(title, description, status)
        print(f"Task added with ID: {task_id}")

    elif command == "list" and len(sys.argv) == 2:
        tasks = get_tasks()
        for task in tasks:
            print(task)

    elif command == "update" and len(sys.argv) == 6:
        task_id, new_title, new_description, new_status = sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
        success = update_task(task_id, new_title, new_description, new_status)
        if success:
            print(f"Task {task_id} updated successfully")
        else:
            print(f"Task {task_id} not found")

    elif command == "delete" and len(sys.argv) == 3:
        task_id = sys.argv[2]
        success = delete_task(task_id)
        if success:
            print(f"Task {task_id} deleted successfully")
        else:
            print(f"Task {task_id} not found")
    
    elif command == "search" and len(sys.argv) == 3:
        query = sys.argv[2]
        matching_tasks = search_tasks(query)
        for task in matching_tasks:
            print(task)

    elif command == "count" and len(sys.argv) == 3:
        status = sys.argv[2]
        task_count = count_tasks_by_status(status)
        print(f"Number of tasks with status '{status}': {task_count}")

    elif command == "assign" and len(sys.argv) == 4:
        task_id, user_id = sys.argv[2], sys.argv[3]
        assign_task_to_user(task_id, user_id)
        print(f"Task {task_id} assigned to user {user_id}")

    else:
        print("Invalid command or arguments")

```

Beispiel für die Nutzung:

```bash
python todo_app.py search "Query String"
python todo_app.py count "Status"
python todo_app.py assign task_id user_id
```