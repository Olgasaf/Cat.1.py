class Cat:
    def __init__(self, name, age, gender):
       self.name = name
       self.age = age
       self.gender = gender
    def getName(self):
       return self.name
    def getAge(self):
       return self.age
    def getGender(self):
       return self.gender




cat1 = Cat('Барон', 2, 'мальчик')
cat2 = Cat('Сэм', 2, 'мальчик')

print(f'Кот по кличке {cat1.name}, возраст - {cat1.age}, {cat1.gender}')
print(f'Кот по кличке {cat2.name}, возраст - {cat2.age}, {cat2.gender}')