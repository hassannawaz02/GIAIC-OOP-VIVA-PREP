# 🐾 Parent Class: Animal
class Animal:
    def __init__(self, name, type):
        # Object properties: name & type (like "Simba", "Wild")
        self.name = name
        self.type = type

    def describe(self):
        # Returns a basic description of the animal
        return f"Name: {self.name}, Type: {self.type}"


# 🦁 Child Class 1: Lion (inherits from Animal)
class Lion(Animal):
    def __init__(self, name):
        # Call parent constructor, set type as "Wild"
        super().__init__(name, "Wild")

    def make_sound(self):
        return "Roar!"


# 🦜 Child Class 2: Parrot (inherits from Animal)
class Parrot(Animal):
    def __init__(self, name):
        # Call parent constructor, set type as "Bird"
        super().__init__(name, "Bird")

    def make_sound(self):
        return "Squawk!"


# 🧪 Creating objects
lion = Lion("Simba")       # Wild animal
parrot = Parrot("Mithu")   # Bird

# 🖨️ Output information
print(lion.describe())             # Description of the lion
print("Sound:", lion.make_sound())  # Lion sound

print()  # Empty line for spacing

print(parrot.describe())             # Description of the parrot
print("Sound:", parrot.make_sound())  # Parrot sound
