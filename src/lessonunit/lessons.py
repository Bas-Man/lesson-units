import datetime as dt

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
        if ((self._date is None) or
            (self._month is None) or
            (self._year is None)):
            raise ValueError("Invalid Date provided")
        try:
            dt.date(year=self._year,month=self._month,day=self._date)
            self._valid = True
        except ValueError as e:
            print(e)
