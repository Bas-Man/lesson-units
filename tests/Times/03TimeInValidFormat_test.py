import unittest

from context import unit

class UnitTimesTests(unittest.TestCase):

    def setUp(self):
        self.unit = unit.Unit(startTime="7:15",endTime="7:45")

    def testObjectCreatedTimeNotSet(self):
        self.assertEqual(self.unit.startTime,"7:15")
        self.assertEqual(self.unit.endTime,"7:45")
        with self.assertRaises(ValueError):
            self.assertFalse(self.unit.isStartTimeValid)
        with self.assertRaises(ValueError):
            self.assertFalse(self.unit.isEndTimeValid)
