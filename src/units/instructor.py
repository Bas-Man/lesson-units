
from . import unit
import re
import json

    # TODO: Consider making a base class Unit with minimal required
    # attributes and then create subclass objects for students and instructors
class UnitInstructor(unit.Unit):
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
        # TODO: Decide how to handle bonus units

    def createUnit(startTime=None,endTime=None,location=None,
                   material=None,comment=None) -> None:
        self._material = material
        self._type = type

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
    def json(self) -> str:
        """
        Return the string representation of the Unit object.
        ensure_ascii=False to preserve non ascii characters
        rtype: str
        """
        return json.dumps(self.__dict__,ensure_ascii=False,indent=4)
