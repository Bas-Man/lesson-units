from .constants import validStartTimes, validEndTimes

def validStartTime(startTime):
    if startTime is None:
        return False

    if startTime in validStartTimes:
        return True
    else:
        return False

def validEndTime(endTime):
    if endTime is None:
        return False

    if endTime in validEndTimes:
        return True
    else:
        return False
