import unittest

from context import unit


class LessonUnitTests(unittest.TestCase):

    def setUp(self):
        self.unit = unit.Unit()

    def testObjectCreatedGetProperies(self):
        self.assertEqual(self.unit.startTime,"")
        self.assertEqual(self.unit.endTime,"")
        self.assertEqual(self.unit.material,"")
        self.assertEqual(self.unit.type,"")
        self.assertEqual(self.unit.comment,"")
        self.assertEqual(self.unit.location,"")
        self.assertEqual(self.unit.count,0)
        self.assertEqual(self.unit.countToStr,"0")
