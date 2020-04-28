""" Custom Exceptions for more detailed and specific Errors """

class UnitError(Exception):
    """Base Class exceptions for Unit."""
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def __str__(self):
        return "{}".format(self.msg)

class UnitCountInvalidStartEndTimeError(UnitError):
    def __init__(self, msg="endTime is before startTime"):
        super().__init__(msg)

class UnitInvalidStartTimeError(UnitError):
    def __init__(self, msg="Invalid Start Time provided."):
        super().__init__(msg)

class UnitInvalidEndTimeError(UnitError):
    def __init__(self, msg="Invalid End Time provided."):
        super().__init__(msg)

###
### Exception classes for unit.Instructor begin from here
###

class InstructorError(UnitError):
    """Base Class exception for unit.Instructor"""
    def __init__(self, msg="Error in unit.Instructor"):
        super().__init__(msg)

class TypeBonusInstructorError(InstructorError):
    def __init__(self, msg="Invalid: _type is None but _bonus is True."):
        super().__init__(msg)
