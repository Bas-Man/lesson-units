import unittest

from context import lessonunit

class LessonUnitTimesTests(unittest.TestCase):

    def setUp(self):
        self.unit = lessonunit.LessonUnit(startTime="7:15",endTime="7:45")

    def testObjectCreatedTimeNotSet(self):
        self.assertEqual(self.unit.startTime,"7:15")
        self.assertEqual(self.unit.endTime,"7:45")
        with self.assertRaises(ValueError):
            self.assertFalse(self.unit.isStartTimeValid)
        with self.assertRaises(ValueError):
            self.assertFalse(self.unit.isEndTimeValid)
