class Goal:
    def __init__(self, name, description, start, end, category):
        self.__name = name
        self.__description = description
        self.__start = start
        self.__end = end
        self.__category = category
        self.__tasks = []

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    @property
    def category(self):
        return self.__category

    @property
    def tasks(self):
        return self.__tasks

    def add_task(self, task):
        self.__tasks.append(task)