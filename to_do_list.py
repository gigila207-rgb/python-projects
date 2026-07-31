todo_list = {}
while True:
    print("""
==== TO-DO LIST ====
1. Add Task
2. Mark Task as Done
3. Show Tasks
4. Delete Task
5. Exit  """)
    choice = int(input("choose: "))

    if choice == 1:
        add_task = input("Add new task: ")
        status = input("status (done / pending): ")
        todo_list[add_task] = status

    elif choice == 2:
        for task, status in todo_list.items():
            print(f"{task} - {status}")
        task = input("choose a task: ")
        if task in todo_list:
            todo_list[task] = "✅"
        else:
            print("Task not found.")

    elif choice == 3:
        for task, status in todo_list.items():
            print(f"{task} - {status}")

    elif choice == 4:
        del_task = input("Choose a task to delete: ")
        if del_task in todo_list:
            del todo_list[del_task]
        else:
            print("Task not found.")

    elif choice == 5:
        print("Goodbye!")
        break
         
     
        
  




   
  


































