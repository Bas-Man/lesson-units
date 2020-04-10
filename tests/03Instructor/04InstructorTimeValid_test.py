import unittest

from context import exceptions as UnitExcpt
from context import unit

class UnitTimesTests(unittest.TestCase):

    def setUp(self):
        self.obj = unit.Instructor()

    def testObjectHourMinuteSplit(self):
        self.obj.createUnit(startTime="07:00", endTime="07:40",
                            location="Otemachi")
        self.assertEqual(self.obj.startHour,7)
        self.assertEqual(self.obj.startMinute,0)
        self.assertEqual(self.obj.endHour,7)
        self.assertEqual(self.obj.endMinute,40)
        self.assertEqual(self.obj.location,"Otemachi")

    def testObjectType(self):
        self.obj.createUnit(startTime="07:00", endTime="07:40",type="Private")
        self.assertFalse(self.obj._bonus)
        self.assertEqual(self.obj.type,"Private")

    def testObjectTypeBonus(self):
        self.obj.createUnit(startTime="07:00", endTime="07:40",type="Private",
                            bonus=True)
        self.assertTrue(self.obj._bonus)
        self.assertEqual(self.obj.type,"Private - Bonus")

    def testObjectTypeBonusException(self):
        with self.assertRaises(UnitExcpt.TypeBonusInstructorError) as e:
            self.obj.createUnit(startTime="07:00", endTime="07:40", bonus=True)
        self.assertEqual(str(e.exception),
                         "Invalid: _type is None but _bonus is True.")
