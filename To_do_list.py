import os

# Function to display the menu
def display_menu():
    print("To-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

# Function to view the current To-Do List
def view_todo_list(todo_list):
    if not todo_list:
        print("Your To-Do List is empty.")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

# Function to add a task to the To-Do List
def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added successfully.")

# Function to mark a task as completed
def mark_completed(todo_list):
    view_todo_list(todo_list)
    index = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= index < len(todo_list):
        print(f"Task '{todo_list[index]}' marked as completed.")
        del todo_list[index]
    else:
        print("Invalid task number.")

# Function to delete a task from the To-Do List
def delete_task(todo_list):
    view_todo_list(todo_list)
    index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= index < len(todo_list):
        print(f"Task '{todo_list[index]}' deleted.")
        del todo_list[index]
    else:
        print("Invalid task number.")

# Main function
def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            view_todo_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            mark_completed(todo_list)
        elif choice == "4":
            delete_task(todo_list)
        elif choice == "5":
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
