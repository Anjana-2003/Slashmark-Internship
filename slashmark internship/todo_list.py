# Initialize an empty to-do-list
todo_list = []

def show_options():
    print("\nTo-Do List Options")
    print("1. Add a new task")
    print("2. Mark task as completed")
    print("3. View all tasks")
    print("4. Delete tasks")
    print("5. Exit the options")

def create_task(tasks):
    task = input("Enter the task details: ")
    tasks.append({"task": task, "status": False})
    print(f"Task '{task}' added successfully.")

def mark_task_as_complete(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to be completed: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks[task_num]["status"] = "Completed"
                print("Task marked as completed successfully.")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
    else:
        print("\nYour Tasks:")
        index = 1
        # Start the numbering from 1
        for task in tasks:
            status = "Completed" if task["status"] else "Incomplete"
            print(f"{index}. {task['task']} - {status}")
            index += 1
            # Increment the index for the next task

def delete_tasks(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_index = int(input("Enter the index number of the task to be deleted: ")) - 1
            if 0 <= task_index < len(tasks):
                deleted_task = tasks.pop(task_index)
                print(f"Task '{deleted_task['task']}' removed successfully.")
            else:
                print("Invalid task number. Please try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please try once more.")

def main_program():
    while True:
        show_options()
        user_choice = input("Choose any option between (1-5): ")
        if user_choice == "1":
            create_task(todo_list)
        elif user_choice == "2":
            mark_task_as_complete(todo_list)
        elif user_choice == "3":
            view_tasks(todo_list)
        elif user_choice == "4":
            delete_tasks(todo_list)
        elif user_choice == "5":
            print("Program is exiting. Have a great day!")
            break
        else:
            print("Choice is invalid. Please select a valid option.")

if __name__ == "__main__":
    main_program()
