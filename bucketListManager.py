from user import *
import pickle

class BucketListManager:
    def __init__(self):
        self.__currentUser = User('a', '')
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

    def autorize(self, login, password):
        for user in self.__users:
            if user.login == login and user.password == password:
                self.__currentUser = user
                return True
        return False