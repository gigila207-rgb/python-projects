todo_list = {}


def show_menu():
    print("\n" + "=" * 35)
    print("📋        TO-DO LIST")
    print("=" * 35)
    print("1. Add Task")
    print("2. Mark Task as Done")
    print("3. Show Tasks")
    print("4. Delete Task")
    print("5. Exit")


def add_task():
    task = input("\nEnter the new task: ")

    if task in todo_list:
        print("❌ Task already exists!")
    else:
        todo_list[task] = "⏳ Pending"
        print("✅ Task added successfully!")


def mark_task_done():
    if not todo_list:
        print("\n📭 No tasks available.")
        return

    show_tasks()

    task = input("\nEnter the task name: ")

    if task in todo_list:
        todo_list[task] = "✅ Done"
        print("🎉 Task marked as done!")
    else:
        print("❌ Task not found.")


def show_tasks():
    if not todo_list:
        print("\n📭 No tasks in your list.")
        return

    print("\n========== YOUR TASKS ==========")

    for number, (task, status) in enumerate(todo_list.items(), start=1):
        print(f"{number}. {task:<25} {status}")

    print("=" * 32)


def delete_task():
    if not todo_list:
        print("\n📭 No tasks to delete.")
        return

    show_tasks()

    task = input("\nEnter the task to delete: ")

    if task in todo_list:
        del todo_list[task]
        print("🗑️ Task deleted successfully!")
    else:
        print("❌ Task not found.")


while True:
    show_menu()

    try:
        choice = int(input("\nChoose an option: "))
    except ValueError:
        print("❌ Please enter a number between 1 and 5.")
        continue

    if choice == 1:
        add_task()

    elif choice == 2:
        mark_task_done()

    elif choice == 3:
        show_tasks()

    elif choice == 4:
        delete_task()

    elif choice == 5:
        print("\n👋 Goodbye! Have a productive day!")
        break

    else:
        print("❌ Invalid choice. Please choose a number from 1 to 5.")
