"""unit module for dealing with units"""

import re
import json
from .constants import validStartTimes, validEndTimes, timePattern, LESSON_LENGTH
from . import exceptions as UnitExcpt

class Unit():
    """
    Create a base unit object.

    This will store minimal information for a given Unit.
    It will provide details such as startTime, endTime and comment.
    This will allow additional types of units to be derived
    """
    # pylint: disable=too-many-instance-attributes
    def __init__(self):
        self._startTime = None
        self._endTime = None
        self._startHour = None
        self._startMinute = None
        self._endHour = None
        self._endMinute = None
        self._count = 0 # Internally calculated.
        self._comment = None

    def __repr__(self): # pragma: no cover
        return (
            f"<{self.__class__.__name__}:  "
            f"'_startTime:' = {self._startTime}, "
            f"'_endTime:' = {self._endTime}, "
            f"'_count:' = {self._count},\n\t"
            f"'_comment:' = {self._comment}"
            f">"
                )

    def __str__(self): # pragma: no cover
        return (
            f"This unit starts at {self._startTime} and ends at"
            f" {self._endTime}.\nThis is {self._count} unit{self.__plural()}.\n"
            f"Comments: {self.comment}"
            )

    def __len__(self): # pragma: no cover
        """
        Return the total lesson time. No counting break time between units if
        units is greater than 1
        :rtype: int
        """
        return self._count * LESSON_LENGTH

    def __plural(self) -> str: # pragma: no cover
        """
        Helper method append 's' if counter is zero more greater than 1

        :rtype: str
        """
        if self._count > 1 or self._count == 0:
            return "s"
        return ""

    def createUnit(self, startTime=None, endTime=None, comment=None) -> None:
        """
        This is the Base Unit Class. Other units can be derivded from this.

        :param startTime:
        :type startTime: str
        :param endTime:
        :type endTime: str
        :param count:
        :type count: int
        :returns: A object of class Unit
        :rtype: None
        """
        self._startTime = startTime
        self._endTime = endTime
        self._count = 0
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
        # TODO: Add index range to speed up index() check
        unitCount = ((validEndTimes.index(self._endTime) -
                      validStartTimes.index(self._startTime)) + 1)
        if unitCount <= self._count:
            raise UnitExcpt.UnitCountInvalidStartEndTimeError(
                "self._endTime: {} is before self.startTime {}".format(
                    self._endTime, self.startTime))
        # No issue. return _count
        self._count = unitCount

    def __startTimeIsValid(self) -> None:
        """
        Raise a UnitInvalidStartTimeError if the format is not valid
        rtype: None
        """
        if self._startTime is None:
            raise UnitExcpt.UnitInvalidStartTimeError(
                "startTime is None. Must be 'HH:MM'")
        # no exception. Do match
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
                "endTime is None. Must be 'HH:MM'")
        # No Exception. Do match.
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

        :returns: The string stored in _startTime
        :rtype:  str
        """
        return self._startTime

    @property
    def startHour(self) -> int:
        """
        Return the startHour.

        :returns: The Hour only portion of startTime which is stored in _startHour
        :rtype: int
        """
        return int(self._startHour)

    @property
    def startMinute(self) -> int:
        """
        Return the startMinute.

        :returns: The Minute only portion of startTime which is stored in _startMinute
        :rtype: int
        """
        return int(self._startMinute)

    @property
    def endTime(self) -> str:
        """
        Return the endTime of the lesson.

        :returns: endTime which is stored in _endTime
        :rtype: str
        """
        return self._endTime

    @property
    def endHour(self) -> int:
        """
        Return the endHour.

        :returns: The Hour only portion of endTime which is stored in _endHour
        :rtype: int
        """
        return int(self._endHour)

    @property
    def endMinute(self) -> int:
        """
        Return the endMinute.
        :returns: The Minute only portion of endTime which is stored in _endMinute
        :rtype: int
        """
        return int(self._endMinute)

    @property
    def hasComment(self) -> bool:
        """
        :returns: True when comment is not None. Else return False
        :rtype: bool
        """
        if self._comment is not None:
            return True
        return False

    @property
    def comment(self) -> str:
        """
        :returns: any comments attached to the unit.
        :rtype: str
        """
        if self._comment is None:
            return ""
        return self._comment

    @property
    def count(self) -> int:
        """
        Return the number of Units covered from startTime to endTime
        example: 07:00 ~ 07:40 -> 1 unit, 07:00 ~ 8:25 -> 2 units

        :returns: The number of units that exist between startTime and endTime
        :rtype: int
        """
        return self._count

    @property
    def countToStr(self) -> str:
        """
        Return the number of Units as a string.

        :returns: count as a type str
        :rtype: str
        """
        return str(self._count)

    @property
    def json(self) -> str:
        """
        Return the string representation of the Unit object.
        ensure_ascii=False to preserve non ascii characters

        :returns: A json string representation of the Unit object.
        :rtype: str
        """
        return json.dumps(self.__dict__, ensure_ascii=False, indent=4)

    @property
    def duration(self) -> int:
        """
        :returns: Returns the total amount of time in minutes for the unit.
        :rtype: int
        """
        return len(self)

class Student(Unit):
    """
    This is the Student Unit Class derivded from Unit.

    This will store the information for a given Student's Unit.
    It inherits, 'startTime', 'endTime' and 'comment'. It adds 'location' as
    as new property
    """

    def __init__(self) -> None:
        super().__init__()
        self._location = None

    def __repr__(self): # pragma: no cover
        return (
            f"{self.__class__.__name__}: "
            f"'_startTime:' = {self._startTime}, "
            f"'_endTime:' = {self._endTime}, "
            f"'_count:' = {self._count},\n\t "
            f"'_comment:' = {self._comment}, "
            f"'_location:' = {self._location}"
            f">")

    def __str__(self): # pragma: no cover
        return (
            f"{super().__str__()}\n"
            f"Location: {self.location}")

    def createUnit(self, startTime=None, endTime=None, comment=None,
                   location=None):
        """
        Create a data populated instance of Student

        :param startTime: The time the lesson will commence.
        :type startTime: str
        :param endTime: The time the lesson will end.
        :type endTime: str
        :param comment: Any comments provided.
        :type comment: str
        :param location: Location of the lesson, LC name or Outservice or other.
        :type location: str
        :rtype: None
        """
        # positional arguments; Do not Change
        super().createUnit(startTime, endTime, comment)
        self._location = location

    @property
    def hasLocation(self) -> bool:
        """
        :returns: True when location is not None. Else return False
        :rtype: bool

        """
        if self._location is not None:
            return True
        return False

    @property
    def location(self) -> str:
        """
        :returns: The location of the lesson.
        :rtype: str
        """
        if self._location is None:
            return ""
        return self._location

class Instructor(Student):
    """
    This is the Instructor Unit Class derivded from Student.

    This will store the information for a given Instructor's Unit.
    It inherits, 'startTime', 'endTime', 'comment', 'location'.
    It adds 'material', 'type' and 'bonus' as new attributes.
    """

    def __init__(self) -> None:
        super().__init__()
        self._material = None
        self._type = None
        self._bonus = False

    def __repr__(self): # pragma: no cover
        return (
            f"{self.__class__.__name__}: "
            f"'_startTime:' = {self._startTime}, "
            f"'_endTime:' = {self._endTime}, "
            f"'_count:' = {self._count},\n\t    "
            f"'_location:' = {self._location}, "
            f"'_material:' = {self._material}, "
            f"'_type:' = {self._type},\n\t    "
            f"'_bonus:' = {self._bonus}, "
            f"'_comment:' = {self._comment}"
            f">")

    def __str__(self): # pragma: no cover
        return (
            f"{super().__str__()}\n"
            f"Material: {self.material}\n"
            f"Type: {self.type}\n"
            f"Bonus: {self._bonus}"
        )

    #pylint: disable=too-many-arguments
    def createUnit(self, startTime=None, endTime=None, comment=None,
                   location=None, material=None, lType=None,
                   bonus=False) -> None:
        """
        :param startTime:
        :type startTime: str
        :param endTime:
        :type endTime: str
        :param comment:
        :type comment: str
        :param location:
        :type location: str
        :param material:
        :type material: str
        :param lType: Lesson Type or Work type default Private
        :type lType: str
        :param bonus:
        :type bonus: bool
        :rtype: None
        """
        # NOTE: Super().createUnit is using positional Params below
        super().createUnit(startTime, endTime, comment, location)
        self._material = material
        self._type = lType
        self._bonus = bonus
        self.__valiateTypeBonus()

    def __valiateTypeBonus(self) -> None:
        """
        Valiate that _type is not None when _bonus is True
        :raises: TypeBonusInstructorError if this case is not True
        :rtype: None
        """
        if self._type is None and self._bonus:
            raise UnitExcpt.TypeBonusInstructorError()

    @property
    def hasMaterial(self) -> bool:
        """
        :returns: True when material is not None. Else return False
        :rtype: bool
        """
        if self._material is not None:
            return True
        return False

    @property
    def material(self) -> str:
        """
        :returns: The type of class material.
        :rtype: str
        """
        if self._material is None:
            return ""
        return self._material

    @property
    def hasType(self) -> bool:
        """
        returns: True when type is not None. Else return False
        :rtype: bool
        """
        if self._type is not None:
            return True
        return False

    @property
    def type(self) ->str:
        """
        Appends " - Bonus" if _bonus is True

        :returns: An updated str for type if bonus is True
        :rtype: str
        """
        if not self._bonus:
            if self._type is None:
                return ""
            return self._type
        # Bonus is true and type is not None
        return f'{self._type} - Bonus'

    @property
    def isBonus(self) -> bool:
        """
        :returns: True or False
        :rtype: bool
        """
        return self._bonus
