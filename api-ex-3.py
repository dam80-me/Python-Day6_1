import requests
import json

BASE_URL ="http://localhost:8000/tasks"

def create_new_task():
    """Creates a new task by sending a POST request to the API."""
    print("--- Creating a new task ---")
    new_task_data = {
        "title": "Plan weekend trip",
        "description": "Research destinations, book flights, arrange",
        "status": "pending",
        "dueDate": "2025-07-15"
    }

    try:
        response = requests.post(BASE_URL, json=new_task_data)
        response.raise_for_status() # Raise an exception for HTTP er
        created_task = response.json()
        print("Task created successfully:")
        print(json.dumps(created_task, indent=2))
    except requests.exceptions.HTTPError as e:
        print(f"Error creating task: {e}")
        if e.response.status_code==400:
            print(f"Bad Request: {e.response.json().get('error', 'unknown')} not found.")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to API: {e}")

create_new_task()
