class Стадион:
    def __init__(self, название, дата_открытия, страна, город, вместимость):
        self.название = название
        self.дата_открытия = дата_открытия
        self.страна = страна
        self.город = город
        self.вместимость = вместимость

    def ввести_данные(self, название, дата_открытия, страна, город, вместимость):
        self.название = название
        self.дата_открытия = дата_открытия
        self.страна = страна
        self.город = город
        self.вместимость = вместимость

    def вывести_данные(self):
        return f"Стадион: {self.название}, Открыт: {self.дата_открытия}, Страна: {self.страна}, Город: {self.город}, Вместимость: {self.вместимость}"

    # Методы для доступа к полям
    def получить_название(self):
        return self.название

    def получить_дату_открытия(self):
        return self.дата_открытия

    def получить_страну(self):
        return self.страна

    def получить_город(self):
        return self.город

    def получить_вместимость(self):
        return self.вместимость


стадион = Стадион("Лужники", "31 июля 1956", "Россия", "Москва", 81000)
print(стадион.вывести_данные())
