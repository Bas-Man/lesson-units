import unittest

from context import exceptions as UnitExcpt
from context import unit


class UnitTests(unittest.TestCase):

    def testObjectCountisValid(self):
        self.unit = unit.Unit(startTime="10:00", endTime="12:55")
        self.assertEqual(self.unit.count,4)
