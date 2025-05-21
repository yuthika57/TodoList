import sys
import os

if sys.argv[1] == "add":
    with open("f1.txt", "a") as f:
        f.write(sys.argv[2] + "\n")
        print("Task Successfully added!")

elif sys.argv[1] == "list":
    with open("f1.txt", "r") as f:
        for index, line in enumerate(f):
            print(index, line.strip())

else:  # treat any other command as a remove attempt for now
    with open("f1.txt", "r") as f:
        with open("temp.txt", "w") as fi:
            for line in f:
                # FIXED: strip both line and input for clean comparison
                if line.strip() != sys.argv[2].strip():
                    fi.write(line)

    # copy temp back into f1.txt
    with open("temp.txt", "r") as file:
        with open("f1.txt", "w") as f:
            for line in file:
                f.write(line)
    os.remove("temp.txt")
    print("Task Successfully removed!")

                 
                 

   

