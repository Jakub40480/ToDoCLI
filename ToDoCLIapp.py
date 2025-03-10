import time
import json
import os
import random

data_file = "data.json"

def generate_unique_id(used_ids):
    while True:
        unique_id = random.randint(0, 1000)
        if unique_id not in used_ids:
            used_ids.append(unique_id)
            return unique_id

def add_task():
    task_name = input("Name of the task: ")
    task_description = input("Description(optional): ")
    time_created = time.ctime()
    time_updated = time.ctime()

    # Load existing tasks from the file
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = []
    else:
        tasks = []

    # Generate a unique ID
    used_ids = [task["ID"] for task in tasks]
    unique_id = generate_unique_id(used_ids)

    while True:
        try:
            task_status = int(input("todo(1), in-progress(2), done(3): "))
        except ValueError:
            print("Invalid input for task status. Please enter 1, 2, or 3.")
            continue
        if task_status not in range(1, 4):
            print("Invalid input for task status. Please enter 1, 2, or 3.")
        else:
            break

    task_status = str(task_status)
    if task_status == "1":
        task_status = "todo"
    elif task_status == "2":
        task_status = "in-progress"
    else:
        task_status = "done"

    task = {
        "ID": unique_id,
        "name": task_name,
        "description": task_description,
        "time created": time_created,
        "time updated": time_updated,
        "status": task_status
    }

    # Add the new task to the list of tasks
    tasks.append(task)

    # Save the updated list of tasks back to the file
    with open(data_file, "w") as file:
        json.dump(tasks, file, indent=4)

    print(f"Task '{task_name}' added at {time_created}")

add_task()