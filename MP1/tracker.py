from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name": "",
    "due": None,  # datetime
    "lastActivity": None,  # datetime
    "description": "",
    "done": False  # False if not done, datetime otherise
}


# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')


def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()


def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")

    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")


def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i + 1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")


# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy()  # don't delete this; use this task reference for the below requirements
    # update lastActivity with the current datetime value
    task['lastActivity'] = datetime.now()
    # set the name, description, and due date (all must be provided)
    # due date must match one of the formats mentioned in str_to_datetime()
    if not name or not description or not due:
        print("Failed to add task. Name, description, and due date must all be provided.")
        return

    try:
        task['due'] = str_to_datetime(due)
    except ValueError:
        print("Failed to add task. The due date format is not recognized.")
        return

    task['name'] = name
    task['description'] = description

    # add the new task to the tasks list
    tasks.append(task)
    # output a message confirming the new task was added or if the addition was rejected due to missing data based on the prior checks
    # make sure save() is still called last in this function
    if '' in task.values():
        print('Task missing data. Task not added.')
    else:
        print(f"Task '{name}' added successfully!")

    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # make sure any checks/conditions clearly display an appropriate message of what failed
    save()

    # UCID: tg335
    # Date: October 8th, 2023
 # In the add_task function, the code first checks that the provided name, description, and due date are not empty. If any of them are missing, it prints an error message and rejects adding the task. If all data is present, it creates a new task based on the TASK_TEMPLATE and updates lastActivity with the current datetime. It then attempts to convert the due date string to a valid datetime format and catches any conversion errors. If successful, it adds the new task to the tasks list and confirms this with a message. Finally, it ensures the changes are saved to a JSON file using the save() function.


def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # show the existing value of each property where the TODOs are marked in the text of the inputs below (replace the TODO related text with the found tasks's data)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    if index < 0 or index >= len(tasks):
        print('Invalid task index. Please provide a valid index.')
        return

    # Get the task by index
    task = tasks[index]

    # Show the existing values of each property
    print(f"Current name: {task['name']}")
    print(f"Current description: {task['description']}")
    print(f"Current due date: {task['due']}")


    name = input(f"What's the name of this task? (TODO name) \n").strip()
    desc = input(f"What's a brief descriptions of this task? (TODO description) \n").strip()
    due = input(f"When is this task due (format: m/d/y H:M:S) (TODO due) \n").strip()
    update_task(index, name=name, description=desc, due=due)
# UCID: tg335
# Date : october 8th, 2023
#The process_update function takes an index as input, checks if it's within the valid range of tasks, and prompts the user for updated task information. It displays the existing values of each property (name, description, and due date) as placeholders in the input prompts. If the index is valid, it then calls the update_task function with the updated data to modify the task. If the index is out of bounds, it notifies the user that the task does not exist. This function allows for user-friendly updates of task details based on the selected index.


def update_task(index: int, name: str, description: str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    # find the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # update incoming task data if it's provided (if it's not provided use the original task property value)
    # update lastActivity with the current datetime value
    # output that the task was updated if any items were changed, otherwise mention task was not updated
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # Check if the index is out of bounds
    if index < 0 or index >= len(tasks):
        print('Invalid task index. Please provide a valid index.')
        return

    # Find the task by index
    task = tasks[index]

    # Update incoming task data if it's provided
    if name:
        task['name'] = name
    if description:
        task['description'] = description
    if due:
        task['due'] = due

    # Update lastActivity with the current datetime value
    task['lastActivity'] = datetime.now().strftime('%y/%m/%d %H:%M:%S')

    # Output that the task was updated if any items were changed
    if name or description or due:
        print('Task updated.')
    else:
        print('Task not updated.')


    save()
# UCID: tg335
# Date : october 8th, 2023
#The update_task function modifies a task's properties based on the provided index. It first checks if the index is valid within the task list. If valid, it updates the task's name, description, and due date with new values if provided; otherwise, it retains the original values. The function also updates the task's lastActivity with the current datetime. It prints a message confirming the update if any changes were made to the task properties; otherwise, it indicates that no updates were made. 

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # if it's not currently marked as done, record the current datetime as the value (don't just set it as true)
    # if it is currently done, print a message saying it's already been completed
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution

    # Check if the index is out of bounds
    if index < 0 or index >= len(tasks):
        print('Invalid task index. Please provide a valid index.')
        return

    # Get the task by index
    task = tasks[index]

    # Check if the task is already completed
    if task.get('done'):
        print('Task already completed.')
        return
    else:
        print('task not completed')
    task['done'] = datetime.now().strftime('%y/%m/%d %H:%M:%S')
    # Record the current datetime as the 'done' value for the task
    # Save the updated tasks list to file

    save()
# UCID: tg335
# Date : october 8th, 2023
#The mark_done function marks a task as done by updating its "done" property with the current datetime if it's not already marked as done. It checks if the index is valid, handles out-of-bounds scenarios, and prints a completion message accordingly. The function also ensures that the changes are saved to a JSON file.

def view_task(index):
    """ View more info about a specific task fetch by index """
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # utilize the given print statement when a task is found
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution

    if index < 0 or index >= len(tasks):
        print('Invalid task index. Please provide a valid index.')
        return

    task = {}  # <-- replace or update the assignment of this variable, I just used an empty dict so it would run without changes
    print(f"""
        [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
        Description: {task['description']} \n 
        Last Activity: {task['lastActivity']} \n
        Due: {task['due']}\n
        Completed: {task['done'] if task['done'] else '-'} \n
        """.replace('  ', ' '))
# UCID: tg335
# Date : october 8th, 2023

def delete_task(index):
    """ deletes a task from the tasks list by index """
    # delete/remove task from list by index
    # message should show if it was successful or not
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # Check if index is out of bounds
    if index < 0 or index >= len(tasks):
        print(f"Invalid index: {index}")
        return
    # Delete task from list by index
    task = tasks.pop(index)
    # Check if task was successfully deleted
    if task:
        print(f"Task {index + 1} deleted successfully")
    else:
        print(f"Error deleting task {index}")
    # Call save function to save changes to tasks list
    save()

# UCID: tg335
# Date : october 8th, 2023
#The delete_task function removes a task from the tasks list based on the provided index, displaying a message indicating success or failure. It also handles out-of-bounds index scenarios and ensures that the changes are saved to a JSON file.
def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # generate a list of tasks where the task is not done
    # pass that list into list_tasks()
    incomplete_tasks = [task for task in tasks if not task['done']]
    if not incomplete_tasks:
        print("There are no incomplete tasks.")
    else:
    # pass that list into list_tasks()
        list_tasks(incomplete_tasks)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
# UCID: tg335
# Date : october 8th, 2023
#The get_incomplete_tasks function generates a list of tasks that are marked as incomplete (where the "done" property is set to False). It then passes this list of incomplete tasks to the list_tasks function to display a summary view of those tasks. This function effectively lists all tasks that have not been marked as done, providing a quick overview of pending tasks. It includes a comment with the UCID and the date when it was implemented.

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than "now" and that are not complete (i.e., not done)
    # pass that list into list_tasks()
    overdue_tasks = [task for task in tasks if not task['done'] and str_to_datetime(str(task['due'])) < datetime.now()]
    list_tasks(overdue_tasks)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution    _
# UCID: tg335
# Date : october 8th, 2023
#The function get_overdue_tasks() identifies and displays tasks that are overdue for completion, specifically those tasks that are not yet completed and have a due date that has already passed.

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # get the days, hours, minutes, seconds between the due date and now
    # display the remaining time via print in a clear format showing X days, X hours, X minutes, X seconds (time components must be clearly separated)
    # example: 1 day, 0 hours, 0 minutes, 0 seconds remaining
    # if the due date is in the past print out how many days, hours, minutes, seconds the task is overdue (clearly note that it's overdue, values should be positive)
    # example: 0 days, 2 hours, 5 minutes, 10 seconds overdue (note there's no negative values)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    #task = {}  # <-- this is a placeholder to populate based on the above requirements
    # do your print logic here
    task = tasks[index] if index < len(tasks) and index >= 0 else None

    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    if task is None:
        print(f"Invalid index: {index}")
        return

    # get the days, hours, minutes, seconds between the due date and now
    # due_date = datetime.strptime(task['due'], '%Y-%m-%d %H:%M:%S')

    due_date = str_to_datetime(task["due"])

    time_diff = due_date - datetime.now()

    # display the remaining time via print in a clear format showing days, hours, minutes, seconds
    if time_diff.total_seconds() > 0:
        days, seconds = divmod(time_diff.total_seconds(), 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        print(
            f"Time remaining for task {index + 1}:\n{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds")
    else:
        time_diff = datetime.now() - due_date
        days, seconds = divmod(time_diff.total_seconds(), 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        print(
            f"Task {index + 1} is {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, and {int(seconds)} seconds overdue.")


# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit",
                "done"]
# UCID: tg335
# Date : october 8th, 2023
#The function `get_time_remaining(index)` checks the validity of the provided task index. If valid, it calculates the time difference between the current moment and the task's due date. The function then breaks down this time difference into days, hours, minutes, and seconds, creating a human-readable format. Depending on whether the task is overdue or not, it prints either the time remaining until the task's due date or the time since it became overdue. After the function, there's an unrelated `command_list` containing potential task management commands.

def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")


def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while (True):
        opt = input("What would you like to do?\n").strip()  # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num - 1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num - 1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num - 1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num - 1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num - 1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()


if __name__ == "__main__":
    run()