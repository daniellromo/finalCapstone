"""
Modified and Improved Task Manager

Notes:
1. Use the following username and password to access the admin rights
username: admin
password: password
"""

#=====importing libraries===========
import os
from datetime import datetime, date

# Formatting string to set constant format datetime object
DT_FMT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open('tasks.txt', 'w',encoding='UTF-8') as default_file:
        pass

# Reading tasks.txt file and storing each line as an element in task_data list
with open('tasks.txt', 'r',encoding='UTF-8') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""] #  Removing empty lines

# Global task_list used for storing all nested new_task dictionaries
task_list = []
for t_str in task_data: #  Iterates through every line in task data
    curr_t = {} #  Empty list representing task for current iteration

    # Each line of data is split into components using a semicolon ;
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DT_FMT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DT_FMT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False
    # Each component above is assigned to corresponding keys in curr_t

    # Once attributes have been assigned to curr_t, it's appended to task_list
    task_list.append(curr_t)

# ====Login Section====
# This block reads usernames and passwords in user.txt so user can login

# If no user.txt file exists, write one with a default account
if not os.path.exists("user.txt"):
    with open('user.txt', 'w',encoding='UTF-8') as default_file:
        default_file.write("admin;password")

# Reading user.txt, splitting lines and storing in user_data as list
with open('user.txt', 'r',encoding='UTF-8') as user_file:
    user_data = user_file.read().split("\n")

# Coverting user_data to global dictionary to store all username;password pairs
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

# Each line in user_data represents a username and password pair,
# seperated by a semicolon. For each for loop iteration
# (line stored in user.txt),the line is split into two parts:
# username and password. These are then added as key-value pairs to the
# username_password" dictionary, where the "username" variable
# is the key, and the "password" variable is the value.

# Prompting user to enter their username and password.
# These are stored to curr_user and curr_pass variables
# and checked against username_password dictionary.
logged_in = False
while not logged_in:
    print(f"\n{'='*25}\n\033[1mLOGIN\033[0m\n{'='*25}")
    curr_user = input("\033[1mUsername:\033[0m ")
    curr_pass = input("\033[1mPassword:\033[0m ")
    # Entered username checked against dictionary keys
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    # Entered password checked against dictionary values
    elif username_password[curr_user] != curr_pass:
        print("Incorrect password. Please try again.")
        continue
    # Login successful if above two conditions evaluate to false
    else:
        print("Login Successful!")
        print("-"*79)
        logged_in = True

# ===Establishing functionality for programme===


def reg_user():
    """Function to add a new user to the user.txt file.
    Prompts user for a username and password. Then: 1) Checks if
    Username does NOT already exist. 2) Checks if password and password
    confirmation match. If these two conditions evaluate to True, the
    new user is added to user.txt
    """

    print(f"{'-'*79}\n\t\t\033[1;4mREGISTER A NEW USER\033[0m\n\n")
    while True:
        # Request input of a new username
        new_username = input("New Username:         ")
        # Check if the username already exists
        if new_username not in username_password.keys():
            break
        else:
            print("\nError: This username already exists, please try a different one.\n")

    # Request input of a new password
    new_password = input("New Password:         ")

    # Request input of password confirmation.
    confirm_password = input("Confirm Password:     ")

    # Check if the new password and confirmed password are the same.
    # If match, username_password pair added to username_password dict
    if new_password == confirm_password:
        print(f"\n\033[1m{new_username}\033[0m has been added as a new user.")
        username_password[new_username] = new_password

    # For loop iterates through every username_password key_value
    # pair and appends pairs as formatted strings (username;password)
    # to user_data list. k respresents the key (username) and username[k]
    # represents the corresponding password. These pairs are written
    # as a new line in the user.txt file

        # user.txt opened in write mode
        with open('user.txt', 'w',encoding='UTF-8') as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

    # Presenting a relevant message if passwords do not match
    else:
        print("\n\033[1mError: Passwords do not match, try again\033[0m")


def add_task():
    """Function allows a user to add a new data to task.txt file.
       User is prompted to enter the username of the person 
       whom the task is assigned to. 
       If entered user exists in username_password keys,
       user is prompted to select a title, 
       description and due date for the task.
       """

    print(f"{'-'*79}\n\t\t\033[1;4mAdd Task\033[0m\n\n")
    while True:
        task_username = input("Enter user assigned to task (or enter 'q' to quit): ")
        if task_username.lower() == 'q':
            print("Returning to main menu...")
            return  # Exit the function and return to the main menu
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username\n")
        else:
            print("Thank you for selecting a user.\n")
            break

    task_title = input("Title of Task:                  ")
    task_description = input("Description of Task:            ")

    while True:
        try:
            # Using datetime strptime method to convert string to DateTime object
            task_due_date = input("Due date of task (YYYY-MM-DD):  ")
            due_date_time = datetime.strptime(task_due_date, DT_FMT)
            break

        except ValueError:
            print("\nInvalid datetime format. Please use the format specified\n")

    # Then get the current date.
    curr_date = date.today()

    # Creating dictionary to store user-entered details for new task
    # including boolean condition to indicate if the task is complete.
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False #  New tasks are automatically set as incomplete
    }

    # Appending new_task dictionary to global task_list
    task_list.append(new_task)

    # Block below iterates through UPDATED task_list containing
    # nested dictionaries that represent tasks. Creates a list of
    # components from each dictionary per ieteration in task_list.
    # square brackets used to store values from the key-value pairs in
    # str_attrs as a list, with t being each task in the dictionary
    with open('tasks.txt', 'w', encoding='UTF-8') as task_file:
        task_list_to_write = [] #  Empty dictionary for file writing
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DT_FMT),
                t['assigned_date'].strftime(DT_FMT),
                "Yes" if t['completed'] else "No" #  Determined by boolean
            ]
            # All attributes in the str_attrs list are joined
            # together by a semi-colon and appended as an element
            # to 'the task_list_to_write' list. Each element represents
            # a line of attributes from each task to be written
            # to tasks.txt, seperated by a new-line character"""
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("\nTask successfully added.")


def view_all():
    """t represents task from task_list dictionary. t is used to
    traverse the values in the task_list dictionary which are then
    printed to the console. task_list is enumerated and
    a for loop is used to iterate through the enmeurated task_list, 
    starting from index 1.
    """

    print(f"\n{34*'='} \033[1mALL TASKS\033[0m {34*'='}\n")
    for counter, t in enumerate(task_list, 1): #  Starting index set to 1.
        disp = f"{79*'-'}\n\033[1mTask:{counter}\033[0m \t\t\t {t['title']}\n"
        disp += f"\033[1mAssigned to:\033[0m \t\t {t['username']}\n"
        disp += f"\033[1mDate Assigned:\033[0m \t\t {t['assigned_date'].strftime(DT_FMT)}\n"
        disp += f"\033[1mDue Date:\033[0m \t\t {t['due_date'].strftime(DT_FMT)}\n"
        disp += f"\033[1mTask Description:\033[0m \t {t['description']}\n"
        disp += f"\033[1mCompleted:\033[0m \t\t {'Yes' if t['completed'] else 'No'}\n{79*'-'}\n"
        print(disp)


def view_mine():
    """Simillar to the for loop in the view_all function, but first 
    checks the username value for each task in task_list, and compares 
    against curr_user. If the username value in the dictionary is equal 
    to curr_user, it prints to the console, all the attributes 
    corresponding to each task assigned to the user.

    The second feature of the function is to prompt the user to
    select a task for modification. The algorithm for this
    consists of a while loop nested in an outer while loop. The outer
    while loop allows the user to select a task to edit or 
    mark as complete and incorporates try-except ValueError handling. 
    The nested while loop allows the user to either change the 
    assigned username or due date, should they decide to edit the task.

    Finally the function writes any modifications the user has made to
    the tasks.txt file before exiting.
    """

    print(f"\n{32*'='} \033[1mView My Tasks\033[0m {32*'='}\n")
    for counter, t in enumerate(task_list, 1):
        if t['username'] == curr_user:
            disp = f"{79*'-'}\n\033[1mTask {counter}:\033[0m \t\t {t['title']}\n"
            disp += f"\033[1mAssigned to:\033[0m \t\t {t['username']}\n"
            disp += f"\033[1mDate Assigned:\033[0m \t\t {t['assigned_date'].strftime(DT_FMT)}\n"
            disp += f"\033[1mDue Date:\033[0m \t\t {t['due_date'].strftime(DT_FMT)}\n"
            disp += f"\033[1mTask Description:\033[0m \t {t['description']}\n"
            disp += f"\033[1mCompleted:\033[0m \t\t {'Yes' if t['completed'] else 'No'}\n{79*'-'}"
            print(disp)

    # While loop for prompting user to select a task to modify
    while True:
        try:
            choice = int(input("\nEnter a task number to modify task "
                               "or enter -1 to return to main menu: "))
            if choice == -1:
                break #  Return to main menu
            elif 1 <= choice <= len(task_list) and task_list[choice - 1]['username'] == curr_user:
                # -1 for difference between actual index and enumerate index
                task = task_list[choice - 1]
                print(f"\n1. Mark [Task {choice}. {task['title']}] as complete\n"
                      f"2. Mark [Task {choice}. {task['title']}] as incomplete\n"
                      f"3. View details and edit [Task {choice}. {task['title']}]\n"
                      f"4. Return to Main Menu"
                      )
                # Nested if-else loop to modify 'task complete' boolean
                edit_or_mark_complete = int(input("\nPlease select a number "
                                                  "from the options above: "
                                                  ))
                if edit_or_mark_complete == 1:
                    if task["completed"] == False:
                        task["completed"] = True
                        print(f"\n\033[1mTask {choice}. '{task['title']}' "
                              f"marked as complete.\033[0m"
                              )
                    else:
                        print(f"\n\033[1mTask {choice}. '{task['title']}' "
                              f"has already been completed\033[0m"
                              )
                elif edit_or_mark_complete == 2:
                    if task["completed"] == True:
                        task["completed"] = False
                        print(f"\n\033[1mTask {choice}. '{task['title']}' "
                              f"marked as incomplete.\033[0m"
                              )
                    else:
                        print(f"\n\033[1mTask {choice}. '{task['title']}' "
                              f"is already incomplete\033[0m"
                              )
                elif edit_or_mark_complete == 3:
                    if task["completed"] == True: #  Can only edit task if marked incomplete
                        print(f"\n\033[1mTask {choice}. '{task['title']}' "
                              f"is already complete and cannot be edited.\033[0m"
                              )
                    else:
                        print("\n\033[1;4mSelected Task Information:\033[0m\n")
                        print(f"\033[1mTitle:\033[0m \t\t\t {task['title']}")
                        print(f"\033[1mAssigned to:\033[0m \t\t {task['username']}")
                        print("\033[1mDate Assigned:\033[0m \t\t "
                              f"{task['assigned_date'].strftime(DT_FMT)}"
                              )
                        print(f"\033[1mDue Date:\033[0m \t\t {task['due_date'].strftime(DT_FMT)}")
                        print(f"\033[1mDescription:\033[0m \t\t {task['description']}\n")
                        print("\033[1mCompleted:\033[0m \t\t "
                              f"{'Yes' if task['completed'] else 'No'}\n"
                              )

                        while True: #  Nested while loop for editing task
                            print("\nPlease choose what you would like to edit:\n"
                                  "1) Username of the user to whom the task is assigned\n"
                                  "2) Due date of the task\n"
                                  "3) Or return to task selection menu\n"
                                  )
                            edit_choice = int(input("Please enter a number "
                                                    "to select an option from above: "
                                                    ))
                            if edit_choice == 1:
                                edit_username = input("Currently assigned to: "
                                                      f"{task['username']}\n"
                                                      "Please enter a new username: "
                                                      )
                                if edit_username not in username_password.keys():
                                    print(f"\n\033[1mThe user '{edit_username}' "
                                          "does not exist. "
                                          "Please enter a valid username.\033[0m")
                                else:
                                    task["username"] = edit_username
                                    print("Username successfully updated.\n")
                                    print(f"\033[1mTask {choice}. [{task['title']}] "
                                          f"is now assigned to '{task['username']}\033[0m'"
                                          )
                                    break
                            elif edit_choice == 2:
                                new_task_due_date = input("Current due date of task: "
                                                          f"{task['due_date']}\n"
                                                          "Enter a new due date of task "
                                                          "(YYYY-MM-DD): "
                                                          )
                                try:
                                    new_due_date_time = datetime.strptime(new_task_due_date, DT_FMT)
                                    task['due_date'] = new_due_date_time
                                    print(f"\n\033[1mNew due date assigned to Task "
                                          f"{choice}. [{task['title']}]\033[0m"
                                          )
                                except ValueError:
                                    print("\n\033[1mInvalid date format. "
                                          "Please enter the date in YYYY-MM-DD format.\033[0m"
                                          )
                            elif edit_choice == 3:
                                break  # Return to task selection menu
                            else:
                                print("\n\033[1mThat is an invalid input, please try again.\033[0m")
                elif edit_or_mark_complete == 4:
                    # No need to write to file here, will be done after the loop
                    pass
                else:
                    print("\n\033[1mInvalid task number. Please try again.\033[0m")
            else:
                print("\n\033[1mInvalid entry. Please try again.\033[0m")
        except ValueError:
            print("\n\033[1mInvalid input. Please enter a number.\033[0m")

    # Write updated task list to tasks.txt file before exiting function
    with open('tasks.txt', 'w',encoding='UTF-8') as task_file:
        for t in task_list:
            task_file.write(
                f"{t['username']};{t['title']};{t['description']};"
                f"{t['due_date'].strftime(DT_FMT)};"
                f"{t['assigned_date'].strftime(DT_FMT)};"
                f"{'Yes' if t['completed'] else 'No'}\n"
            )


def generate_task_overview():
    """Using List Comprehension to generate sum of figures for report
    by iterating through each task in task_list and evaluating the 
    tasks' attributes representing conditionals in If Statements.
    Arithmetic operations are then carried out using 'total_tasks',
    'completed_tasks','uncompleted_tasks' and overdue_tasks 
    to calculate other details such as percentages for report. 
    """

    total_tasks = len(task_list)
    # 1 added to sum for every task in task list that's marked complete
    completed_tasks = sum(1 for task in task_list if task['completed'])
    uncompleted_tasks = total_tasks - completed_tasks
    # 1 added for every task in task list that's incomplete AND exceeded due date
    overdue_tasks = sum(1 for task in task_list if not task['completed'] and task['due_date'].date() < date.today())
    incomplete_percentage = (uncompleted_tasks / total_tasks) * 100
    complete_percentage = (completed_tasks / total_tasks) * 100
    overdue_percentage = (overdue_tasks / total_tasks) * 100
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # F-strings to print calculated details above to report
    task_overview_content = f"{32*'-'} TASK OVERVIEW {32*'-'}\n"
    task_overview_content += f"Date: {current_datetime}\n{'-'*79}\n\n"
    task_overview_content += f"Total number of tasks: {total_tasks}\n"
    task_overview_content += f"Total number of completed tasks: {completed_tasks}\n"
    task_overview_content += f"Total number of uncompleted tasks: {uncompleted_tasks}\n"
    task_overview_content += f"Total number of overdue tasks: {overdue_tasks}\n\n"
    task_overview_content += f"Percentage of complete tasks: {complete_percentage:.2f}%\n"
    task_overview_content += f"Percentage of incomplete tasks: {incomplete_percentage:.2f}%\n"
    task_overview_content += f"Percentage of tasks that are overdue: {overdue_percentage:.2f}%\n\n"

    with open('task_overview.txt', 'w',encoding='UTF-8') as task_overview_file:
        task_overview_file.write(task_overview_content)


def generate_user_overview():
    """Tasks_assigned_to_users variable generates a dictionary of 
    Username:Total Number Of Task pairs. It consists of two seperate 
    loops that iterate together. 

    [for username in username_password.keys()] - Iterates over each 
    username in the username_passsword dictionary.
    [sum(1 for task in task_list if task['username'] == username] -
    Iterates over each task in the task_list dictionary. 
    The task_list usernames are compared with the current username 
    in the username.password iteration. If they match then the loop 
    generates a vlaue of 1. The sum() adds up all 1's for each 
    matching username iteration.

    The For Loop iterates over the key_value pairs 
    in the tasks_assigned_to_users dictionary to calculate details for
    the report.
    """

    total_tasks = len(task_list)
    total_users = len(username_password)

    tasks_assigned_to_users = {user_name: sum(1 for task in task_list if task['username'] == user_name) for user_name in username_password.keys()}
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    user_overview_content = f"{32*'-'} USER OVERVIEW {32*'-'}\n"
    user_overview_content += f"Date: {current_datetime}\n{'-'*79}\n\n"
    user_overview_content += f"Total number of users registered: {total_users}\n"
    user_overview_content += f"Total number of tasks: {total_tasks}\n\n"

    # Items() method allows loop to iterate over BOTH keys and values
    # of the dictionary in a single loop iteration
    for user_name, tasks_assigned in tasks_assigned_to_users.items():
        # 1 added for every completed task
        # that has a username matching username in dictionary
        completed_tasks_by_user = sum(1 for task in task_list if task['username'] == user_name and task['completed'])
        incomplete_tasks_by_user = tasks_assigned - completed_tasks_by_user
        # 1 added for every task that has a date exceeding today's date
        # AND a username that matches username in dictionary
        overdue_tasks_by_user = sum(1 for task in task_list if task['username'] == user_name and not task['completed'] and task['due_date'].date() < date.today())
        tasks_assigned_percentage = (tasks_assigned / total_tasks) * 100
        completed_tasks_percentage = (completed_tasks_by_user / tasks_assigned) * 100
        incomplete_tasks_percentage = (incomplete_tasks_by_user / tasks_assigned) * 100
        overdue_tasks_percentage = (overdue_tasks_by_user / tasks_assigned) * 100

        # F-strings to print calculated details above to report
        user_overview_content += (f"{33*'-'} User: {user_name} {33*'-'}\n\n"
        f"Number (Percentage) of total number of tasks assigned: "
        f"{tasks_assigned} ({tasks_assigned_percentage:.2f}%)\n\n"
        f"Number (Percentage) of completed tasks: "
        f"{completed_tasks_by_user} ({completed_tasks_percentage:.2f}%)\n"
        f"Number (Percentage) of incomplete tasks: "
        f"{incomplete_tasks_by_user} ({incomplete_tasks_percentage:.2f}%)\n"
        f"Number (Percentage) of overdue tasks: "
        f"{overdue_tasks_by_user} ({overdue_tasks_percentage:.2f}%)\n\n"
        )

    with open('user_overview.txt', 'w',encoding='UTF-8') as user_overview_file:
        user_overview_file.write(user_overview_content)


def display_statistics():
    """
    The function 'display_statistics allows the admin to display
    the generated reports to the terminal.

    This function will read the information from the task_overview.txt
    and user_overview.txt and display it in a user-friendly manner.

    If the admin has not generated the reports yet, then the code to
    generate the text files will be called in order to display the
    information. 
    """

    # Create task_overview.txt if it does not exist.
    if not os.path.exists("task_overview.txt"):
        generate_task_overview()

    # Create user_overview.txt if it does not exist.
    if not os.path.exists("user_overview.txt"):
        generate_user_overview()

    print()
    print(f"{34*'='} \033[1mSTATISTICS\033[0m {35*'='}\n")
    with open('task_overview.txt', 'r',encoding='UTF-8') as task_overview_file:
        task_ov_content = task_overview_file.read()
        print(task_ov_content)

    print("\n")
    with open('user_overview.txt','r',encoding='UTF-8') as user_overview_file:
        user_ov_content = user_overview_file.read()
        print(user_ov_content)

# Presenting menu and converting input to lower case for error handling
while True:
    print("\n\n\t\t\033[1;4mMAIN MENU\033[0m\n")
    menu = input('''Select one of the following options below:
                 
    r  -        Registering a user
    a  -        Adding a task
    va -        View all tasks
    vm -        View my tasks
    gr -        generate reports
    ds -        Display statistics
    e  -        Exit
    : ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'gr':
        generate_task_overview()
        generate_user_overview()
        print("\nReports generated successfully.")

# Only admin can display statistics about number of users and tasks.
    elif menu == 'ds':
        if curr_user == 'admin':
            display_statistics()
        else:
            print("\n\033[1mOnly admin can select this option.\033[0m")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("\n\033[1mInvalid choice, Please Try again.\033[0m")
