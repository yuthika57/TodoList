import sys
import os

# Make sure at least one command is passed
if len(sys.argv) < 2:
    print("Error: Missing command.")
    sys.exit(1)

# adding tasks
if sys.argv[1] == "add":
    if len(sys.argv) < 3 or len(sys.argv[2].strip()) == 0:
        print("Error: Missing task to add.")
        sys.exit(1)
    
    task = sys.argv[2]
    with open("tasks.json", "a") as js:
        line = '{ "task": "' + task + '", "done": false }\n'
        js.write(line)
    print("Task successfully added!")

# listing
elif sys.argv[1] == "list":
    with open("tasks.json", "r") as js:
        for line in js:
            print(line.strip())
    print("All tasks have been printed successfully!")


elif sys.argv[1] == "done":
    if len(sys.argv) < 3 or len(sys.argv[2].strip()) == 0:
        print("Error: Missing task to mark as done.")
        sys.exit(1)

    task = sys.argv[2]
    original = '{ "task": "' + task + '", "done": false }'
    updated = '{ "task": "' + task + '", "done": true }'

    with open("tasks.json", "r") as js, open("temp.json", "w") as tmp:
        for line in js:
            if line.strip() == original:
                tmp.write(updated + "\n")
            else:
                tmp.write(line)

    with open("temp.json", "r") as file, open("tasks.json", "w") as js:
        for line in file:
            js.write(line)

    os.remove("temp.json")
    print("Task marked as done!")
      

# removing
elif sys.argv[1] == "remove":
    if len(sys.argv) < 3 or len(sys.argv[2].strip()) == 0:
        print("Error: Missing task to remove.")
        sys.exit(1)
    
    removetask = sys.argv[2]
    removecon = '{ "task": "' + removetask + '", "done": false }'
    
    with open("tasks.json", "r") as js, open("temp.json", "w") as tmp:
        for line in js:
            if line.strip() != removecon.strip():
                tmp.write(line)

    with open("temp.json", "r") as file, open("tasks.json", "w") as f:
        for line in file:
            f.write(line)

    os.remove("temp.json")
    print("Task successfully removed!")

else:
    print("Error: Unknown command.")
