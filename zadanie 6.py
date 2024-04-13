import datetime


class Car():

    def __init__(self, make, model, year, millage, price):
        self.make = make if isinstance(make, str) else ""
        self.model = model if isinstance(model, str) else ""
        self.year = year if isinstance(year, int) else 1900
        self.millage = millage if isinstance(millage, int) and millage > 0 else 0
        self.price = price if isinstance(price, (int, float)) and price > 0 else 0


    def drive(self, new_millage):
        if isinstance(new_millage, int) and new_millage > 0:
            self.millage = new_millage

    def calculate_depreciation(self):
        millage_percent = int(self.millage / 10000)
        year_percent = (datetime.datetime.today().year - self.year) * 2.75
        depreciation_percent = millage_percent + year_percent
        return f"Wartość samochodu spadła o {depreciation_percent}% od wartości pierwotnej"

    def __str__(self):
        return f"Auto {self.make}, model {self.model} rok produkcji {self.year} przebieg {self.millage}, cena {self.price}"

    def __repr__(self):
        return f"{self.make}, {self.model}, {self.year}, {self.millage}, {self.price}"

