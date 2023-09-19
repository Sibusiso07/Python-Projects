from datetime import datetime

while True:
    user_name = input("Enter your username: ")
    pass_word = input("Enter your password: ")
# The condition that has to be met in order to login successfully
    access = user_name + ", " + pass_word
# Opening the user text file to check if the username and password are correct.
    with open("user.txt" , "r") as f:
        grant_access = False
        for line in f:
            if access in line:
                grant_access = True
                break
    if grant_access == True:
        print("Welcome, " + user_name)
        break
    elif grant_access == False:
        print("Incorrect Username or Password")

def main_menu():
    while True:
        if user_name != "admin":
            print("\n")
            menu = input('''Select one of the following Options below:
        # r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - View my task
        e - Exit
        : ''').lower()
        else:
            print("\n")
            menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - View my task
        gr - Generate reports
        ds - Display statistics
        e - Exit
        : ''').lower()

        if menu == "r":
            reg_user()
        elif menu == "a":
            add_task()
        elif menu == "va":
            view_all()
        elif menu == "vm":
            view_mine()
        elif menu == "gr":
            generate_reports()
        elif menu == "ds":
            display_statistics()
        elif menu == 'e':
            print('Goodbye!!!')
            exit()
        else:
            print("You have made a wrong choice, Please Try again")
            

# Register a new user function
def reg_user():
    print("\n")
    if user_name != "admin":
        print("You do not have the right to register users!")
    else:
        username = input("Please enter the username: ").lower()
        data_file = open("user.txt", "r+") 
        for line in data_file:
            if username == line:
                print("Username already exist!")
                return
        password = input("Please enter the password: ")
        password1 = input("Please confirm the password: ")

        if password1 == password:
            with open('user.txt', 'a') as f:
                f.write(username + ", " + password + ("\n"))
            f.close
        else:
            print("Password mismatch, please confirm the password.")

# Function to add tasks and also it returns the total number of tasks                
def add_task():
    total_tasks = 2
    
    print("Please enter either Yes or No. \n")    
    task = input("Do you wish to create a new Task: ").lower()
        
    if task == "yes":
        person = input("Please enter the username of the person whom the task is assigned: ")
        title= input("Please enter the Title of the task: ")
        descrip = input("Please enter the task description: ")
        current_date = input("PLease enter the current date: ")
        due_date = input("Please enter the task due date: ")
        task_complete = input("Is the task complete (Yes or No): ")

        with open('tasks.txt', 'a') as f:
            f.write(person + "," + title + "," + descrip + "," + current_date + "," + due_date + "," + task_complete + ("\n"))
        f.close()
        print("Adding of new task is complete.")
        
        total_tasks += 1
    else:
        print("No new task has been added.")
    
    return total_tasks

returned_total = add_task()

#View all tasks function        
def view_all():
    data_file = open("tasks.txt", "r")
    for line in data_file:
        info = line.split(",")
        for i in info:
            print(i)

    data_file.close()

# View mine function with input to ask user if they wanna return to the main menu
def view_mine():
    data_file = open("tasks.txt", "r+").readlines()
    for line in data_file:
        info = line.split(",")
        if user_name == info[0]:
            for i in info:
                print(i)
    
    opt = input('''Please select one of the options
                -1 = Main menu
                et = Edit task
                e = Exit
                : ''')
    if opt == "-1":
        main_menu()
    elif opt == "et":
        task_completion = input("Is the task complete (Yes or No): ")
        info[-1] = task_completion
    elif opt == "e":
        print("Goodbye")
        exit()
    else:
        print("Invalid input")

    data_file.close()

# Function to generate reports    
def generate_reports():
    uncompleted_tasks = 0
    completed_tasks = 0
    overdue_tasks = 0
# Opening the task text file to check the date to see if weather the task is overdue or not
    print("\n")
    # current dateTime
    now = datetime.now()

    # convert to date String
    current_date = now.strftime("%d %b %Y")
    # current_date = input("Date: ")

    my_file = open("tasks.txt", "r")
    for line in my_file:
        info = line.strip("\n").split(", ")
        if (current_date < info[-2]):
            overdue_tasks += 1
    my_file.close()
# Opening the task text file to count weather the tasks are completed or not.
    data_file = open("tasks.txt", "r+")
    for line in data_file:
        info = line.strip("\n").split(", ")
        if info[-1] == "No":
            uncompleted_tasks += 1
        elif info[-1] == "Yes":
            completed_tasks += 1
    data_file.close()
    
    percetage_uncompleted = uncompleted_tasks / returned_total * 100
    percetage_overdue = overdue_tasks / returned_total * 100
# Created the task overview text file to write the statistics for the task over view
    task_file = open("task_overview.txt", "w")       
    task_file.write("The total number of tasks generated is " + str(returned_total) + "\n")
    task_file.write("The number of completed tasks is " + str(completed_tasks) + "\n")
    task_file.write("The number of uncompleted tasks is " + str(uncompleted_tasks) + "\n")
    task_file.write("The number of overdue tasks is " + str(overdue_tasks) + "\n")
    task_file.write("The percentage of uncompleted tasks is " + str(percetage_uncompleted) + " percent. \n")
    task_file.write("The percentage of uncompleted tasks is " + str(percetage_overdue) + " percent.")
    task_file.close()


    user_total_tasks = 0
    user_uncompleted_tasks = 0
    user_completed_tasks = 0
    uncompleted_and_overdue = 0
    # current dateTime
    now = datetime.now()

    # convert to date String
    current_date = now.strftime("%d %b %Y")
    # current_date = input("Date: ")
    
    my_file = open("tasks.txt", "r")
    for line in my_file:
        info = line.strip("\n").split(", ")
        if info[-2] > current_date and info[-1] == "No":
            uncompleted_and_overdue += 1
    my_file.close()
# Opening the task text file to count weather the user tasks are completed or not. 
    data_file = open("tasks.txt", "r+")
    for line in data_file:
        info = line.strip("\n").split(", ")
        if info[-1] == "No":
            user_uncompleted_tasks += 1
        elif info[-1] == "Yes":
            user_completed_tasks += 1
        
        if info[0] == user_name:
            user_total_tasks += 1
    data_file.close()
    
    user_total_percentage = user_total_tasks / returned_total * 100
    user_completed_percetage = user_completed_tasks / user_total_tasks * 100
    user_uncompleted_percetage = user_uncompleted_tasks / user_total_tasks * 100
    uncompleted_overdue_percentage = uncompleted_and_overdue / user_total_tasks * 100
# Writing data into the user overview text file 
    user_file = open("user_overview.txt", "w")
    user_file.write("The total number of assigned tasks to the user is: " + str(user_total_tasks) + "\n")
    user_file.write("The percentage of the tasks assigned to the user is: " + str(user_total_percentage) + " percent. \n")
    user_file.write("The percetage of the completed user tasks is: " + str(user_completed_percetage) + " percent. \n")
    user_file.write("The percetage of the uncompleted user tasks is: " + str(user_uncompleted_percetage) + " percent. \n")
    user_file.write("The user tasks that are uncompleted and overdue percentage is: " + str(uncompleted_overdue_percentage) + " percent.")
    user_file.close()
    
# The function will display the text files created in generate reports function
def display_statistics():
    print("\n")
    print("TASK OVERVIEW STATS")
    task_file = open("task_overview.txt", "r")
    for line in task_file:
        print(line)
        
    print("\n")
    print("USER OVERVIEW STATS")
    user_file = open("task_overview.txt", "r")
    for line in user_file:
        print(line)

main_menu()
