import unittest

from context import unit

class UnitTimesTests(unittest.TestCase):

    def setUp(self):
        self.unit = unit.Unit(startTime="07:00",endTime="07:40")

    def testObjectCreatedTimeNotSet(self):
        self.assertEqual(self.unit.startTime,"07:00")
        self.assertTrue(self.unit.isStartTimeValid)
        self.assertTrue(self.unit.isEndTimeValid)
