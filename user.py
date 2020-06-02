class User:
    def __init__(self, login, password):
        self.__login = login
        self.__password = password
        self.__goals = []

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    def add_goal(self, goal):
        self.__goals.append(goal)

    @property
    def goals(self):
        return self.__goals