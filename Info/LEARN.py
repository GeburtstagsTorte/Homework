
class Thing:

    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age

    def print_thing(self):
        print("Name: ", self.name, " Weight: ", self.weight, " Age: ", self.age)

    def increase_age(self, value):
        self.age += value

    def take_weight(self, amount):
        self.weight -= amount

        if self.weight < 0:
            return True
        else:
            return False


class Person:

    def __init__(self, name, age, thing):
        self.thing = thing
        self.hair = True
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age > 18:
            return True
        else:
            return False

    def print_info(self):
        print("The person's name is {}, aged {}".format(self.name, self.age))

        if self.check_adult():
            print("{} is an adult".format(self.name))
        else:
            print("{} is not an adult".format(self.name))

        if self.hair:
            print("{} has hair".format(self.name))
        else:
            print("{} doesn't have hair".format(self.name))

        if self.thing is not None:
            print("{} has a thing".format(self.name))
            self.thing.print_thing()
        else:
            print("{} doesn't have a thing".format(self.name))

        print()


p = [Person("Vlad", 19, Thing("Chair", 10, 3)), Person("Simon", 18, Thing("Table", 120, 20))]
p[1].print_info()
if p[1].thing.take_weight(130):
    p[1].thing = None

p[1].print_info()














































# HENTAI