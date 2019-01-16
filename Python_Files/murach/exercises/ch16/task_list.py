import objects
import task_list_storage as storage


def listTasks(other=False):
    allLists = storage.readLists()
    for listIndex in range(0, len(allLists)):
        print(listIndex + 1, ": ", allLists[listIndex], sep="")
    if other:
        print(listIndex+2, ": New List", sep="")

    print()


def display_main_menu():
    print("The Task List program")
    print()
    print("COMMAND MENU")
    print("help - Show all commands")

    # print("expa - Show tasks in specific list") #@Depricated switched to list
    print("add -  Adds a new list or task")
    print("del -  Deletes a list or task")
    print("list - List all task lists")
    print("comp -  Marks a task as complete")
    print("exit - Exit program")
    print()


# def display_task_menu():
#     print("The Task List program")
#     print()
#     print("COMMAND MENU")
#     print("help - Show all commands")
#     print("list - List all tasks for current list")
#     print("comp - Mark task as completed")
#     print("mod -  change a specific list of tasks")
#     print("del - Delete a task")
#     print()


def main():
    print("\n\r**********************************")
    print("Welcome to the Task List Program")
    display_main_menu()

    listData = []
    listData = storage.readData()

    while True:
        command = input("Command: ")
        if command == "help":
            display_main_menu()
        elif command == "add":
            listData = storage.readData()
            addData(listData)
        elif command == "del":
            print("Command not implemented\n\r")
        elif command == "list":
            listData = storage.readData()
            expandList(listData)
        elif command == "comp":
            listData = storage.readData()
            compTask(listData)

        # elif command == "expa":
        #     expandList(listData)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")


def addData(listData):
    allLists = storage.readLists()
    print("Which List would you like to add to?")
    listTasks(True)
    command = int(input("Command: "))
    listIndex = command - 1
    # print("Index",listIndex,"Length",len(allLists))
    if listIndex > -1 and listIndex < len(allLists):
        print("Add value to existing list")
        newTaskName = input("Task Name: \t\t")
        data = storage.readData()
        data[listIndex].append(newTaskName)
        data[listIndex].append("False")
        storage.writeData(data)

    elif listIndex == len(allLists):
        newListName = [input("List Name: \t\t")]

        data = storage.readData()
        data.append(newListName)
        storage.writeData(data)
    else:
        print("Command", command, "is not valid")


def delData(listData):
    allLists = storage.readLists()
    print("Which List would you like to add to?")
    listTasks(True)
    command = int(input("Command: "))
    listIndex = command - 1
    # print("Index",listIndex,"Length",len(allLists))
    if listIndex > -1 and listIndex < len(allLists):
        print("Add value to existing list")
        newTaskName = input("Task Name: \t\t")
        data = storage.readData()
        data[listIndex].append(newTaskName)
        data[listIndex].append("False")
        storage.writeData(data)

    elif listIndex == len(allLists):
        newListName = [input("List Name: \t\t")]

        data = storage.readData()
        data.append(newListName)
        storage.writeData(data)
    else:
        print("Command", command, "is not valid")



def compTask(listData):
    allLists = storage.readLists()
    print("Which list has a task that is complete?")
    listTasks()
    command = int(input("Command: "))
    listIndex = command - 1
    if listIndex > -1 and listIndex < len(allLists):
        print("Valid Command", allLists[listIndex])
        curTask = objects.TaskList(listData[listIndex])
        for taskIndex in range(0, len(curTask.tasks)):
            if curTask.taskStatus[taskIndex] == "True":
                status = "Complete"
            else:
                status = "Incomplete"
            print(taskIndex+1, ": ",
                  curTask.tasks[taskIndex], "\t\tStatus:", status, sep="")

        print("Which task is complete?")
        command = int(input("Command: "))
        taskIndex = command - 1
        if taskIndex > -1 and taskIndex < len(listData):
            curTask = objects.TaskList(listData[listIndex])
            curTask.taskComplete(taskIndex)

        else:
            print("Invalid indexer of", taskIndex)

    else:
        print("Invalid indexer of", listIndex)


def expandList(listData):
    allLists = storage.readLists()
    print("Which list would you like to expand?")
    listTasks()
    command = int(input("\tExpan: "))
    listIndex = command - 1
    if listIndex > -1 and listIndex < len(allLists) and len(allLists[listIndex]) > 0:
        # print("Valid Command", allLists[listIndex])
        curTask = None
        curTask = objects.TaskList(listData[listIndex])
        # curTask.resetTaskList(listData[listIndex])
        # print("Length:",len(curTask.taskStatus),curTask.taskStatus)
        for taskIndex in range(0, len(curTask.tasks)):
            # print("Indexing:",taskIndex)
            if curTask.taskStatus[taskIndex] == "True":
                status = "Complete"
            else:
                status = "Incomplete"
            print("Task: ", curTask.tasks[taskIndex], "\t\tStatus:", status)
        print()

    else:
        print("Invalid indexer of", listIndex)


if __name__ == "__main__":
    main()
