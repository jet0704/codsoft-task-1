# todo_list.py

# Define an empty to-do list
todo_list = []

# Function to create a new to-do list
def create_todo_list():
    global todo_list
    todo_list = []

# Function to add tasks to the to-do list
def add_task(task):
    todo_list.append({"task": task, "completed": False})

# Function to remove tasks from the to-do list
def remove_task(task):
    global todo_list
    todo_list = [t for t in todo_list if t["task"] != task]

# Function to mark tasks as completed
def mark_completed(task):
    for t in todo_list:
        if t["task"] == task:
            t["completed"] = True
            break

# Function to display the to-do list
def display_todo_list():
    for index, task in enumerate(todo_list):
        completed = "[Task Completed]" if task["completed"] else "[Task Not Completed]"
        print(f"{index + 1}. {completed} {task['task']}")

# Main function to run the application
def main():
    create_todo_list()
    while True:
        print("\nTo-Do List")
        print("----------")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Completed")
        print("4. Display Tasks")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            task = input("Enter task: ")
            add_task(task)
        elif choice == 2:
            task = input("Enter task: ")
            remove_task(task)
        elif choice == 3:
            task = input("Enter task: ")
            mark_completed(task)
        elif choice == 4:
            display_todo_list()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()