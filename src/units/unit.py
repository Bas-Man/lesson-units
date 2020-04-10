
from .constants import validStartTimes, validEndTimes, timePattern
from . import exceptions as UnitExcpt
import re
import json

    # TODO: Consider making a base class Unit with minimal required
    # attributes and then create subclass objects for students and instructors
class Unit(object):
    """
    Create a base unit object.

    This will store minimum information for a given Unit.
    It will provide details such as startTime, endTime and comment.
    This will allow additional types of units to be derived
    """

    def __init__(self):
        self._startTime = None
        self._endTime = None
        self._count = 0
        self._comment = None

    def __repr__(self):
        message = (
            f"<{self.__class__.__name__}: "
            f"'_startTime:' = {self._startTime}, "
            f"'_endTime:' = {self._endTime} "
            f"'_count:' = {self._count}, "
            f"'_comment:' = {self._comment}"
            f">")
        return message


    def createUnit(self, startTime=None, endTime=None, comment=None) -> None:
        self._startTime = startTime
        self._endTime = endTime
        self._count = 0
        self._comment = comment
        # TODO: Decide how to handle bonus units
        self.__startTimeIsValid()
        self.__endTimeIsValid()
        self.__countIsValid()

    def __countIsValid(self) -> None:
        """
        Raise ValueError if count equals Zero or count does not match time
        difference
        rtype: None
        """
        # TODO: Add index range to speed up index() check
        UnitCount = ((validEndTimes.index(self._endTime) -
            validStartTimes.index(self._startTime)) + 1)
        if UnitCount <= self._count:
                raise UnitExcpt.UnitCountInvalidStartEndTimeError(
                    "self._endTime: {} is before self.startTime {}".format(
                        self._endTime, self.startTime))
        else:
            self._count = UnitCount

    def __startTimeIsValid(self) -> None:
        """
        Raise a UnitInvalidStartTimeError if the format is not valid
        rtype: None
        """
        if self._startTime is None:
            raise UnitExcpt.UnitInvalidStartTimeError(
                "startTime is None. Must be 'HH:MM'")
        else:
            pattern = re.compile(timePattern)
            match = pattern.match(self._startTime)
            if not match:
                raise UnitExcpt.UnitInvalidStartTimeError(
                    "Format Error startTime does not conform to 'HH:MM'")
        if self._startTime not in validStartTimes:
            raise UnitExcpt.UnitInvalidStartTimeError

        # startTime is valid. Split and create attributes for use with
        # a calendar Event object
        hour, minute = self._startTime.split(':')
        self._startHour = hour
        self._startMinute = minute

    def __endTimeIsValid(self) -> None:
        """
        Return true or false if the endTime is valid.
        Raise a UnitInvalidEndTimeError if the format is not valid
        rtype: None
        """
        if self._endTime is None:
            raise UnitExcpt.UnitInvalidEndTimeError(
                            "endTime is None. Must be 'HH:MM'"
                            )
        else:
            pattern = re.compile(timePattern)
            match = pattern.match(self._endTime)
            if not match:
                raise UnitExcpt.UnitInvalidEndTimeError(
                    "Format Error endTime does not conform to 'HH:MM'")
        if self._endTime not in validEndTimes:
            raise UnitExcpt.UnitInvalidEndTimeError()

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
    def comment(self) -> str:
        """
        Return any comments attached to the lesson.
        rtype: str
        """
        if self._comment is None:
            return ""
        return self._comment

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
    def json(self) -> str:
        """
        Return the string representation of the Unit object.
        ensure_ascii=False to preserve non ascii characters
        rtype: str
        """
        return json.dumps(self.__dict__,ensure_ascii=False,indent=4)


class Student(Unit):
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

    def __init__(self) -> None:
        super().__init__()
        self._location = None

    def __repr__(self):
        message = (
            f"{self.__class__.__name__}: "
            f"'_startTime:' = {self._startTime}, "
            f"'_endTime:' = {self._endTime} "
            f"'_count:' = {self._count}, "
            f"'_comment:' = {self._comment}, "
            f"'_location:' = {self._location}"
            f">")
        return message



    def createUnit(self, startTime=None, endTime=None, comment=None,
                   location=None):
        # positional arguments; Do not Change
        super().createUnit(startTime,endTime,comment)
        self._location = location

    @property
    def location(self) -> str:
        """
        Return the location of the lesson.
        rtype: str
        """
        if self._location is None:
            return ""
        return self._location

class Instructor(Student):
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

    def __init__(self) -> None:
        super().__init__()
        self._material = None
        self._type = None
        self._bonus = False
        # TODO: Decide how to handle bonus units

    def __repr__(self):
        message = (
            f"{self.__class__.__name__}: "
            f"'_startTime:' = {self._startTime}, "
            f"'_endTime:' = {self._endTime} "
            f"'_count:' = {self._count}, "
            f"'_comment:' = {self._comment}, "
            f"'_material:' = {self._material}, "
            f"'_type:' = {self._type}, "
            f"'_bonus:' = {self._bonus}, "
            f"'_location:' = {self._location}"
            f">")
        return message

    def createUnit(self, startTime=None,endTime=None,location=None,
                   material=None, type=None, comment=None, bonus=False) -> None:
        # NOTE: Super().createUnit is using positional Params below
        super().createUnit(startTime,endTime,comment,location)
        self._material = material
        self._type = type
        self._bonus = bonus
        self.__valiateTypeBonus()

    def __valiateTypeBonus(self) -> None:
        """
        Valiate that _type is not None when _bonus is True
        Raise TypeBonusInstructorError if this case is not True
        rtype: None
        """
        if self._type is None and self._bonus:
            raise UnitExcpt.TypeBonusInstructorError()

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
        Appends " - Bonus" if _bonus is True
        rtype: str
        """
        if not self._bonus:
            if self._type is None:
                return ""
            return self._type
        else:
            return f'{self._type} - Bonus'
