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
