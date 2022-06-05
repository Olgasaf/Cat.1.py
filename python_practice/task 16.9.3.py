class Clients:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def __str__(self):
        return f'{self.name} {self.surname} {self.city} {self.balance}'
client_1 = Clients('Иван','Петров','Москва',50)
print(client_1)
