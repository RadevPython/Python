# To-Do list application created by RadevPy 
import time

time.sleep(1)
print("To-Do list application created by RadevPy")
time.sleep(1)



task_list = []

def add_task():
    enter_task = input("Enter task: ")
    task_list.append(enter_task)

def remove_task():
    rem_task = input("Enter task to remove: ")
    if rem_task in task_list:
        task_list.remove(rem_task)
    else:
        print("This task doesn't exist")

def view_task():
    print(task_list)


while True:
    print("Main Menu")
    print("1: Add task")
    print("2: Remove task")
    print("3: View Task")
    print("4: Exit")
    ch=int(input("Enter your choose: "))
    if ch == 1:
        add_task()
    elif ch == 2:
        remove_task()
    elif ch == 3:
        view_task()
    elif ch == 4:
        break
    else:
        print("Invalid input, Try again.")

