# Task Manager

## Description
This project was completed as the final capstone task for the HyperionDev Software Engineering bootcamp. The aim of this project was to debug and refine the functionality of a task manager programme 'original_task_manager.py' provided by HyperionDev. The final product 'task_manager.py' reflects the improvements made. These include but are not limited to: enhanced UI, task modification, displaying statistics for stored user and task data.


## Overview
The Task Manager Programme is a command-line tool designed to help users or small businesses manage their tasks efficiently. It allows users to create, edit, mark tasks as complete or incomplete, and view task details.

## Objective
The aim of this project was to apply all the fundementals of programming delievered by HyperionDev. The main aim was to refactor and streamline the code for improved user experience. To do so, the functionality of lists, dictionaries and functions have been incoporated. The code has also been restructured to follow Pythons PEP8 coding conventions to aid other developers.


## Features

**1. Task Creation:** Users can create new tasks with titles, descriptions, due dates, and assign them to specific users.  
**2. Task Editing:** Users can edit existing tasks to update their titles, descriptions, due dates, or assigned users.  
**3. Task Completion:** Tasks can be marked as complete or incomplete based on the user's progress.  
**4. Task Overview:** Users can view a summary of their tasks, including the total number of tasks assigned, completed tasks, incomplete tasks, and overdue tasks.  
**5. User Registration:** New users can register accounts by providing a username and password.  
**6. Data Persistence:** Task and user data are stored in text files for persistence across sessions.  


## Installation
1. Clone the repository to your local machine: `git clone https://github.com/daniellromo/finalCapstone.git`
2. Navigate to the project directory: `cd finalCapstone`
3. Ensure you have Python installed
4. Open the project folder in your preferred IDE
5. Run the programme: python task_manager.py


## Usage:
**1. Login:** Upon running the program, a login section will appear which will prompt the user for a username and password. As there will be no registered users on the first run, please use the following credentials to set-up the task manager **Username**: admin, **Password**: 

![Screenshot 2024-04-14 at 15 01 19](https://github.com/daniellromo/finalCapstone/assets/157993708/1981cfb8-3753-47c2-acb1-434e7dcf4074)

**2. Main Menu:** Following login, users are presented with a main menu where they can choose from various options, such as creating a new task, editing an existing task, or viewing task overviews.

![Screenshot 2024-04-14 at 15 02 26](https://github.com/daniellromo/finalCapstone/assets/157993708/204c2b27-0f3d-4d15-b6df-529a04fc47aa)

**3. User Registration:** New users can register accounts by providing a unique username and password.

**4. Task Creation:** Users can choose to create a new task by providing relevant information such as title, description, due date, and assigned user.

![Screenshot 2024-04-14 at 15 08 38](https://github.com/daniellromo/finalCapstone/assets/157993708/34e4fe4c-4dac-4ecb-93a5-f3e8a497c187)

**5. Task Completion:** Users can view all their tasks and choose to mark them as complete or incomplete by selecting 'vm' in the main menu

![Screenshot 2024-04-14 at 15 11 54](https://github.com/daniellromo/finalCapstone/assets/157993708/e87a8759-5147-41e1-a266-858b1ce17eca)

**6. Task Editing:** Users can view all their tasks and choose to edit the task details including the due date and assigned user by selecting 'vm' in the main menu

![Screenshot 2024-04-14 at 15 12 45](https://github.com/daniellromo/finalCapstone/assets/157993708/3aac8c90-0b96-4486-9ee5-4234d10b0ff1)

**7. view all tasks:** Users can choose to view a summary of all tasks logged in the task manager

![Screenshot 2024-04-14 at 15 50 09](https://github.com/daniellromo/finalCapstone/assets/157993708/84ffea68-82f6-486b-be32-113996b6054d)

**8. Generate reports:** Users can choose to generate a report. The programme will create two files. 
- task_overview This file provides an overview task information
- user_overview This file provides a breakdown of specific user information for all users

Users will be able to the view summaries of their tasks, including the total number of tasks assigned, completed tasks, incomplete tasks, and overdue tasks.

![Screenshot 2024-04-14 at 15 43 10](https://github.com/daniellromo/finalCapstone/assets/157993708/50a58954-0fce-4564-96e0-eae98ce27312)
![Screenshot 2024-04-14 at 15 43 26](https://github.com/daniellromo/finalCapstone/assets/157993708/5df55ef4-02ca-4075-a8f4-69eac14d7009)

**9. Display statistics:** The admin can choose to display the information generated in the task_overview and user_overview files to the console.

![Screenshot 2024-04-14 at 15 49 22](https://github.com/daniellromo/finalCapstone/assets/157993708/8e54112f-c7e6-4778-b7bc-2f9dffb10f91)


## Dependencies:
Python 3.x


## Contributing:
Contributions to the Task Manager Program are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request. Ensure that your code follows the project's coding conventions and that any new features or changes are well-documented.


## License:
This project is licensed under the MIT License. See the LICENSE file for details.


## Authors and Credits
[HyperionDev](https://www.hyperiondev.com/)
- Provided original programme 'original_task_manager' to be modified

[daniellomo](https://github.com/daniellromo)

- Fiexed syntax errors, runtime issues, and logical inconsistencie
- Implemeneted enhancements to improvde code readability, modularity and user experience
- Added new features such as user regisration, task management functionalities, and report generation.
- Conducted thorough testing and debugging to esnure the reliability and stability of the Task Manager application


## Acknowledgments:
Special thanks to HyperionDev for inspiration and guidance.
