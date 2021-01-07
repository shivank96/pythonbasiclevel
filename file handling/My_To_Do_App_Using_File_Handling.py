li=[]
response_list=['y','Y',"YES","yes","Yes"]
while True:
    print("---------------To Do App Maker--------------")
    print("1.Add A task")
    print("2.View all tasks")
    # print("3.Delete a task")
    print("3.Exit")
    choice=None
    try:
        choice = int(input("select an option"))
    except ValueError:
        print("please select valid option ")
    if choice==1:
        f = open("Taskslist.txt", "r")
        task_name=input("Enter your task name ")
        res=f.read()
        f.close()
        if task_name in res:
            print("Task already added Do you want to add something else?")
        else:
            with open("Taskslist.txt","a") as f:
                li.append(task_name)
                f.write("\n")
                f.writelines(task_name)
    elif choice==2:
        with open("Taskslist.txt", "r") as f:
            res=f.read()
            if len(res)==0:
                print("No tasks To do ")
            else:
                for x in res:
                    for y in x:
                        print(y,end="")
                print()
    # elif choice==3:
    #     with open("Taskslist.txt", "r") as f:
    #         res=f.read()
    #         if len(res)==0:
    #             print("No taks to delete")
    #         else:
    #             counter = 0
    #             for x in li:
    #                 counter+=1
    #                 print(counter,x)
    #     option=None
    #     try:
    #         option = int(input("select a task you want to delete"))
    #     except ValueError:
    #         print("invalid option select valid option")
    #     li.remove(li[option-1])
    elif choice==3:
        break
    else:
        print("please select a valid option")
    print("Do you want to continue if yes press y")
    response = input()
    if response not in response_list:
        break