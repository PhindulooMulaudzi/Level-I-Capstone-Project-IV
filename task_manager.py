# Task 1
# Project
from datetime import datetime  # import so that can get current date


# Function used to register new users
def reg_user():
    usernameList = []  # list to store all users
    userFile = open('user.txt', 'r')  # open file with read permissions
    for line in userFile:
        lineSplit = line.split(',')  # split line using ','
        usernameList.append(str(lineSplit[0]))  # save users into list
    userFile.close()  # close file

    userFile = open('user.txt', 'a+')  # open file with read and append permissions
    passWordVerified = False  # Check if password verified
    userNameVerified = False  # Check if user name doesnt already exist
    isRegistered = False

    # Loop to to register new user
    while not isRegistered:
        userName = str(input("Please enter a new username: "))  # request new username
        if userName not in usernameList:  # Check that user doesnt already exist
            userNameVerified = True  # Confirm that user is new and doesnt exists
            if not passWordVerified:  # Check that password is confirmed successfully
                passWord = str(input("Please enter the password: "))
                passWord2 = str(input("Please confirm the password: "))
                if passWord == passWord2:  # Check that password confirmation passses
                    passWordVerified = True  # loop exit condition password confirmed
                    isRegistered = True  # Confirm that new user successfully created
                else:
                    print("Passwords do not match!")
        else:
            print("User name already exists!")

    # If password verified register new user to user.txt
    if passWordVerified:
        userFile.write("\n" + userName + ", " + passWord)  # write username and password to file
        print("New user registered!\n")  # Print message once registered
    userFile.close()  # close file #close file done registering user


# Function to add task
def add_task():
    userName = str(input("Please enter the user the task is assigned to: "))  # request new username
    taskTitle = str(input("Please enter title of the task: "))  # request task title
    taskDescription = str(input("Please enter task description: "))  # request task description

    # get task date from date time assume task due at current date
    dateAssigned = datetime.today().strftime('%d %b %Y')
    dueDate = datetime.today().strftime('%d %b %Y')
    taskComplete = str("No")

    #  read task file to check if end on new line
    with open('tasks.txt') as taskFile:
        text = taskFile.read()

    # write task to task file if taskfile does not end on new line '\n'
    with open('tasks.txt', 'a') as taskFile:
        if not text.endswith('\n'):
            # Write tasks detail to task.txt
            taskFile.write("\n" + userName + ", " + taskTitle + ", " + taskDescription + ", "
                           + str(dateAssigned) + ", " + str(dueDate) + ", " + taskComplete)

    print("New task created!\n")  # Print message once registered


#  Function to ammend change to task text file
def update_task_information(task_list):
    taskFile = open('tasks.txt', 'w')  # open file, clear it and write information

    #  Update text file using loop to write out dictionary to text file
    for dictionary in task_list:
        for key in dictionary:
            if key != "Task Status":
                taskFile.write(str(dictionary[key]) + ", ")
            else:
                taskFile.write(str(dictionary[key]))
        taskFile.write("\n")
    taskFile.close()  # close file once done


#  Function to display user and task overview information
def view_all():
    taskList = load_task()
    taskNumber = 0

    #  Print all task items from dictionary task list
    for dictionary in taskList:
        print("-----Task Number: " + str(taskNumber) + "-----")
        for key in dictionary:
            print(key + ": ", end='')
            print(dictionary[key])
        taskNumber += 1

    #  Query user to option to either select a task or exit task view
    selection = int(input("Please enter a task number or enter '-1' to return to the main menu: "))

    #  Print relevant information based on user selection
    if selection != -1:

        print("Task number: '" + str(selection) + "' selected!\n" + "Task Owner: "
              + taskList[selection]["Task Owner"] + "\n" + "Task Description: " + taskList[selection][
                  "Task Description"]
              + "\n" + "Date Assigned: " + taskList[selection]["Date Assigned"] + "\n" + "Due Date: " +
              taskList[selection][
                  "Due Date"] + "\n" + "Task Status: " + taskList[selection]["Task Status"] + "\n" +
              "d\t-\tMark task as complete.\ne\t-\tEdit task details.\n")

        option = str(input("Please enter your selection either 'e' or 'd': "))  # request user selection
        if option == "d":  # logic for if user choose to mark task done
            taskList[selection]["Task Status"] = "Yes"
        elif option == "e":  # logic for if user choose to edit task
            if taskList[selection]["Task Status"] != "Yes":
                newUser = str(input("Please enter new task owner: "))
                newDueDate = str(input("Please enter new due date 'DD MMMM YYYY': "))
                taskList[selection]["Due Date"] = newDueDate
                taskList[selection]["Task Owner"] = newUser
            else:  # logic if user editing completed task
                print("The task is already completed, you can not edit it!\n")
        update_task_information(taskList)  # call to update task information
    else:
        print("\n\tReturning to main menu.\n")  # Return to menu if user chooses '-1['


# function to view user specific information, require user name parameter to be passed in
def view_mine(username):
    taskList = load_task()  # load all tasks
    mineList = []  # list to contain user specific task
    otherList = []  # list to contain other user taks
    taskNumber = 0  # variable to contain task number

    # loop to separate user specific tasks from all tasks
    for dictionary in taskList:
        if dictionary["Task Owner"] == username:
            print("-----Task Number: " + str(taskNumber) + "-----")
            mineList.append(dictionary)
            taskNumber += 1
            for key in dictionary:
                if dictionary["Task Owner"] == username:
                    print(key + ": ", end='')
                    print(dictionary[key])
        else:  # if task not belong to specific user move to other list
            otherList.append(dictionary)

    #  Query user to option to either select a task or exit task view
    selection = int(input("Please enter a task number or enter '-1' to return to the main menu: "))

    #  Print relevant information based on user selection
    if selection != -1:

        print("Task number: '" + str(selection) + "' selected!\n" + "Task Owner: "
              + taskList[selection]["Task Owner"] + "\n" + "Task Description: " + taskList[selection][
                  "Task Description"]
              + "\n" + "Date Assigned: " + taskList[selection]["Date Assigned"] + "\n" + "Due Date: " +
              taskList[selection][
                  "Due Date"] + "\n" + "Task Status: " + taskList[selection]["Task Status"] + "\n" +
              "d\t-\tMark task as complete.\ne\t-\tEdit task details.\n")

        option = str(input("Please enter your selection either 'e' or 'd': "))  # request user selection
        if option == "d":  # logic for if user choose to mark task done
            mineList[selection]["Task Status"] = "Yes"
        elif option == "e":  # logic for if user choose to edit task
            if mineList[selection]["Task Status"] == "No":
                newUser = str(input("Please enter new task owner: "))
                newDueDate = str(input("Please enter new due date 'DD MMMM YYYY': "))
                mineList[selection]["Due Date"] = newDueDate
                mineList[selection]["Task Owner"] = newUser
            else:  # logic if user editing completed task
                print("The task is already completed, you can not edit it!\n")
        newTaskList = otherList + mineList  # ammend task list with new edited information
        update_task_information(newTaskList)  # call to update task information
    else:
        print("\n\tReturning to main menu.\n")  # Return to menu if user chooses '-1['


# Function to load tasks based on selection
def load_task():
    taskList = []
    keyCounter = 0
    taskFile = open('tasks.txt', 'r')  # open file with read permissions
    for line in taskFile:
        lineSplit = line.split(',')  # split line using ','

        userName = str(lineSplit[0])  # save username
        taskTitle = str(lineSplit[1])  # save task title
        taskDescription = str(lineSplit[2])  # save task description
        dateAssigned = lineSplit[3].strip()  # save task dates
        dueDate = lineSplit[4].strip()
        taskComplete = lineSplit[5].rstrip("\n").strip()  # save task complete status

        taskList.append({"Task Owner": userName, "Task Title": taskTitle, "Task Description": taskDescription,
                         "Date Assigned": dateAssigned, "Due Date": dueDate, "Task Status": taskComplete})

    taskFile.close()  # close file

    return taskList  # return task list


# function to generate task overview report
def task_overview_report():
    taskReport = open("task_overview.txt", 'w')  # open file, clear it and write information
    taskList = load_task()  # load all tasks
    totalTask = len(taskList)  # total task is equal to length of task list

    # defin variable to be used for counting
    taskCompleted = 0
    taskOutstanding = 0
    taskOverdue = 0

    # count task status using dictionary key in for loop
    for dictionary in taskList:
        for key in dictionary:
            if key == "Task Status":
                if dictionary[key] == "No":
                    taskOutstanding += 1
                else:
                    taskCompleted += 1
            if key == "Due Date":
                if dictionary["Task Status"] == "No":
                    # If due date is in the past task is overdue
                    if datetime.strptime(dictionary[key], "%d %b %Y") < datetime.today():
                        taskOverdue += 1
    # write task overview in presentable manner to text file
    taskReport.write(
        "Total number of tasks: " + str(totalTask) + "\nTotal number of completed tasks: " + str(taskCompleted)
        + "\nTotal number of uncompleted tasks: " + str(taskOutstanding) + "\nTotal number of overdue tasks: " + str(
            taskOverdue) + "\nPercentage of tasks that are incomplete: " +
        str(round((taskOutstanding / totalTask) * 100, 0)) + "\nPercentage of tasks that are overdue: " +
        str(round((taskOverdue / totalTask) * 100, 0)))

    taskReport.close()  # close file
    return taskList  # return task list to be used by report function


# function to display user task overview
def user_overview_report(user_name, task_list):
    userReport = open("user_overview.txt", 'w')  # open file, clear it and write information
    userList = []  # list to store all users

    # Read user text file to determine number of users
    userFile = open('user.txt', 'r')  # open file with read permissions
    for line in userFile:
        lineSplit = line.split(',')  # split line using ','
        userList.append(str(lineSplit[0]))  # save users into list
    userFile.close()  # close file

    # variable to store count of user specific task activity
    totalUserTasks = 0
    userTaskOverdue = 0
    userTaskOutstanding = 0
    userTaskCompleted = 0
    totalTask = len(task_list)

    # count task status using dictionary key in for loop
    for dictionary in task_list:
        for key in dictionary:
            if key == "Task Owner" and dictionary[key] == user_name:
                totalUserTasks += 1
                if dictionary["Task Status"] == "No":
                    if datetime.strptime(dictionary["Due Date"], "%d %b %Y") < datetime.today():
                        userTaskOverdue += 1

                if dictionary["Task Status"] == "No":
                    userTaskOutstanding += 1
                else:
                    userTaskCompleted += 1

            if key == "Task Owner":
                userList.append(dictionary[key])

    userList = list(set(userList))  # make user list unique

    # write use overview report in presentable manner
    userReport.write("Total number of users registered: " + str(len(userList)) + "\nTotal number of tasks: "
                     + str(totalTask) + "\nTotal number of tasks assigned to " + user_name + ": " + str(totalUserTasks)
                     + "\nPercentage of total number of tasks assigned to " + user_name + ": "
                     + str(round((totalUserTasks / totalTask) * 100, 0))
                     + "\nPercentage of tasks assigned to " + user_name + " completed: "
                     + str(round((userTaskCompleted / totalUserTasks) * 100, 0)) + "\nPercentage of " + user_name
                     + "'s tasks that are incomplete: " +
                     str(round(((totalUserTasks - userTaskCompleted) / totalUserTasks) * 100, 0))
                     + "\nPercentage of " + user_name + "'s tasks that are overdue: " + str(
        round((userTaskOverdue / totalUserTasks) * 100, 0)))

    userReport.close()  # close file


# function to generate report, both for user and tasks
def generate_reports(user_name):
    user_overview_report(user_name, task_overview_report())


# Function to view statistics if admin user logged in
def view_statistics(user_name):
    generate_reports(user_name)  # call function to generate all reports

    # read task overview from text file generate by report function
    taskOverviewFile = open('task_overview.txt', 'r')  # open file with read permissions

    # print in presentable manner
    print("--------Task Overview Summary for Task Manager.py--------")
    for line in taskOverviewFile:
        print(line, end="")
    taskOverviewFile.close()

    # read user overview from text file generate by report function
    userOverviewFile = open('user_overview.txt', 'r')  # open file with read permissions

    # print in presentable manner
    print("\n\n--------" + user_name + "'s Overview Summary for Task Manager.py--------")
    for line in userOverviewFile:
        print(line, end="")
    userOverviewFile.close()


# Function to load login details into value key dictionary
def load_login_details():
    # Declare dictionary to store user names and password as value key
    loginDetails = {}

    # open user name text file to load users and passwords into program
    userFile = open('user.txt', 'r')  # open file as read only

    for line in userFile:
        lineSplit = line.split(',')  # split line using ','
        # Save username and password as a dictionary data type called login details
        # username is the key, and the value item is the password
        loginDetails[lineSplit[0].strip(' ')] = lineSplit[1].replace(" ", "").rstrip('\n')

    userFile.close()  # close file
    return loginDetails


# login function that handles user authentication and prints welcome message
def login():
    # Program welcome message, request user to login
    print("Welcome!, Please login first before you can use the program.\n")
    isLogin = False  # boolean value to track login condition

    # Loop to request user to login until correct login details are entered
    while not isLogin:
        userName = str(input("Please enter a valid username: "))  # Request user name input
        # Validate username and password
        if userName in load_login_details():
            passWord = str(input("Please enter your password: "))  # Request passwprd input
            if load_login_details()[userName] == passWord:
                isLogin = True
            else:
                print("\tInvalid password detected!")  # Error if password invalid
        else:
            print("\tInvalid username detected!")  # Error if username invalid
    return userName  # Return name of user that is currently logged in


# Declare program main function that constantly loops
def main():
    userName = login()  # Authenticate user and save current username
    while True:
        # Print program main menu based on user logged in
        if userName != "admin":
            # normal main menu
            print("\nPlease select one of the following options:\nr	-	register user\n"
                  "a	-	add task\nva	-	view all tasks\nvm	-	view my tasks\ne	-	exit")
            option = str(input("\nPlease enter selection: "))  # save user selection
        else:
            # admin main menu
            print("\nPlease select one of the following options:\nr\t-   register user\n"
                  "a\t-   add task\nva\t-   view all tasks\nvm\t-   view my tasks"
                  "\nds\t-   display statistics\ngr\t-   generate reports\ne\t-   exit")
            option = str(input("\nPlease enter selection: "))  # save user selection

        # Evaluate input selection and call relevant function
        if option == "r":
            if userName == "admin":
                reg_user()
                print("*****Program execution completed, returning to main menu.*****")
            else:
                print("*****Insufficient privileges, returning to main menu.*****")
        elif option == "a":
            add_task()
            print("*****Program execution completed, returning to main menu.*****")
        elif option == "va":
            view_all()
            print("*****Program execution completed, returning to main menu.*****")
        elif option == "vm":
            view_mine(userName)  # view task of user that is currently logged in
            print("*****Program execution completed, returning to main menu.*****")

        elif option == "ds":
            if userName == "admin":
                view_statistics(userName)  # view statistics
                print("\n*****Program execution completed, returning to main menu.*****")
            else:
                print("*****Insufficient privileges, returning to main menu.*****")
        elif option == "e":
            print("*****Program will now terminate, Goodbye.*****")
            exit()  # Terminate program
        elif option == "gr":
            if userName == "admin":
                generate_reports(userName)  # view statistics
                print("*****Program execution completed, returning to main menu.*****")
            else:
                print("*****Insufficient privileges, returning to main menu.*****")
        else:
            print("Invalid selection!")  # invalid selection message


# -----------------------------Program loop------------------------------------#
main()  # call program main function
