from user import *
import pickle

class BucketListManager:
    def __init__(self):
        self.__currentUser = None
        self.__categories = []
        self.__users = []

    def add_category(self, category):
        self.__categories.append(category)

    @property
    def currentUser(self):
        return self.__currentUser

    @property
    def categories(self):
        return self.__categories

    @property
    def users(self):
        return self.__users

    def add_user(self, user):
        self.__users.append(user)

    def autorize(self, login, password):
        for user in self.__users:
            if user.login == login and user.password == password:
                self.__currentUser = user
                return True
        return False


