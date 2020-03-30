import unittest

from context import unit
from context import unit_exceptions


class UnitTests(unittest.TestCase):

    def testObjectCountIsZeroOrLower(self):
        with self.assertRaises(
            unit_exceptions.UnitCountValueInvalidError) as e:
            self.unit = unit.Unit(startTime="08:30",endTime="09:10",
                                              material="BE3",
                                              type="Private",comment="@Akasaka",
                                              location="Akasaka",count=0)
        self.assertEqual(str(e.exception),
                        "Count is not one or higher. Not a valid value.")

    def testObjectCountRaisesValueError(self):
        with self.assertRaises(ValueError) as e:
            self.unit = unit.Unit(startTime="08:30",endTime="09:55",
                                              material="BE3",
                                              type="Private",comment="@Akasaka",
                                              location="Akasaka",count=1)
        self.assertEqual(str(e.exception),"Time difference does not match count")

    def testObjectCountisValid(self):
        self.unit = unit.Unit(startTime="10:00", endTime="12:55",count=4)
        self.assertEqual(self.unit.count,4)
