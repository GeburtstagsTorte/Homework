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


class Player:

    def __init__(self, name, age, money, max_carry_weight, objects):
        self.name = name
        self.age = age
        self.money = money
        self.max_carry_weight = max_carry_weight
        self.objects = objects

    def print_player(self):
        print('\n'
              'Person |  Name: {} \n'
              '           Age: {} \n'
              '         Money: {} \n'
              ' max c. weight: {} \n'.format(self.name, self.age, self.money, self.max_carry_weight))

        if self.objects != 0:
            print("{} has {} Object(s): \n".format(self.name, len(self.objects)))
            for i in self.objects:
                i.print_object()
        else:
            print("{} has no Object\n".format(self.name))
        print()

people = [Player('Ahiru', 18, 400, 1, [Object('Mytho', 65, 'white', 10)]), Player('Shiru', 200, 321, 2, [])]


def add_person(people):

    name = input("Name: ")
    age = input("Age: ")
    money = input("Money: ")
    max_carry_weight = input("max c. weight: ")

    try:
        age, money, max_carry_weight = int(age), int(money), int(max_carry_weight)

    except ValueError:
        print("Error. Please use int values because i am too lazy to change it.")
        return add_person(people)

    people.append(Player(name, age, money, max_carry_weight, []))


def add_object_to_player(people):
    player_name = input("Player name who gets the object: ")
    for i in people:
        if player_name == i.name:
            print("{} is in people. Continue..\n".format(player_name))

            object_name = input("Which name shall the object have?:\n   ")
            object_weight = input("How heavy is it?:\n  ")
            object_color = input("Which color does it have?:\n  ")
            object_price = input("How much does it cost?:\n ")
            try:
                i.objects.append(Object(object_name, int(object_weight), object_color, int(object_price)))
            except ValueError:
                print("Error. Please use int values because i am too lazy to change it.")
                return add_object_to_player(people)
            print("\nCurrent details of {}:\n".format(player_name))
            i.print_player()
            break

    else:
        print("{} is not in people.".format(player_name))


def total_max_c_weight(people):
    total = 0
    for i in people:
        total += i.max_carry_weight
    print("All people can carry {} weight units".format(total))


def print_all_players(people):
    for i in range(len(people)):
        people[i].print_player()


def main():

    while True:
        print("1. Add a new person")
        print("2. Add object to person")
        print("3. How much everyone can carry")
        print("4. Print all player's details because i want to finish this shit fast so we can continue with graphics")
        print("Z. Exit")
        print()
        x = input("Choose an option from the menu: ")
        print()
        try:
            x = int(x)

        except ValueError:
            if x == 'Z':
                break
            else:
                print("This was not a valid value!")
                main()

        if x == 1:
            add_person(people)
            print("You just added: ")
            people[len(people)-1].print_player()

        if x == 2:
            add_object_to_player(people)

        if x == 3:
            total_max_c_weight(people)
        if x == 4:
            print_all_players(people)


if __name__ == '__main__':
    main()
