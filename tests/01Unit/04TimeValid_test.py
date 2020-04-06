import unittest

from context import exceptions as UnitExcpt
from context import unit

class UnitTimesTests(unittest.TestCase):

    def testObjectHourMinuteSplit(self):
        obj = unit.Unit(startTime="07:00", endTime="07:40")
        self.assertEqual(obj.startHour,7)
        self.assertEqual(obj.startMinute,0)
        self.assertEqual(obj.endHour,7)
        self.assertEqual(obj.endMinute,40)
