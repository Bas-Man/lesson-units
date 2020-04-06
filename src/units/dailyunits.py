import datetime as dt
import json
import re

from . import unit

# Possble Name Change to unitsondate

class DailyUnits(object):
    """DailyUnits object will contain a list of units which take place on
    this day.

    This will provate year,month, date and then a list of units with their
    startTime and endTime

    """

    def __init__(self,year=None,month=None,date=None) -> None:
        self._year = year
        self._month = month
        self._date = date
        self._units = []
        self._numOfUnits = 0
        # _valid currently unused.
        self._valid = False
        self.__validateDate()

    def __validateDate(self) -> None:
        """
        Validate that the date object created with the passed params is a
        date that exists. Handles leap year dates using datetime package
        rasies ValueError if any param is None.
        raises ValueError if datetime.date raises Error
        rtype: None
        """
        if ((self._date is None) or (self._month is None) or
            (self._year is None)):
            raise ValueError("date, month or year not set.")
        try:
            # Attempt to create a valid datetime object using passed params
            dt.date(year=self._year,month=self._month,day=self._date)
            self._valid = True
        except ValueError as e:
            print(e)

    def __type(self, value) -> None:
        """
        Raise TypeError if param is not of type int
        """
        if type(value) is not int:
            raise TypeError("Not Integer")

    @property
    def date(self) -> int:
        """
        Return the date, Day date only.
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
        rtype: None
        """
        self.__type(value)
        if ((value < 1) or (value > 31)):
            raise ValueError("Not within range 1 ~ 31")
        self._date = value

    @property
    def month(self) -> int:
        """
        Return the month.
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
        rtype: None
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
        Raises a TypeError if not int
        Raises a valueError if it does not match the four digit string
        rtype: None
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
    def numberOfUnits(self) -> int:
        """
        Return the number of units for the day
        rtype: int
        """
        return self._numOfUnits

    def appendUnit(self, thisunit) -> None:
        """
        Append unit.Unit object to DailyUnits.units[]
        Raises a TypeError if object is not an instance of unit.Unit
        rtype: None
        """
        if isinstance(thisunit, unit.Unit):
            self._units.append(thisunit)
            self._numOfUnits += thisunit.count
        else:
            raise TypeError("Invalid Object passed")

    @property
    def units(self) -> list:
        """
        Return a list of events that take place on the day.
        rtype: list
        """
        if self.numberOfUnits is 0:
            raise TypeError("No Units. List can not be created.")
        return self._units

    @property
    def jsonStr(self) -> str:
        """
        code taken from:
        https://medium.com/@yzhong.cs/serialize-and-deserialize-complex-json-in-python-205ecc636caa
        rtype: str
        """
        return json.dumps(self.__dict__,default=lambda o: o.__dict__,
                          ensure_ascii=False,indent=4)
