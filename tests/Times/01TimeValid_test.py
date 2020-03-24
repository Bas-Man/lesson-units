import unittest

from context import lessonunit

class LessonUnitTimesTests(unittest.TestCase):

    def setUp(self):
        self.unit = lessonunit.LessonUnit(startTime="07:00",endTime="07:40")

    def testObjectCreatedTimeNotSet(self):
        self.assertEqual(self.unit.startTime,"07:00")
        self.assertTrue(self.unit.isStartTimeValid)
        self.assertTrue(self.unit.isEndTimeValid)
