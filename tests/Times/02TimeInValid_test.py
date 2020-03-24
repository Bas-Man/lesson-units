import unittest

from context import unit

class LessonUnitTimesTests(unittest.TestCase):

    def setUp(self):
        self.unit = unit.Unit(startTime="07:15",endTime="07:45")

    def testObjectCreatedTimeNotSet(self):
        self.assertEqual(self.unit.startTime,"07:15")
        self.assertEqual(self.unit.endTime,"07:45")
        self.assertFalse(self.unit.isStartTimeValid)
        self.assertFalse(self.unit.isEndTimeValid)
