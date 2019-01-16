# There is no starting point for the exercise for this chapter.

Definitions:
Task

Data Attributes:
    taskName
    taskListName  
    taskDescription
    taskCompleted
    taskData

Classes:
    taskList    (List of tasks)
    Tasks       (individual tasks)

Methods:
    getTasks        (connects to a CSV file based on taskListName)
    getTaskLists    (connects to a static CSV file task_List.csv)
    ^ ^^ > combined into readData with default file being static csv file
    addTask
    addTaskList
    removeTask
    removeTaskList
    listTasks
    listTaskList

Python Files:
    objects     (Stores all classes)
    taskList    (Official program)
    CSV Files:
        1 for all the tasks         Singular file
        1 for each task list        might have many

