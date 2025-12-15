
def add_tasks():
    """a function to add tasks to tasks list to be done"""
    items =  input("add a task: ")
    print(f" '{items}' has been added to the list \n \n")
    tasks.append(items)

def display():
    """a function to display existing tasks"""

    if not tasks:
        print("no tasks has been added")
    
    if completed_task:
        print_completed_task()

    else:
        for index, items in enumerate(tasks):
            print(f"{index+1}. {items}")

   
    print("\n\n")
                  

def delete():
    task_delete = int(input("enter a task to delete: "))
    print(f"{tasks[task_delete-1]} has been deleted ")
    tasks.pop(task_delete-1)
   
# def complete():
#     done = int(input("enter the number of the activity you're done with: "))
#     completed_task.append(tasks[done-1]) 
#     return done
           


def print_completed_task():  
    """prints out the list with the indicated completed task""" 
    done = int(input("enter the number of the activity you're done with: "))
    completed_task.append(tasks[done-1]) 
    for items in tasks:
        if items == tasks[done-1]:
             print(f"{tasks[done-1]} -------- [x]")
        else:
            print(items)



def quit():
    to_false = False

tasks = []
completed_task = []






to_do = True
while to_do:
    print("--------------------------------")
    print("1. Add tasks")
    print("2. Display task")
    print("3  Delete tasks")
    print("4  mark complete")
    print("--------------------------------\n\n")
   
    action = int(input("enter the number associated to task you wish to perform: "))
    if action == 1:
        add_tasks()

    elif action == 2:
         display()

    elif action == 3:
        display()
        delete()

    elif action == 4:
        print_completed_task()

    # elif action == 4:
    #     quit()











