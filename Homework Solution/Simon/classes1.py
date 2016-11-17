import sys


class Object:
    def __init__(self, name, weight, color, price):
        self.name = name
        self.weight = weight
        self.color = color
        self.price = price

    def print_object(self):
        print('Object |  Name: {} \n'
              '        Weight: {} \n'
              '         Color: {} \n'
              '         Price: {}'.format(self.name, self.weight, self.color, self.price))
        print()

    def take_money_and_evaluate_quantity(self):
        try:
            current_money = int(input("give me the amount of money you currently have: "))
        except ValueError:
            print("It seems you made a mistake there...")
            pass

        quantity = current_money // int(self.price)
        if quantity > 0:
            print("Your possible quantity is: " + str(quantity))
            return quantity
        if quantity <= 0:
            print("your can currently buy nothing with your available money")
        else:
            print("it seems you made a mistake")

            # make a function that takes input for more eZ

    def take_weight_and_return_maxobj(self):
        user_weight = 0
        try:
            user_weight += int(input("give me the weight you can carry: "))
        except ValueError:
            pass

        maxobj = user_weight // self.weight

        if maxobj > 0:
            print("you can carry " + str(maxobj) + " objects in total")
            return maxobj
        if maxobj <= 0:
            print("you can currently carry nothing because you are too weak")
        else:
            print("seems you made a mistake")

    def return_weight_per_dollar(self):

        weight_per_dollar = self.price // self.weight
        print("the weight per dollar ratio is: " + str(weight_per_dollar))
        return weight_per_dollar(self)


class Person:
    current_carried_weight = 0

    def __init__(self, name, age, money, carry_weight, object):
        self.name = name
        self.age = age
        self.money = money
        self.carry_weight = carry_weight
        self.object = object

    def print_person(self):
        print('Player  |  Name: {} \n'
              '            Age: {} \n'
              '          Money: {} \n'
              ' max. c. weight: {} \n'
              '        objects: {} \n'.format(self.name, self.age, self.money, self.carry_weight, self.object))

people = [Person("Simon", 18, 500, 50, [Object("chair", 10, "blue", 49.99)]), Person("Samuel", 17, 500, 50, None)]


def print_persons_details(people):
    person = input("the name of the person which details are supposed to be printed: ")
    for i in people:
        if person == i.name:
            print('Player  |  Name: {} \n'
                  '            Age: {} \n'
                  '          Money: {} \n'
                  ' max. c. weight: {} \n'
                  '        objects: {} \n'.format(i.name, i.age, i.money, i.carry_weight, i.object))
        # some mistakes in here


def add_person(people):
    print("time to add a new person")
    name = input("give me the name of the person: ")
    try:
        age = int(input("give me the age of the person: "))
        money = int(input("give me the money that person has: "))
        carry_weight = int(input("give me the weight that person can carry: "))
    except ValueError:
        print("seems like you made a mistake there")
        return add_person(people)

    people.append(Person(name, age, money, carry_weight, []))
    print("person {} added".format(name))


def add_object_to_person(people):
    x = input("To which person do you want to add an object? ")
    for i in people:
        if x == i.name:
            print("\ntime to create a new object...")
            name = input("the name of your object: ")
            color = input("the color of the object: ")
            try:
                weight = int(input("the weight of the object: "))
                price = int(input("the price of your object: "))
            except ValueError:
                print("you made a mistake...")
                return add_object_to_person(people)
            i.object.append(Object(name, weight, color, price))
            print("object appended")
    else:
        print("{} is not in people.".format(x))


def print_all_carry_weight(people):
    all_weight = 0
    for i in people:
        all_weight += i.carry_weight
    print("{} is the weight all people can currently carry together".format(str(all_weight)))


def main():
    while True:
        print("\nChoose an option: ")
        print("1: Add an object to a person\n2: Add a new person\n3: Print a persons details \n4: Print the currenty weight all people could carry\n")
        print("type 'E' to exit the 'program'")
        x = input("\ntype the key for option you want to execute, correctly: ")
        if x == "E":
            print("\nBye...")
            sys.exit("exit complete, thank you for participating")
        try:
            x = int(x)
        except ValueError:
            print("It seems you made a mistake")
            main()

        if x == 1:
            print("executing function 1...")
            add_object_to_person(people)
        if x == 2:
            print("executing function 2...")
            add_person(people)
        if x == 3:
            print("executing function 3...")
            print_persons_details(people)
        if x == 4:
            print("executing function 4...")
            print_all_carry_weight(people)
        else:
            return main()


if __name__ == '__main__':
    main()

# do not roast me on that please.. i know that most of it is shit, but i also wrote most of it while having a headache
# so please have mercy  :)