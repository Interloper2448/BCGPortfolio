import task_list_storage as storage
import copy


class TaskList:
    def __init__(self, listData):
        self.name = listData[0]
        self.__listData = listData
        self.tasks = listData[1:len(listData)-1:2]
        self.taskStatus = listData[2:len(listData):2]
        # print("PING", listData)
        # print("LenListData", len(listData))
        # print("self.tasks:", self.tasks)
        # print("Lenself.tasks:", len(self.tasks))
        # print("self.taskStatus:", self.taskStatus)
        # print("Lenself.taskStatus:", len(self.taskStatus))

    # def addTaskList(self, name):
        # prevList = storage.readData()
        # print(prevList)

    # def resetTaskList(self, listData):
    #     self.tasks = listData[1:len(listData[0])-1:2]
    #     self.taskStatus = listData[2:len(listData[0])-1:2]

    # def __str__(self):
    #     return self.__listData[0]

    def getListData(self):
        return self.__listData

    def taskComplete(self, taskIndex):
        # print("Entered Task Complete Method")
        # print("PING:",self.__listData)
        self.taskStatus[taskIndex] = "True"
        self.__listData[taskIndex * 2 + 2] = "True"
        storage.updateList(self.__listData)
        # print(self.__listData)


def main():
    print("\n\r**********************************")
    print("Welcome to the task_List Object Tester")
    listIndex = 0
    # taskIndex = 2
    print()
    allLists = storage.readLists()
    print("All task lists:", allLists)
    print("Lookup for index ", listIndex, ": ", allLists[listIndex], sep="")

    listdata = []
    listdata = storage.readData()
    # print("Raw Data:",listdata[0])#Prints out what is in the selected task list

    curTask = TaskList(listdata[listIndex])

    print("Current Task List:", curTask.name)
    print("Tasks in list:", curTask.tasks)
    print("Status of tasks in list:", curTask.taskStatus)
    print("Ping", storage.readData())
    # storage.delTask("p1","p2")#curTask,curTask.tasks[taskIndex])
    # taskList, taskName, file = "task_list_OfTasks.csv")


if __name__ == "__main__":
    main()
