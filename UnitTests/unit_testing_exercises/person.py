class Person:

    def __init__(self, first_name, last_name, age = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        pass

    def increment_age(self):
        self.age = self.age + 1
        return self.age


    def kill(self):
        self.dead = True

    def change_name(self, new_first, new_last):
        self.first_name = new_first
        self.last_name = new_last