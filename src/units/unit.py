
from .constants import validStartTimes, validEndTimes, timePattern
from . import exceptions as UnitExcpt
import re

class UnitTime(object):
    """docstring for UnitTime."""

    def __init__(self,hour=None,minute=None) -> None:
        self._hour = hour
        self._minute = minute
        if self._hour is None:
            raise ValueError("No Hour set.")
        if self._minute is None:
            raise ValueError("No Minute set.")

    @property
    def hour(self) -> int:
        """
        """
        return self._hour

    @property
    def minute(self) -> int:
        """
        """
        return self._minute

class Unit(object):
    """
    Create a lesson unit object.

    This will store the information for a given Unit. It will provide details
    such as startTime, endTime. The material to be taught.

    Lesson type, private, office, bonus, travel.

    Number of lessons; this will be a single unit in the case of student,
    2 or more in the case of an instructor.

    Location of the lesson to be given. Any additional comments provided by the
    staff or scheduler.
    """

    def __init__(self, startTime=None, endTime=None,
                 location=None, material=None,
                 type=None, count=1, comment=None) -> None:
        self._startTime = startTime
        self._endTime = endTime
        self._location = location
        self._material = material
        self._type = type
        self._count = count
        self._comment = comment
        self.__startTimeIsValid()
        self.__endTimeIsValid()
        self.__countIsValid()

    def __countIsValid(self) -> None:
        """
        Raise ValueError if count equals Zero or count does not match time
        difference
        rtype: None
        """
        if self._count <= 0:
            raise UnitExcpt.UnitCountValueInvalidError(
                "Count is not one or higher. Not a valid value.")

        # TODO: Add index range to speed up index() check
        timeUnitDiff = ((validEndTimes.index(self._endTime) -
            validStartTimes.index(self._startTime)) + 1)
        if timeUnitDiff != self._count:
                raise UnitExcpt.UnitTimeCountValueMismatchError(
                    "Time difference does not match count")

    def __startTimeIsValid(self) -> None:
        """
        Raise a ValueError if the format is not valid
        rtype: None
        """
        if self._startTime is None:
            raise ValueError( "startTime is None. Must be 'HH:MM'")
        else:
            pattern = re.compile(timePattern)
            match = pattern.match(self._startTime)
            if not match:
                raise ValueError(
                    "Format Error startTime does not conform to 'HH:MM'")
        if self._startTime not in validStartTimes:
            raise ValueError("Invalid Start Time provided")

        # startTime is valid. Split and create attributes for use with
        # a calendar Event object
        hour, minute = self._startTime.split(':')
        self._startHour = hour
        self._startMinute = minute

    def __endTimeIsValid(self) -> None:
        """
        Return true or false if the endTime is valid.
        Raise a ValueError if the format is not valid
        rtype: None
        """
        if self._endTime is None:
            raise ValueError(
                            "endTime is None. Must be 'HH:MM'"
                            )
        else:
            pattern = re.compile(timePattern)
            match = pattern.match(self._endTime)
            if not match:
                raise ValueError(
                    "Format Error endTime does not conform to 'HH:MM'")
        if self._endTime not in validEndTimes:
            raise ValueError("Invalid End Time provided")

        # endTime is valid. Split and create attributes for use with
        # a calendar Event object
        hour, minute = self._endTime.split(':')
        self._endHour = hour
        self._endMinute = minute

    @property
    def startTime(self) -> str:
        """
        Return the startTime of the lesson.
        rtype:  str
        """
        return self._startTime

    @property
    def startHour(self) -> int:
        """
        Return the startHour used with icalendar.Event object.
        rtype: str
        """
        return int(self._startHour)

    @property
    def startMinute(self) -> int:
        """
        Return the startMinute used with icalendar.Event object.
        rtype: str
        """
        return int(self._startMinute)

    @property
    def endTime(self) -> str:
        """
        Return the endTime of the lesson.
        rtype: str
        """
        return self._endTime

    @property
    def endHour(self) -> int:
        """
        Return the endHour used with icalendar.Event object.
        rtype: str
        """
        return int(self._endHour)

    @property
    def endMinute(self) -> int:
        """
        Return the endMinute used with icalendar.Event object.
        rtype: str
        """
        return int(self._endMinute)

    @property
    def material(self) -> str:
        """
        Return the type of class material.
        rtype: str
        """
        if self._material is None:
            return ""
        return self._material

    @property
    def type(self) ->str:
        """
        Return the lesson type.
        rtype: str
        """
        if self._type is None:
            return ""
        return self._type

    @property
    def comment(self) -> str:
        """
        Return any comments attached to the lesson.
        rtype: str
        """
        if self._comment is None:
            return ""
        return self._comment

    @property
    def location(self) -> str:
        """
        Return the location of the lesson.
        rtype: str
        """
        if self._location is None:
            return ""
        return self._location

    @property
    def count(self) -> int:
        """
        Return the number of Units for the lesson as a number
        rtype: int
        """
        return self._count

    @property
    def countToStr(self) -> str:
        """
        Return the number of Units for the lesson as a string.
        rtype: str
        """
        return str(self._count)

    @property
    def startTimeForEvent(self) -> UnitTime:
        """
        """
        obj = UnitTime(self.startHour,self.startMinute)
        return obj

    @property
    def endTimeForEvent(self) -> UnitTime:
        """
        """
        obj = UnitTime(self.endHour,self.endMinute)
        return obj
