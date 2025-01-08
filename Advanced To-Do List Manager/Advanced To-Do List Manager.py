import json
import time
import os

clear = lambda: os.system("cls" if os.name == "nt" else "clear")

tasks = []
complete = []

def ensure_directory_exists(directory):
    print(f"Checking if directory exists: {directory}")
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
            print(f"Directory created: {directory}")
        except Exception as e:
            print(f"Error creating directory {directory}: {e}")
    else:
        print(f"Directory already exists: {directory}")
        
def get_desktop_path():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    return desktop_path
    
def get_default_save_path():
    desktop_path = get_desktop_path()
    subfolder = os.path.join(desktop_path, "ToDoList")
    return subfolder
    
def save_tasks_to_file(tasks, complete, directory=None, filename="tasks.json"):
    if directory is None:
        directory = get_default_save_path()
        
    ensure_directory_exists(directory)
    filepath = os.path.join(directory, filename)
    backup_filepath = filepath + ".bak"
    
    print(f"Saving tasks to: {filepath}")
    
    if os.path.exists(backup_filepath):
        timestamp = time.strftime("%Y%m%d%H%M%S")
        backup_filepath = f"{filepath}_{timestamp}.bak"
        print(f"Backup file already exists. Using a new backup name: {backup_filepath}")
        
    if os.path.exists(filepath):
        os.rename(filepath, backup_filepath)
        
    data = {
        "not completed": tasks,
        "completed": complete
    }
    
    try:
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Tasks saved to {filepath}")
    except Exception as e:
        print(f"Error saving tasks: {e}")
        if os.path.exists(backup_filepath):
            os.rename(backup_filepath, filepath)
            
def load_tasks_from_file(directory=None, filename="tasks.json"):
    if directory is None:
        directory = get_default_save_path()
        
    filepath = os.path.join(directory, filename)
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
            if not isinstance(data, dict):
                raise ValueError("Invalid file format.")
                
            tasks = data.get("not completed", [])
            complete = data.get("completed", [])
            print(f"Tasks loaded from {filepath}")
            return tasks, complete
            
    except FileNotFoundError:
        print(f"File not found: {filepath}. Starting fresh.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {filepath}. Starting fresh.")
    except Exception as e:
        print(f"Error loading tasks: {e}. Starting fresh.")
        
    return [], []
    
def main():
    global tasks, complete
    tasks, complete = load_tasks_from_file()
    
    while True:
        print("""
Welcome to the To-Do List Python App!

Here you can:
    1. Add a task
    2. Mark a task as complete
    3. View all tasks
    4. Delete a task
    5. Save tasks to a file
    6. Load tasks from a file
    7. Exit

Select an option:
        """)
        try:
            action = int(input("> "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue
            
        if action == 1:
            task = input("What task would you like to add?\n> ")
            tasks.append(task)
            print(f"Task added: {task}")
            
        elif action == 2:
            if tasks:
                print(f"Tasks: {tasks}")
                try:
                    index = int(input("Enter the task number to mark as complete:\n> ")) - 1
                    if 0 <= index < len(tasks):
                        complete.append(tasks.pop(index))
                        print("Task marked as complete.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks to mark as complete.")
                
        elif action == 3:
            print(f"""
Not completed:
{tasks}

Completed:
{complete}
            """)
            
        elif action == 4:
            if tasks or complete:
                list_choice = input("Delete from (1) not completed or (2) completed tasks?\n> ")
                try:
                    list_choice = int(list_choice)
                    if list_choice == 1 and tasks:
                        print(f"Not completed tasks: {tasks}")
                        index = int(input("Enter the task number to delete:\n> ")) - 1
                        if 0 <= index < len(tasks):
                            removed_task = tasks.pop(index)
                            print(f"Deleted task: {removed_task}")
                        else:
                            print("Invalid task number.")
                    elif list_choice == 2 and complete:
                        print(f"Completed tasks: {complete}")
                        index = int(input("Enter the task number to delete:\n> ")) - 1
                        if 0 <= index < len(complete):
                            removed_task = complete.pop(index)
                            print(f"Deleted task: {removed_task}")
                        else:
                            print("Invalid task number.")
                    else:
                        print("Invalid choice or list is empty.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks to delete.")
                
        elif action == 5:
            directory = input("Enter directory to save tasks (default: Desktop\\ToDoList):\n> ") or None
            save_tasks_to_file(tasks, complete, directory=directory)
            
        elif action == 6:
            directory = input("Enter directory to load tasks from (default: Desktop\\ToDoList):\n> ") or None
            tasks, complete = load_tasks_from_file(directory=directory)
            
        elif action == 7:
            print("Goodbye!")
            break
            
        else:
            print("Please select a valid option.")
        input("Press Enter to continue...")
        clear()
        
try:
    main()
except KeyboardInterrupt:
    print("Goodbye")
    exit()