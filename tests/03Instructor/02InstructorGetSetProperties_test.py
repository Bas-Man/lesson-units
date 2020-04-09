import unittest

from context import unit


class UnitTests(unittest.TestCase):

    def setUp(self):
        self.unit = unit.Instructor()
        self.unit.createUnit(startTime="08:30",endTime="09:10",
                                          comment="@Akasaka")

    def testObjectCreatedGetSetProperies(self):
        self.assertEqual(self.unit.startTime,"08:30")
        self.assertEqual(self.unit.endTime,"09:10")
        self.assertEqual(self.unit.comment,"@Akasaka")
        self.assertEqual(self.unit.count,1)
        self.assertEqual(self.unit.countToStr,"1")
