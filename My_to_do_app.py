li=[]
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
        task_name=input("Enter your task name ")
        if task_name in li:
            print("Task already added Do you want to add something else?")
        else:
            li.append(task_name)
    elif choice==2:
        if len(li)==0:
            print("No tasks To do ")
        else:
            for x in li:
                print(x)
    elif choice==3:
        if len(li)==0:
            print("No taks to delete")
        else:
            counter = 0
            for x in li:
                counter+=1
                print(counter,x)
            option=None
            try:
                option = int(input("select a task you want to delete"))
            except ValueError:
                print("invalid option select valid option")
            li.remove(li[option-1])
    elif choice==4:
        break
    else:
        print("please select a valid option")
    print("Do you want to continue if yes press y")
    response = input()
    if response not in response_list:
        break