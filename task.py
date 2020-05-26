class Task:
    def __init__(self, name):
        self.__name = name
        self.__completed = False

    @property
    def name(self):
        return self.__name

    @property
    def completed(self):
        return self.__completed

    @completed.setter
    def completed(self, value):
        self.__completed = value