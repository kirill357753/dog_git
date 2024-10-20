class Dog:
    def __init__(self, name, age, color):
        self.__name = name
        self.__age = age
        self.__color = color

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_color(self):
        return self.__color

    def set_age(self, new_age):
        self.__age = new_age
        return "Успешно"

    def bark(self):
        return f"Собака {self.get_name()} возрастом {self.get_age()} лет, цвета {self.get_color()}, громко гавкает"




class PurebredDog(Dog):
    def __init__(self, name, age, color, breed):
        super.__init__(name, age, color)
        self.__breed = breed

    def get_breed(self):
        return self.__breed

    def bark(self):
        return f"Собака {self.get_name()} возрастом {self.get_age()} лет, цвета {self.get_color()} и породы {self.get_breed()}, громко гавкает"

    def go_to_dog_show(self):
        return f"Собака {self.get_name()} породы {self.get_breed()} участвует на показе"

