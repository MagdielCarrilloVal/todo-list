import json
import os

archivo = 'todo.json'

def load_task():
    if not os.path.exists(archivo):
        return []
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_task(tasks):
    with open (archivo, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False,indent=4)


def create_task(tasks):
    # Ask the user for the task description
    description = input("Enter the task description: ")
    # Generate the ID based on the current list length
    new_id = len(tasks)+1

    # Create the task dictionary
    new_task = {
        "id": new_id,
        "description": description,
        "status": "pending"
    }

    #Add it to the list and save
    tasks.append(new_task)
    save_task(tasks)
    print(f"Task '{description}' created with ID: '{new_id}")

def view_task(task):
    if not os.path.exists(archivo):
        return []
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            data = json.load(archivo)
            print(data['description'])
            print(data['status'])
    except (json.JSONDecodeError, IOError):
        return []

'''        
def delete_task():


# CRUD -> CREATE, READ , UPDATE, DELETE
'''