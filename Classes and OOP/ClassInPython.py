class Wolf:
    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color

    def bark():
        print("Grr...")


class Dog(Wolf):
    def bark(self):
        print("Woof woof!")


husky = Dog("Max", "gray")
husky.bark()
