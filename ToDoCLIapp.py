import time
import json
import random
import os

IDs = random.randint(0, 1000)
data_file = "data.json"


def add_task():
    task_name = input("Name of the task: ")
    task_description = input("Description(optional): ")
    time_created = time.ctime()
    time_updated = time.ctime()
    unique_id = IDs
    used_ids = []
    if unique_id in used_ids:
        unique_id = IDs
    else:
        used_ids.append(unique_id)
    while True:
        try:
            task_status = int(input("todo(1), in-progress(2), done(3): "))
        except ValueError:
            pass
        if task_status not in range(1, 4):
            print("Invalid input for task status. Please enter 1, 2, or 3.") 
        else:
            task_status = str(task_status)
            if task_status == "1":
                task_status == "todo"
            elif task_status == "2":
                task_status == "in-progress"
            else:
                task_status = "done"
            break

    task = {
        "ID": unique_id,
        "name": task_name,
        "description": task_description, 
        "time created": time_created,
        "time updated": time_updated,
        "status": task_status
    }
    if not os.path.exists(data_file):
        with open(data_file, "w") as file:
            json.dump({}, file)

    with open(data_file, "w") as file:
        json.dump(task, file, indent=4)
    
    print(f"Task '{task_name}' added at {time_created}")

add_task()

