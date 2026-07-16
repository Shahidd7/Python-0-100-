import json
tasks = []
try:
    with open("tasks.json" ,"r") as file:
        tasks = json.load(file)
        print("previous tasks loaded successfully")
except FileNotFoundError:
    pass
while True:
    print("--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Tasks:")
    print("5. Save and Quit")
    choice = int(input("enter your choice 1-5:"))
    if (choice == 1):
        task = input("Enter the Task title:")
        task_dict = {"title": task, "is_completed":False}
        tasks.append(task_dict)
    elif (choice == 2):
        for task in tasks:
            if task["is_completed"]:
                status = "x"
            else:
                status = " "
            print(f"[{status}] {task['title']}")
    elif (choice == 3):
        task_title = input("enter the task which you want to mark as complete:")
        for task in tasks:
            if task['title'] == task_title:
                task['is_completed'] = True
                print("Task marked as complete.")
                break
        else:
            print("Task not Found")                
        
    elif (choice == 4):
        task_delete = input("enter the task which you want to delete:")
        for task in tasks:
            if task['title'] == task_delete:
                tasks.remove(task)
                print('task is deleted succesfully')
                break
        else:
            print("Task not Found")
        
    else:
        with open ("tasks.json" , "w") as file:
            json.dump(tasks , file)
        print("File saved successfully.")
        break