from datetime import date as dt_date, timedelta

class Date:
    @staticmethod
    def isLeapYear(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def last_day_static(month, year):
        if month in [1,3,5,7,8,10,12]: return 31
        if month in [4,6,9,11]: return 30
        return 29 if Date.isLeapYear(year) else 28
    
    def __init__(self, month=1, day=1, year=1900):
        self._date = self.setDate(month, day, year)

    def setDate(self, month, day, year):
        try:
            date = dt_date(year, month, day)
            return date
        except ValueError:
            print("Invalid date, setting to default")
            date = dt_date(1900, 1, 1)
            return date

    @property
    def day(self):
        return self._date.day

    @day.setter
    def day(self, d):
        m = self._date.month
        y = self._date.year
        self._date = self.setDate(m, d, y)

    @property
    def month(self):
        return self._date.month

    @month.setter
    def month(self, m):
        d = self._date.day
        y = self._date.year
        self._date = self.setDate(m, d, y)

    @property
    def year(self):
        return self._date.year

    @year.setter
    def year(self, y):
        d = self._date.day
        m = self._date.month
        self._date = self.setDate(m, d, y)
   
    def print_format_1(self):
        return self._date.strftime("%m/%d/%Y")

    def print_format_2(self):
        return self._date.strftime("%B %d, %Y")

    def print_format_3(self):
        return self._date.strftime("%d %B %Y")

    def __str__(self):
        return self.print_format_1()

    def __sub__(self, other):
        return abs((self._date - other._date).days)

    def __add__(self, days):
        self._date += timedelta(days=days)

    def nextDay(self):
        self._date += timedelta(days=1)

    def previousDay(self):
        self._date -= timedelta(days=1)

    @classmethod
    def from_input(cls):
        try:
            raw = input("Enter date (MM/DD/YYYY): ")
            parts = list(map(int, raw.strip().split("/")))
            return cls(parts[0], parts[1], parts[2])
        except Exception:
            print("Invalid input. Defaulting to 1/1/1900.")
            return cls()

if __name__ == "__main__":
    print("Default constructor")
    d1 = Date()
    print(d1)
    print("--------------")

    print("Invalid date, 2/29/2009")
    d1 = Date(2, 29, 2009)
    print(d1)
    print("--------------")
    print("Invalid date: 4/31/2008")
    d1 = Date(4, 31, 2008)
    print(d1)
    print("--------------")
    print("Invalid date: 13/1/1953")
    d1 = Date(13, 1, 1953)
    print(d1)
    print("--------------")

    print("Valid date")
    d1 = Date(2, 29, 2008)
    print(d1)
    print(d1.print_format_2())
    print(d1.print_format_3())
    print("--------------")

    print("Accessing date components as ints")
    print(d1.month, d1.day, d1.year)
    print("--------------")
    
    print("Changing the day to 15")
    d1.day = 15
    print(d1)

    print("Changing the month to May")
    d1.month = 5
    print(d1)

    print("Changing the year to 2009")
    d1.year = 2009
    print(d1)