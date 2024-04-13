from operator import attrgetter

class Movie():

    def __init__(self, name, year, rate):
        self.name = name if isinstance(name, str) else ''
        self.year = year if isinstance(year, int) and year >= 1900 and year < 2100 else 1900
        self.rate = rate if isinstance(rate, (int, float)) and rate > 0 and rate <= 10 else 0

    def __repr__(self):
        return f"Movie name: {self.name}, movie year {self.year}, movie rate {self.rate}"



movie_list = [
    Movie('Moon', 1901, 8),
    Movie('Mars', 1950, 4),
    Movie('Jupyter', 1990, 4),
    Movie('Earth', 1960, 5),
    Movie('Eris', 2006, 8),
    Movie('Sun', 2022, 10),
    Movie('Uran', 2002, 3.9),
    Movie('Ceres', 2022, 2.1),
    Movie('Stars', 2000, 0.1),
    Movie('Space', 1976, 8.9)
]

# sortowanie od najstarszych filmów do najnowszych
sort1 = sorted(movie_list, key=attrgetter('year'))
# sortowanie według ocen od najwyższej
sort2 = sorted(movie_list, key=attrgetter('rate'), reverse=True)
# sortowanie według ocen a następnie według lat malejąco
sort3 = sorted(movie_list, key=attrgetter('rate', 'year'), reverse=True)
# sortowanie alfabetycznie
sort4 = sorted(movie_list, key=attrgetter('name'))
# sortowanie alfabetycznie, następnie według lat i ocen rosnąco
sort5 = sorted(movie_list, key=attrgetter('name', 'year', 'rate'))