import unittest

from context import unit


class LessonUnitTimesTests(unittest.TestCase):

    def setUp(self):
        self.unit = unit.Unit()

    def testObjectCreatedTimeNotSet(self):
        self.assertIsNone(self.unit._startTime)
        self.assertIsNone(self.unit._endTime)
