dict={}
response_list=['y','Y',"YES","yes","Yes"]
while True:
    print("---------------To Do App Maker--------------")
    print("1.Add A task")
    print("2.View all tasks")
    print("3.Delete a task")
    print("4.Exit")
    choice=None
    try:
        choice = int(input("select an option"))
    except ValueError:
        print("please select valid option ")
    if choice==1:
        task_name = input("Enter task name ")
        if task_name in dict:
            print("Task already added Do you want to add something else?")
        else:
            dict[task_name] = input("Enter date")
    elif choice==2:
        if len(dict)==0:
            print("No tasks To do ")
        else:
            for x,y in dict.items():
                print(x,"---",y)
    elif choice==3:
        if len(dict)==0:
            print("No taks to delete")
        else:
            for x,y in dict.items():
                print(x,"---",y)
            option=None
            try:
                option = input("select a task you want to delete by entering task name")
            except ValueError:
                print("invalid option select valid option")
            dict.pop(option)
    elif choice==4:
        print("Bye")
        break
    else:
        print("please select a valid option")
    print("Do you want to continue if yes press y")
    response = input()
    if response not in response_list:
        break