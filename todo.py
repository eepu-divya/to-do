FILENAME = "tasks.txt"

def load_tasks():
    tasks = []
    file_exists = False
    try:
        file = open(FILENAME, "r")
        file_exists = True
    except:
        file_exists = False

    if file_exists:
        for line in file:
            tasks.append(line.strip())
        file.close()
    return tasks

def save_tasks(tasks):
    file = open(FILENAME, "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()

def add_task(tasks):
    task = input("Enter a new task: ")
    task = task.strip()
    if task != "":
        tasks.append(task)

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        for i in range(len(tasks)):
            print(str(i+1) + ". " + tasks[i])

def remove_task(tasks):
    view_tasks(tasks)
    num = input("Enter task number to remove: ")
    if num.isdigit():
        index = int(num) - 1
        if index >= 0 and index < len(tasks):
            tasks.pop(index)
            print("Removed task.")
        else:
            print("Invalid task number.")
    else:
        print("Please enter a number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            print("Exited!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
