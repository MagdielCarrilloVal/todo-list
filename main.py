import json
import os

def load_tasks(task):
    with open(archivo='todo.json'):
        if not os.path.exists(archivo):
            return []
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)

def save_tasks():
    
