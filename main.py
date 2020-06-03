from user import *
from bucketListManager import *
from category import *
from datetime import datetime
from task import *
from goal import *
from file_manager import *
from validator import *

bucket_manager = load_list()

def create_category():
    name = input('The category : ')
    category = Category(name)
    return category

def create_goal():
    name = input('Name of the goal: ')
    description = input('Description: ')
    start = datetime.strptime(input('Start: '), '%d.%m.%Y')
    end = datetime.strptime(input('Finish: '), '%d.%m.%Y')

    i = 1
    if len(bucket_manager.categories) > 0:
        print('Choose the category')
        for category in bucket_manager.categories:
            print(f'{i}.{category}')
            i += 1
    print(f'{i}.Create a new category')
    choose = input_integer(start = 0, end  = i)
    if choose > len(bucket_manager.categories):
        category = create_category()
        bucket_manager.add_category(category)
    else:
        category = bucket_manager.categories[choose - 1]
    goal = Goal(name, description,start, end, category)

    count = int(input('Amount of the tasks = '))
    for i in range(count):
        name = input('Task: ')
        task = Task(name)
        goal.add_task(task)
    return goal

def show_goal(goal:Goal):
    print('Name of the goal:', goal.name)
    print('Description:', goal.description)
    print('Start:', goal.start.strftime("%d.%m.%Y"))
    print('Finish:', goal.end.strftime("%d.%m.%Y"))
    print('Category:', goal.category)
    print('List of the tasks')
    i = 1
    print('%5s%30s%20s' % ('Task number', 'Task', 'Status'))
    for task in goal.tasks:
        print('%5d%30s%20s' % (i, task.name, task.status))
        i += 1

def show_all_goals(goals, edit=False, category=None):
    if len(goals) == 0:
        print('There are np goals')
        return

    show_goals(goals, category)
    print('\n1.Back')
    print('2.See the goal')
    choose = input_integer(0, 2)
    if choose == 2:
        number = int(input('Enter a number of a goal: '))
        show_goal(goals[number - 1])
        if edit:
            print('1.Complete the task')
            print('0.Back')
            choose = input_integer(0, 1)
            if choose == 1:
                print('Enter a number of a task: ', end='')
                number_task = input_integer(1, len(goals[number - 1].tasks))
                goals[number - 1].tasks[number_task - 1].completed = True
                save_list(bucket_manager)

def show_goals(goals, category=None):
    print('%5s%30s%30s%15s%15s%15s%15s' % ('Number', 'Name', 'Description', 'Start', 'Finish', 'Category','Status'))
    i = 1
    for goal in goals:
        if category is not None and goal.category != category:
            continue
        description = goal.description
        if len(description) >= 30:
            description = goal.description[:27] + '...'
        if goal.completed:
            status = 'Achieved'
        else:
            status = 'Not achieved'
        print('%5d%30s%30s%15s%15s%15s%15s' % (i, goal.name, description,
                                           goal.start.strftime("%d.%m.%Y"), goal.end.strftime("%d.%m.%Y"),
                                           goal.category, status))
        i += 1

def my_goals_menu():
    while True:
        print('1.Create the goal')
        print('2.See the goals')
        print('0.Back')
        choose = input_integer(start = 0, end  = 2)
        if choose == 0:
            break
        elif choose == 1:
            goal = create_goal()
            bucket_manager.currentUser.add_goal(goal)
            save_list(bucket_manager)
        elif choose == 2:
            show_all_goals(bucket_manager.currentUser.goals, True)

def form_enemy_goals():
    goals = []
    for user in bucket_manager.users:
        if user == bucket_manager.currentUser:
            continue
        goals.extend(user.goals)
    return goals

def enemy_goals_menu():
    while True:
        print('1.Display all the goals')
        print('2.Display the goals for a chosen category')
        print('0.Back')

        choose = input_integer(start = 0, end  = 3)
        if choose == 0:
            break
        elif choose == 1:
            goals = form_enemy_goals()
            show_all_goals(goals)
        elif choose == 2:
            i = 1
            print('Choose the category')
            for category in bucket_manager.categories:
                print(f'{i}.{category}')
                i += 1
            number_category = input_integer(1, len(bucket_manager.categories))
            goals = form_enemy_goals()
            show_all_goals(goals, category=bucket_manager.categories[number_category-1])


def main():
    while True:
        print("1.Log in")
        print("2.Sign up")
        print("0.Back")
        choose = input_integer(start = 0, end  = 2)
        if choose == 0:
            return
        elif choose == 1:

            login = input('Enter your login: ')
            password = input('Enter the password: ')
            if bucket_manager.autorize(login, password):
                break
            else:
                print('Wrong login or password')
        else:
            login = input('Enter your login: ')
            password = input('Enter the password: ')
            user = User(login, password)
            bucket_manager.add_user(user)
            save_list(bucket_manager)

    while True:
        print('1.My goals')
        print('2.Goals of others')
        print('0.Back')
        choose = input_integer(0, 2)
        if choose == 0:
            break
        elif choose == 1:
            my_goals_menu()
        elif choose == 2:
            enemy_goals_menu()

main()