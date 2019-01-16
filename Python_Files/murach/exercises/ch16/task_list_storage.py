import csv
from pathlib import Path
from os import path
import objects


def getDir(file):
    myFile = []
    myFile = path.split(__file__)
    return myFile[0] + "\\" + file


def writeData(data, file="task_list_OfTasks.csv"):
    path = Path(getDir(file))
    if path.is_file():
        with open(path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
    else:
        raise Exception("Bad File ya Tried to reach there of:\n\r", path)


def readData(file="task_list_OfTasks.csv"):
    path = Path(getDir(file))
    if path.is_file():
        data = []
        with open(path, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data
    raise Exception("Bad File ya Tried to reach there of:\n\r", path)


def readLists(file="task_list_OfTasks.csv"):
    path = Path(getDir(file))
    if path.is_file():
        data = []
        with open(path, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                # data.append(row)
                data.append(row[0])
        return data
    raise Exception("Bad File ya Tried to reach there of:\n\r", path)


def updateList(curTaskList):
    allLists = readLists()
    for listIndex in range(0, len(allLists)):
        if curTaskList[0] == allLists[listIndex]:
            data = readData()
            data[listIndex] = curTaskList
            writeData(data)
            # print("Data:",data)
            # print("GetData",readData())
    # print("GetData", readData())



def delTask(taskList, taskName):
    print("taskList", taskList, "\n\rtaskName", taskName)


def main():
    print("\n\r**********************************")
    print("Welcome to the task_List Object Tester")

    listdata = []
    listdata = readData()
    listIndex = 1
    curTask = objects.TaskList(listdata[listIndex])

    print("Current Task List:", curTask)
    updateList(curTask)


if __name__ == "__main__":
    main()
