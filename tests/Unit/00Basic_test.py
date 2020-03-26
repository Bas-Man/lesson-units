import unittest

from context import unit


class UnitTests(unittest.TestCase):

    def setUp(self):
        self.unit = unit.Unit()

    def testObjectCreated(self):
        self.assertIsNone(self.unit._startTime)
        self.assertIsNone(self.unit._endTime)
        self.assertIsNone(self.unit._material)
        self.assertIsNone(self.unit._type)
        self.assertIsNone(self.unit._comment)
        self.assertIsNone(self.unit._location)
        self.assertIsNone(self.unit._material)
        self.assertIs(self.unit._count,0)
