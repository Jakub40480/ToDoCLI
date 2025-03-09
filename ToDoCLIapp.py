import time
import json
import random
import os

ids = random.randint(0, 1000)
data_file = "data.json"


def add_task():
    task_name = input("Name of the task: ")
    task_description = input("Description(optional): ")
    time_created = time.ctime()
    time_updated = time.ctime()
    unique_id = ids
    used_ids = []
    if unique_id in used_ids:
        unique_id = ids
    else:
        used_ids.append(unique_id)
    task_status  = input("todo(1), in-progress(2), done(3)")
    task = {
        "ID": unique_id,
        "name": task_name,
        "description": task_description, 
        "time created": time_created,
        "time updated": time_updated,
        "task_status": task_status
    }
    if not os.path.exists(data_file):
        with open(data_file, "w") as file:
            json.dump({}, file)

    with open(data_file, "w") as file:
        json.dump(task, file, indent=4)
    
    print(f"Task '{task_name}' added at {time_created}")

add_task()

