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
    name = input('Название: ')
    category = Category(name)
    return category

def create_goal():
    name = input('Название цели: ')
    description = input('Описание: ')
    start = datetime.strptime(input('Дата начала: '), '%d.%m.%Y')
    end = datetime.strptime(input('Дата окончание: '), '%d.%m.%Y')

    i = 1
    if len(bucket_manager.categories) > 0:
        print('Выберите категорию')
        for category in bucket_manager.categories:
            print(f'{i}.{category}')
            i += 1
    print(f'{i}.Создать новую категорию')
    choose = input_integer(start = 0, end  = i)
    if choose > len(bucket_manager.categories):
        category = create_category()
        bucket_manager.add_category(category)
    else:
        category = bucket_manager.categories[choose - 1]
    goal = Goal(name, description,start, end, category)

    count = int(input('Кол-во задач = '))
    for i in range(count):
        name = input('Название: ')
        task = Task(name)
        goal.add_task(task)
    return goal

def show_goal(goal:Goal):
    print('Название:', goal.name)
    print('Описание:', goal.description)
    print('Начало:', goal.start.strftime("%d.%m.%Y"))
    print('Окончание:', goal.end.strftime("%d.%m.%Y"))
    print('Категория:', goal.category)
    print('Список задач')
    i = 1
    print('%5s%30s%20s' % ('Номер', 'Название', 'Статус'))
    for task in goal.tasks:
        print('%5d%30s%20s' % (i, task.name, task.status))
        i += 1

def show_all_goals(goals, edit=False, category=None):
    if len(goals) == 0:
        print('Нет целей')
        return

    show_goals(goals, category)
    print('\n1.Назад')
    print('2.Посмотреть цель')
    choose = input_integer(0, 2)
    if choose == 2:
        number = int(input('Введите номер цели: '))
        show_goal(goals[number - 1])
        if edit:
            print('1.Завершить задачу')
            print('0.Назад')
            choose = input_integer(0, 1)
            if choose == 1:
                print('Введите номер задачи: ', end='')
                number_task = input_integer(1, len(goals[number - 1].tasks))
                goals[number - 1].tasks[number_task - 1].completed = True
                save_list(bucket_manager)

def show_goals(goals, category=None):
    print('%5s%30s%30s%15s%15s%15s%15s' % ('Номер', 'Название', 'Описание', 'Начало', 'Окончание', 'Категория','Статус'))
    i = 1
    for goal in goals:
        if category is not None and goal.category != category:
            continue
        description = goal.description
        if len(description) >= 30:
            description = goal.description[:27] + '...'
        if goal.completed:
            status = 'Достигнута'
        else:
            status = 'Не достигнута'
        print('%5d%30s%30s%15s%15s%15s%15s' % (i, goal.name, description,
                                           goal.start.strftime("%d.%m.%Y"), goal.end.strftime("%d.%m.%Y"),
                                           goal.category, status))
        i += 1

def my_goals_menu():
    while True:
        print('1.Создать цель')
        print('2.Просмотреть цели')
        print('0.Назад')
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
        print('1.Вывести все цели')
        print('2.Вывести цели по заданной категории')
        print('0.Назад')

        choose = input_integer(start = 0, end  = 3)
        if choose == 0:
            break
        elif choose == 1:
            goals = form_enemy_goals()
            show_all_goals(goals)
        elif choose == 2:
            i = 1
            print('Выберите категорию')
            for category in bucket_manager.categories:
                print(f'{i}.{category}')
                i += 1
            number_category = input_integer(1, len(bucket_manager.categories))
            goals = form_enemy_goals()
            show_all_goals(goals, category=bucket_manager.categories[number_category-1])


def main():
    while True:
        print("1.Войти")
        print("2.Регистрация")
        print("0.Выход")
        choose = input_integer(start = 0, end  = 2)
        if choose == 0:
            return
        elif choose == 1:

            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if bucket_manager.autorize(login, password):
                break
            else:
                print('Неверный логин или пароль')
        else:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            user = User(login, password)
            bucket_manager.add_user(user)
            save_list(bucket_manager)

    while True:
        print('1.Мои цели')
        print('2.Чужие цели')
        print('0.Выход')
        choose = input_integer(0, 2)
        if choose == 0:
            break
        elif choose == 1:
            my_goals_menu()
        elif choose == 2:
            enemy_goals_menu()

main()