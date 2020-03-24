import unittest

from context import lessonunit


class LessonUnitTimesTests(unittest.TestCase):

    def setUp(self):
        self.unit = lessonunit.LessonUnit()

    def testObjectCreatedTimeNotSet(self):
        self.assertIsNone(self.unit._startTime)
        self.assertIsNone(self.unit._endTime)
