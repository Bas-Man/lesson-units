import unittest

from context import exceptions as UnitExcpt
from context import unit

class UnitTimesTests(unittest.TestCase):

    def testObjectHourMinuteSplit(self):
        obj = unit.Student()
        obj.createUnit(startTime="07:00", endTime="07:40",location="Otemachi")
        self.assertEqual(obj.startHour,7)
        self.assertEqual(obj.startMinute,0)
        self.assertEqual(obj.endHour,7)
        self.assertEqual(obj.endMinute,40)
        self.assertEqual(obj.location,"Otemachi")
