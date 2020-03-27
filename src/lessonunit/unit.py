
from .constants import validStartTimes, validEndTimes, timePattern
import re

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
                 type=None, count=1, comment=None):
        self._startTime = startTime
        self._endTime = endTime
        self._location = location
        self._material = material
        self._type = type
        self._count = count
        self._comment = comment
        self.__validateSelf()


    def __validateSelf(self):
        """
        Internal function to check that required default values have been set.
        rtype: None
        """
        if self._startTime is None:
            raise ValueError(
                            "startTime is None. Must be 'HH:MM'"
                             )
        if self._endTime is None:
            raise ValueError(
                            "endTime is None. Must be 'HH:MM'"
                            )

    @property
    def startTime(self):
        '''
        Return the startTime of the lesson.
        rtype:  str
        '''
        return self._startTime

    @property
    def endTime(self):
        '''
        Return the endTime of the lesson.
        rtype: str
        '''
        return self._endTime

    @property
    def material(self):
        '''
        Return the type of class material.
        rtype: str
        '''
        if self._material is None:
            return ""
        return self._material

    @property
    def type(self):
        '''
        Return the lesson type.
        rtype: str
        '''
        if self._type is None:
            return ""
        return self._type

    @property
    def comment(self):
        '''
        Return any comments attached to the lesson.
        rtype: str
        '''
        if self._comment is None:
            return ""
        return self._comment

    @property
    def location(self):
        '''
        Return the location of the lesson.
        rtype: str
        '''
        if self._location is None:
            return ""
        return self._location

    @property
    def count(self):
        '''
        Return the number of Units for the lesson as a number
        rtype: int
        '''
        return self._count

    @property
    def countToStr(self):
        '''
        Return the number of Units for the lesson as a string.
        rtype str
        '''
        return str(self._count)

    @property
    def isStartTimeValid(self):
        '''
        Return true or false if the startTime is valid.
        Raise a ValueError if the format is not valid
        rtype: boolean
        '''
        pattern = re.compile(timePattern)
        match = pattern.match(self._startTime)
        if not match:
            raise ValueError("Format Error startTime does not conform to HH:MM")

        if self.startTime in validStartTimes:
            return True
        else:
            return False

    @property
    def isEndTimeValid(self):
        '''
        Return true or false if the endTime is valid.
        Raise a ValueError if the format is not valid
        rtype: boolean
        '''
        pattern = re.compile(timePattern)
        match = pattern.match(self._endTime)
        if not match:
            raise ValueError("Format Error endTime does not conform to HH:MM")

        if self.endTime in validEndTimes:
            return True
        else:
            return False
