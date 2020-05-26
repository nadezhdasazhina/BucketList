from user import *
from bucketListManager import *
from category import *
from datetime import datetime
from task import *
from goal import *
from file_manager import *

bucket_manager = load_list()


def login():
    user = User("", "")
    return user


def create_category():
    name = input('Название: ')
    category = Category(name)
    return category


def create_goal():
    name = input('Название цели: ')
    description = input('Описание: ')
    start = datetime.strptime(input('Дата начала: '), '%d.%m.%Y')
    end = datetime.strptime(input('Дата окончание: '), '%d.%m.%Y')

    if len(bucket_manager.categories) > 0:
        print('Выберите категорию')
        i = 1
        for category in bucket_manager.categories:
            print(f'{i}.{category}')
            i += 1
    print(f'{i}.Создать новую категорию')
    choose = int(input())
    if choose > len(bucket_manager.categories):
        category = create_category()
        bucket_manager.add_category(category)
    else:
        category = bucket_manager.categories[choose - 1]
    goal = Goal(name, description, start, end, category)

    count = int(input('Кол-во задач = '))
    for i in range(count):
        name = input('Название: ')
        task = Task(name)
        goal.add_task(task)
    return goal


def show_goal(goal: Goal):
    print('Название:', goal.name)
    print('Описание:', goal.description)
    print('Начало:', goal.start.strftime("%d.%m.%Y"))
    print('Окончание:', goal.end.strftime("%d.%m.%Y"))
    print('Категория:', goal.category)
    print('Список задач')
    i = 1
    for task in goal.tasks:
        print('%5d%20s%30s' % f'{i}.{task.name} -> {task.status}')
        i += 1


def show_my_goals():
    if len(bucket_manager.currentUser.goals) == 0:
        print('Нет целей')
        return

    print('%5s%20s%30s%15s%15s%15s' % ('Номер', 'Название', 'Описание', 'Начало', 'Окончание', 'Категория'))
    i = 1
    for goal in bucket_manager.currentUser.goals:
        description = goal.description
        if len(description) >= 20:
            description = goal.description[:17] + '...'
        print('%5d%20s%30s%15s%15s%15s' % (i, goal.name, description,
                                           goal.start.strftime("%d.%m.%Y"), goal.end.strftime("%d.%m.%Y"),
                                           goal.category))
        i += 1
    print('\n1.Назад')
    print('2.Посмотреть цель')
    choose = int(input())
    if choose == 2:
        number = int(input('Введите номер цели: '))
        show_goal(bucket_manager.currentUser.goals[number - 1])


def my_goals_menu():
    while True:
        print('1.Создать цель')
        print('2.Просмотреть цели')
        print('0.Назад')
        choose = int(input())
        if choose == 0:
            break
        elif choose == 1:
            goal = create_goal()
            bucket_manager.currentUser.add_goal(goal)
            save_list(bucket_manager)
        elif choose == 2:
            show_my_goals()


def main():
    while True:
        print('1.Мои цели')
        print('2.Чужие цели')
        print('4.Выход')
        choose = int(input())
        if choose == 4:
            break
        elif choose == 1:
            my_goals_menu()


main()