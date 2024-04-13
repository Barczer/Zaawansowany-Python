class Time():

    def __init__(self, hour, minute):
        self.hour = hour if isinstance(hour, int) else 0
        self.minute = minute if isinstance(minute, int) else 0

    def is_hour(self):
        if (((self.hour >= 0) and (self.hour <= 23)) and
                (self.minute >= 0) and (self.minute <= 59)):
            return True

    def add_time(self, other_hour, other_minute):
        self.minute = self.minute + other_minute
        if self.minute > 60:
            temp = self.minute / 60
            temp_hour = int(temp)
            temp_rest = temp - temp_hour
            temp_rest = int(round(temp_rest * 60, 0))
            self.minute = temp_rest
            self.hour = self.hour + other_hour + temp_hour
            if self.hour == 24:
                self.hour = 0
            elif self.hour > 24:
                self.hour = self.hour - 24
        else:
            self.hour = self.hour + other_hour
            if self.hour == 24:
                self.hour = 0
            elif self.hour > 24:
                self.hour = self.hour - 24

    def __lt__(self, other):
        return (self.hour, self.minute) < (other.hour, other.minute)



    def __repr__(self):
        return f"{str(self.hour).rjust(2, '0')}:{str(self.minute).zfill(2)}"

t1 = Time(12, 90)
t2 = Time(23, 50)
t3 = Time(2, 50)
list_time = [
    t1, t2, t3
]

t1.add_time(3, 40)
print(t1)
t2.add_time(2, 4)
print(t2)
t3.add_time(5, 345)
print(t3)

sorted_time = sorted(list_time)
print(sorted_time)

