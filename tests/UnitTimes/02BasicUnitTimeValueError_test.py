import unittest

from context import unit


class UnitTests(unittest.TestCase):

    # Errors should NEVER Happen as this should only be called by
    # a Unit Object which will have already been tested
    def testObjectUnitTimeRaisesValueErrorOnHour(self):
        with self.assertRaises(ValueError) as e:
            self.test = unit.UnitTime()
        self.assertEqual(str(e.exception),"No Hour set.")

    def testObjectUnitTimeRaisesValueErrorOnMinute(self):
        with self.assertRaises(ValueError) as e:
            test.test = unit.UnitTime(hour=7)
        self.assertEqual(str(e.exception),"No Minute set.")
