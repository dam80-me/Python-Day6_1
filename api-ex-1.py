import requests
import json
import time # To add a small delay between requests if needed

BASE_URL ="http://localhost:8000/tasks"

def bulk_create_tasks(num_tasks=5):
    """Creates a specified number of new tasks."""
    print(f"---Bulk creating {num_tasks} new tasks ---")
    for i in range(num_tasks):
        task_data ={
            "title": f"Auto-generated Task {i+1}",
            "description": f"This is an automated task number {i+1}",
            "status": "pending",
            "dueDate": f"2025-07-{20+i:02d}" #Example:due dates
        }
    try:
        response = requests.post(BASE_URL, json=task_data)
        response.raise_for_status()
        created_task = response.json()
        print(f"Created Task {i+1}: {created_task['title']}")
    except requests.exceptions.RequestException as e:
        print(f" Error creating task {i+1}: {e}")

"""def get_tasks_by_status (status):
    """#Fetches and prints"""
    #print(f"--- Getting tasks with status: '{status}' ---")
    #params = {'status'}"""