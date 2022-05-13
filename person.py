class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def last_name(self):
        return self.name.split()[-1]

    def give_rise(self, percent):
        self.pay *= 1 + percent * 0.01


class Manager(Person):
    def __init__(self, name, age, pay=0):
        super().__init__(name, age, pay)
        self.job = 'manager'

    def give_rise(self, percent):
        self.pay *= 1 + percent * 0.02

if __name__ == '__main__':
    bob = Person('bob', 37, 40000, 'worker')
    mike = Manager('mike', 14)
    print(bob.__dict__)
    bob.give_rise(10)
    print(bob.__dict__)
    mike.give_rise(10)
    print(mike.__dict__)

