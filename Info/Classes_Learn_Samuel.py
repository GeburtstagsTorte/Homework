class Animal:

    mammal = True

    def __init__(self, species, age):
        self.species = species
        self.age = age

    def print_animal(self):
        print("Your animal, which is a(n) " + self.species + " is " + str(self.age) + " years old.")

    def print_animal_twice(self):
        self.print_animal()
        self.print_animal()

dog = Animal("Dog", 3)
dog.mammal = False
cat = Animal("Cat", 5)
print(dog.mammal)

