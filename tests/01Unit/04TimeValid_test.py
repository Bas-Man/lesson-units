import unittest

from context import exceptions as UnitExcpt
from context import unit

class UnitTimesTests(unittest.TestCase):

    def testObjectHourMinuteSplit(self):
        self.unit = unit.Unit(startTime="07:00", endTime="07:40")
        self.assertEqual(self.unit.startHour,7)
        self.assertEqual(self.unit.startMinute,0)
        self.assertEqual(self.unit.endHour,7)
        self.assertEqual(self.unit.endMinute,40)
