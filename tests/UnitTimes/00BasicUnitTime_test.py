import unittest

from context import unit


class UnitTests(unittest.TestCase):

    def setUp(self):
        self.test = unit.UnitTime(hour=7, minute=40)

    def testObjectUnitTimeBasic(self):
        self.assertEqual(self.test._hour,7)
        self.assertEqual(self.test._minute,40)
        self.assertEqual(self.test.hour,7)
        self.assertEqual(self.test.minute,40)
