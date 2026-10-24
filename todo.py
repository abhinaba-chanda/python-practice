import json, os

FILE = "todos.json"

def load():
    return json.load(open(FILE)) if os.path.exists(FILE) else []

def save(items):
    json.dump(items, open(FILE, "w"), indent=2)

items = load()
while True:
    cmd = input("add / list / done / quit: ").strip()
    if cmd == "add":
        items.append({"task": input("Task: "), "done": False})
    elif cmd == "list":
        for i, t in enumerate(items, 1):
            print(i, "[x]" if t["done"] else "[ ]", t["task"])
    elif cmd == "done":
        items[int(input("Number: ")) - 1]["done"] = True
    elif cmd == "quit":
        break
    save(items)
