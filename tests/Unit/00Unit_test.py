import unittest

from context import unit


class UnitTests(unittest.TestCase):

    def testObjectStartTime(self):
        with self.assertRaises(ValueError) as e:
            self.obj = unit.Unit()
        self.assertEqual(str(e.exception),"startTime is None. Must be 'HH:MM'")

    def testObjectEndTime(self):
        with self.assertRaises(ValueError) as e:
            self.obj = unit.Unit(startTime="07:00")
        self.assertEqual(str(e.exception),"endTime is None. Must be 'HH:MM'")

    def testObectTypeNone(self):
        self.obj = unit.Unit(startTime="07:00", endTime="07:40")
        self.assertIsNone(self.obj._material)
        self.assertIsNone(self.obj._type)
        self.assertIsNone(self.obj._comment)
        self.assertIsNone(self.obj._location)
        self.assertIsNone(self.obj._material)
        self.assertIs(self.obj._count,1)
