tasks=[]

def addTask():
    task=input("Enter a Task: ")
    tasks.append(task)
    print("Task '{task}' added to the list.")

def listTask():
    if not tasks:
        print("No tasks available !")
    else:
        print("Available tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deleteTask():
    listTask()
    try:
        taskToDelete=int(input("Enter the task number{#} to be deleted:"))
        if taskToDelete >=0 and len(tasks):
            tasks.pop(taskToDelete)
            print("Task has been deleted")
        else:
            print("Task #{taskToDelete} was not found.")
    except:
        print("Invalid input")

if __name__=="__main__":
    print("Welcome to the to do list:")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("__________________________________________")
        print("1.Add a new task")
        print("2.Delete a task")
        print("3.List tasks")
        print("4.Quit")


        choice=input("Enter your choice:")

        if(choice == "1"):
            addTask()
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            listTask()
        elif(choice == "4"):
            break
        else:
            print("Invalid input.Try again !!!")
    print("Thankyou !!!")
