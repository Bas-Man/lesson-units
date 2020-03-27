import unittest

from context import unit


class UnitTests(unittest.TestCase):

    def setUp(self):
        self.unit = unit.Unit(startTime="07:00", endTime="07:40")

    def testObjectCreatedGetProperies(self):
        self.assertEqual(self.unit.startTime,"07:00")
        self.assertEqual(self.unit.endTime,"07:40")
        self.assertEqual(self.unit.material,"")
        self.assertEqual(self.unit.type,"")
        self.assertEqual(self.unit.comment,"")
        self.assertEqual(self.unit.location,"")
        self.assertEqual(self.unit.count,1)
        self.assertEqual(self.unit.countToStr,"1")
