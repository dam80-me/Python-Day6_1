import requests
import json

BASE_URL ="http://localhost:8000/tasks"

def partial_update_task(task_id):
    url =f"{BASE_URL}/{task_id}"
    # Only send the feilds you want to change
    patch_data={
        "status": "completed"
    }
    
    try:
        response = requests.patch(url, json=patch_data)
        response.raise_for_status() # Raise an exception for HTTP er
        updated_task = response.json()
        print(f"Task {task_id} partially updated successfully:")
        print(json.dumps(updated_task, indent=2))
    except requests.exceptions.HTTPError as e:
        print(f"Error partially updating task {task_id}: {e}")
        if e.response.status_code==400:
            print(f"Not Found: Task with ID '{task_id}' not found.")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to API: {e}")
    print("-"*30)

#partial_update_task(task_id=123)
    
if __name__== "__main__":
    # Ensure 'task456' exists or run 'get_tasks.py' and 'post_task.py'
    partial_update_task("task456")
    partial_update_task("noneexistent_task_for_patch") # Will result
