import unittest

from context import unit

class UnitTimesTests(unittest.TestCase):

    def testObjectStartTimeNotValid(self):
        with self.assertRaises(ValueError) as e:
            self.unit = unit.Unit(startTime="07:15",endTime="07:40")
        self.assertEqual(str(e.exception),"Invalid Start Time provided")

    def testObjectEndTimeNotValid(self):
        with self.assertRaises(ValueError) as e:
            self.unit = unit.Unit(startTime="07:00", endTime="07:45")
        self.assertEqual(str(e.exception),"Invalid End Time provided")

    def testObjectHourMinuteSplit(self):
        self.unit = unit.Unit(startTime="07:00", endTime="07:40")
        self.assertEqual(self.unit.startHour,7)
        self.assertEqual(self.unit.startMinute,0)
        self.assertEqual(self.unit.endHour,7)
        self.assertEqual(self.unit.endMinute,40)
