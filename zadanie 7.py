class Samochod():

    def __init__(self, marka, model, rok_produkcji, przebieg):
        self.marka = marka if isinstance(marka, str) else 'brak'
        self.model = model if isinstance(model, str) else 'brak'
        self.rok_produkcji = rok_produkcji if isinstance(rok_produkcji, int) else 1900
        self.przebieg = przebieg if isinstance(przebieg, int) else 0

    def __lt__(self, other):
        return self.przebieg < other.przebieg

    def __str__(self):
        return f"Samochód marki: {self.marka} model {self.model} rok produkcji {self.rok_produkcji} przebieg {self.przebieg}"




s1 = Samochod('Audi', 'A4', 2000, 500000)
s2 = Samochod('Adui', 'A4', 2000, 3000)
print(s1 < s2)