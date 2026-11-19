class Musician:
    def __init__(self, name, fee, age, genre):
        self.__name = name
        self.__fee = fee
        self.__age = age
        self.__genre = genre

    def get_name(self):
        return self.__name

    def get_fee(self):
        return self.__fee

    def get_age(self):
        return self.__age

    def get_genre(self):
        return self.__genre

    def set_name(self, name):
        if name == "":
            print("Помилка")
        else:
            self.__name = name

    def set_fee(self, fee):
        if fee <= 0:
            print("Недостатньо коштів")
        else:
            self.__fee = fee

    def set_age(self, age):
        if age <= 0:
            print("XD")
        else:
            self.__age = age

    def set_genre(self, genre):
        if genre == "":
            print("Помилка")
        else:
            self.__genre = genre

    def __del__(self):
        print(f"Музиканта: {self.__name}, жанр: {self.__genre}, вік: {self.__age}, гонорар: {self.__fee} видалено")

    def show_info(self):
        print(f"Музикант: {self.__name}, жанр: {self.__genre}, вік: {self.__age}, гонорар: {self.__fee}")


class MusicFestival:
    def __init__(self, max_budget, musicians=None):
        self.__max_budget = max_budget
        self.__musicians = []
        if musicians is not None:
            total = 0
            for m in musicians:
                if total + m.get_fee() <= self.__max_budget:
                    self.__musicians.append(m)
                    total += m.get_fee()
                else:
                    print("Бюджету не хватає")

    def get_max_budget(self):
        return self.__max_budget

    def set_max_budget(self, max_budget):
        if max_budget <= 0:
            print("Помилка")
        else:
            self.__max_budget = max_budget

    def get_musicians(self):
        return self.__musicians

    def set_musicians(self, musicians):
        self.__musicians = []
        if musicians is not None:
            total = 0
            for m in musicians:
                if total + m.get_fee() <= self.__max_budget:
                    self.__musicians.append(m)
                    total += m.get_fee()
                else:
                    print("Бюджету не хватає")

    def add_musician(self, musician):
        total = 0
        for m in self.__musicians:
            total += m.get_fee()
        if total + musician.get_fee() <= self.__max_budget:
            self.__musicians.append(musician)
            print("Музиканта додано")
        else:
            print("Не хватає грошей")

    def del_musician(self, musician):
        if musician in self.__musicians:
            self.__musicians.remove(musician)
            print("Музиканта видалено")
        else:
            print("Музиканта не знайдено")

    def show_info(self):
        print(f"Максимальний бюджет фестивалю: {self.__max_budget}")
        print("Список музикантів:")
        if not self.__musicians:
            print("Порожньо")
        else:
            for m in self.__musicians:
                m.show_info()


g1 = Musician("Гурт 1", 5000, 10, "Рок")
g2 = Musician("Гурт 2", 4000, 8, "Поп")
g3 = Musician("Гурт 3", 3000, 5, "Фанк")


fest = MusicFestival(16000, [g1, g2, g3])

fest.show_info()

fest.del_musician(g2)
fest.add_musician(g3)
fest.add_musician(g1)

fest.show_info()
