from datetime import date as dt_date, timedelta

class Date:
    MONTH_NAMES = [
        "", "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    def __init__(self, month=1, day=1, year=1900):
        if self._is_valid_date(month, day, year):
            self._date = dt_date(year, month, day)
        else:
            print("Invalid input. Defaulting to 1/1/1900.")
            self._date = dt_date(1900, 1, 1)

    def set_date(self, month, day, year):
        if self._is_valid_date(month, day, year):
            self._date = dt_date(year, month, day)
        else:
            print("Invalid input. Defaulting to 1/1/1900.")
            self._date = dt_date(1900, 1, 1)

    def get_day(self):
        return self._date.day

    def get_month(self):
        return self._date.month

    def get_year(self):
        return self._date.year

    def is_leap_year(self):
        return Date.is_leap_year_static(self.get_year())

    @staticmethod
    def is_leap_year_static(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def last_day(self):
        return Date.last_day_static(self.get_month(), self.get_year())

    @staticmethod
    def last_day_static(month, year):
        if month in [1,3,5,7,8,10,12]: return 31
        if month in [4,6,9,11]: return 30
        return 29 if Date.is_leap_year_static(year) else 28

    def print_format_1(self):
        return self._date.strftime("%m/%d/%Y")

    def print_format_2(self):
        return self._date.strftime("%B %d, %Y")

    def print_format_3(self):
        return f"{self._date.day} {Date.MONTH_NAMES[self._date.month]} {self._date.year}"

    def __str__(self):
        return self.print_format_2()

    def __sub__(self, other):
        return abs((self._date - other._date).days)

    def __add__(self, days):
        new_date = self._date + timedelta(days=days)
        return Date(new_date.month, new_date.day, new_date.year)

    def increment(self):
        self._date += timedelta(days=1)

    def decrement(self):
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

    def _is_valid_date(self, m, d, y):
        try:
            dt_date(y, m, d)
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    d1 = Date()
    d2 = Date(2, 29, 2008)
    print("Default:", d1)
    print("Leap date:", d2.print_format_3())

    d2.increment()
    print("After increment:", d2.print_format_1())

    d2.decrement()
    print("After decrement:", d2.print_format_1())

    print("Is leap year?", d2.is_leap_year())

    d3 = Date(12, 31, 2024)
    d3.increment()
    print("Year rollover:", d3)

    diff = d2 - d3
    print(f"Days between {d2} and {d3}: {diff}")

    d3 = Date.from_input()
    print(d3)