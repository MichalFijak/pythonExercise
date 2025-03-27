
class BestFriend:
    def __init__(self):
        self.is_best_friend=True

class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True


    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def voice(self):
        print("gives a voice:")

class Dog(Animal,BestFriend):
    def __init__(self,name):
        super().__init__(name)
        BestFriend.__init__(self)

    def voice(self):
        super().voice()
        print("woof,woof")


class Cat(Animal):
    pass

class Mouse(Animal):
    pass


dog=Dog("Azor")
cat =Cat("Szajbus")
mouse =Mouse("Szczur")

print(f"{dog.name} {dog.is_alive} and {dog.is_best_friend}")
dog.voice()