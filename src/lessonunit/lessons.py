import datetime as dt
import re

class Lessons(object):
    """docstring for Lessons."""

    def __init__(self,date=None,month=None,year=None):
        self._date = date
        self._month = month
        self._year = year
        self.classes = []
        self._valid = False
        self._validateDate()

    def _validateDate(self):
        if ((self._date is None) or (self._month is None) or
            (self._year is None)):
            raise ValueError("Invalid date provided")
        try:
            dt.date(year=self._year,month=self._month,day=self._date)
            self._valid = True
        except ValueError as e:
            print(e)

    def _type(self, value):
        if type(value) is not int:
            raise TypeError("Not Integer")

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._type(value)
        if ((value < 1) or (value > 31)):
            raise ValueError("Not within range 1 ~ 31")
        self._date = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._type(value)
        if ((value < 1) or (value > 12)):
            raise ValueError("Not within range 1 ~ 12")
        self._month = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._type(value)
        pattern = re.compile(r'''\d{4}''')
        match = pattern.match(str(value))
        if not match:
            raise ValueError("Must be four digits.")
        self._year = value

    @property
    def dateToStr(self):
        return str(self._date)

    @property
    def monthToStr(self):
        return str(self._month)

    @property
    def yearToStr(self):
        return str(self._year)
