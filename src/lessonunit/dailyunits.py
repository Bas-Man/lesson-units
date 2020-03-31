import datetime as dt
import re
from . import unit

class DailyUnits(object):
    """docstring for Lessons."""

    def __init__(self,date=None,month=None,year=None) -> None:
        self._date = date
        self._month = month
        self._year = year
        self.units = []
        self._valid = False
        self.__validateDate()

    def __validateDate(self) -> None:
        if ((self._date is None) or (self._month is None) or
            (self._year is None)):
            raise ValueError("Invalid date provided")
        try:
            dt.date(year=self._year,month=self._month,day=self._date)
            self._valid = True
        except ValueError as e:
            print(e)

    def __type(self, value) -> None:
        if type(value) is not int:
            raise TypeError("Not Integer")

    @property
    def date(self) -> int:
        """
        Return the date of lessons.
        rtype: Int
        """
        return self._date

    @date.setter
    def date(self, value) -> None:
        """
        Set the date value.
        Checks that the input is of type int and raises TypeError if not int
        Checks that the value is in the range 1 to 31 as a minimum test.

        Raises a valueError is not in range.
        """
        self.__type(value)
        if ((value < 1) or (value > 31)):
            raise ValueError("Not within range 1 ~ 31")
        self._date = value

    @property
    def month(self) -> int:
        """
        Return the month of lessons.
        rtype: Int
        """
        return self._month

    @month.setter
    def month(self, value) -> None:
        """
        Set the month value.
        Checks that the input is of type int and raises TypeError if not int
        Checks that the value is in the range 1 to 12 as a minimum test.

        Raises a valueError is not in range.
        """
        self.__type(value)
        if ((value < 1) or (value > 12)):
            raise ValueError("Not within range 1 ~ 12")
        self._month = value

    @property
    def year(self) -> int:
        """
        Return the year of lessons.
        rtype: Int
        """
        return self._year

    @year.setter
    def year(self, value) -> None:
        """
        Set the year value.
        Checks that the input is in the string format of four digits

        Raises a valueError if it does not match the four digit string
        """
        self.__type(value)
        pattern = re.compile(r'''\d{4}''')
        match = pattern.match(str(value))
        if not match:
            raise ValueError("Must be four digits.")
        self._year = value

    @property
    def dateToStr(self) -> str:
        """
        Return date as a str
        rtype: str
        """
        return str(self._date)

    @property
    def monthToStr(self) -> str:
        """
        Retrun month as str
        type: str
        """
        return str(self._month)

    @property
    def yearToStr(self) -> str:
        """
        Return year as str
        rtype: str
        """
        return str(self._year)

    @property
    def numberOfunits(self) -> int:
        """
        Return the number of units for the lessons
        rtype: int
        """
        return len(self.units)

    def appendUnit(self, thisunit) -> None:
        """
        Append unit.Unit object to lessons.Lessons.unit[]
        Raises a TypeError if object is not of unit.Unit
        rtype: None
        """
        if isinstance(thisunit, unit.Unit):
            self.units.append(thisunit)
        else:
            raise TypeError("Invalid Object passed")
