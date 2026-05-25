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
    if not description:
        print("Task description cannot be empty!")
        return

    # Generate the ID based on the current list length
    new_id = max([task['id'] for task in tasks], default=0) + 1

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

def view_task(tasks):
    if not tasks:
        print("No tasks found! Your to-do list is empty")
        return
    print("\nTO-DO LIST\n")
    for task in tasks:
        print(f"{task['id']}:  {task['description']} - {task['status']}")
    print("-----------------------")

def delete_task(tasks):
    if not tasks:
        print("Your to-do list is empty. Nothing to delete")
        return
    try:
        # Ask the user for the ID that want to delete
        task_id = int(input("Enter the ID of the task you want to delete: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    task_to_remove = None
    # Verify if the task exists
    for task in tasks:
        if task['id'] == task_id:
            task_to_remove = task
            break
    if task_to_remove:
        tasks.remove(task_to_remove)
        save_task(tasks)
        print(f"Taks '{task_to_remove['description']} (ID: {task_id}) delete successfully.")
    else:
        print(f"No task found with ID: {task_id}")


def edit_task(tasks):
    if not tasks:
        print("Your TO-DO list is empty. Nothing to edit")
        return
    try:
        # Ask the user for the ID that want to edit
        task_id = int(input("Enter the ID of the task you want to edit: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return
    
    # Look for the task
    for task in tasks:
        if task['id'] == task_id:
            new_desc = input(f"Enter new description for '{task['description']} (or press Enter to leave unchanged): ").strip()

            if new_desc:
                task['description'] = new_desc
                save_task(tasks)
                print(f"Tak {task_id} update successfully!")
            else:
                print("No changes made.")
            return
    print(f"No task found with ID: {task_id}") 

def mark_completed(tasks):
    if not tasks:
        print("Your TO-DO list is empty!")
        return
    try:
        task_id = int(input("Enter the ID of the tasj you want to mark as completed: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    for task in tasks:
        if task['id'] == task_id:
            if task['status'] == 'completed':
                print(f"Task {task_id} is already completed!")
                return
            task['status'] = 'completed'
            save_task(tasks)
            print(f"Task '{task['description']}' (ID: {task_id}) marked as completed!")
            return
        print(f"No task found with ID: {task_id}")

def main():
    tasks = load_task()
    while True:
        print("\n1. View Tasks" \
             "\n2. Add Tak" \
             "\n3. Delete task" \
             "\n4. Edit task" \
             "\n5. Mark completed" \
             "\n6. Exit")
        choice = input("Chosse an option: ").strip()

        if choice == '1':
            view_task(tasks)
        elif choice == '2':
            create_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            edit_task(tasks)
        elif choice == '5':
            mark_completed(tasks)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()