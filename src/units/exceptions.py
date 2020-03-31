# Custom Exceptions for more detailed and specific Errors

class UnitExceptions(Exception):
    """Base Class exceptions for Unit."""
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return "{}".format(self.msg)

class UnitCountValueInvalidError(UnitExceptions):
    """UnitCountValueInvalid."""
    def __init__(self, msg="UnitCountValueInvalidError occured"):
        super().__init__(msg)

class UnitTimeCountValueMismatchError(UnitExceptions):
    """docstring for UnitTimeCountValueMismatchError.UnitException"""
    def __init__(self, msg="Time difference does not match count"):
        super().__init__(msg)
