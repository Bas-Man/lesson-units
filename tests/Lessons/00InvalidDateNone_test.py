import unittest

from context import dailyunits


class DailyUnitsTests(unittest.TestCase):

    def testObjectCreated(self):
        with self.assertRaises(ValueError) as e:
            self.unit = dailyunits.DailyUnits()
        self.assertEqual(str(e.exception),"Invalid date provided")
