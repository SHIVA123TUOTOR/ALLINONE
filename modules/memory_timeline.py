import json
import os
from datetime import datetime

mem_path = "data/memory.json"

def add_memory(event):
    data = []
    if os.path.exists(mem_path):
        with open(mem_path, "r") as f:
            data = json.load(f)
    data.append({"event": event, "time": datetime.now().isoformat()})
    with open(mem_path, "w") as f:
        json.dump(data, f, indent=4)
    print("Memory added.")

def get_memories():
    if os.path.exists(mem_path):
        with open(mem_path, "r") as f:
            data = json.load(f)
            return data
    else:
        return []
