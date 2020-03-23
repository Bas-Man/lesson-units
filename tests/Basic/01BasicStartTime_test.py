import unittest

from context import lessonunit


class LessonUnitTests(unittest.TestCase):

    def setUp(self):
        self.unit = lessonunit.LessonUnit(startTime="8:30")

    def testObjectCreatedStartTime(self):
        self.assertEqual(self.unit._startTime,"8:30")
        self.assertIsNone(self.unit._endTime)
        self.assertIsNone(self.unit._material)
        self.assertIsNone(self.unit._type)
        self.assertIsNone(self.unit._comment)
        self.assertIsNone(self.unit._location)
        self.assertIs(self.unit._count,0)
