import unittest

from context import student


class UnitTests(unittest.TestCase):

    def setUp(self):
        self.unit = student.UnitStudent()
        self.unit.createUnit(startTime="07:00", endTime="07:40")

    def testObjectCreatedGetProperies(self):
        self.assertEqual(self.unit.startTime,"07:00")
        self.assertEqual(self.unit.endTime,"07:40")
        self.assertEqual(self.unit.comment,"")
        self.assertEqual(self.unit.count,1)
        self.assertEqual(self.unit.countToStr,"1")
