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
