
from . import unit
import re
import json

    # TODO: Consider making a base class Unit with minimal required
    # attributes and then create subclass objects for students and instructors
class UnitStudent(unit.Unit):
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

    def createUnit(self, startTime=None, endTime=None, comment=None,
                   location=None):
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
