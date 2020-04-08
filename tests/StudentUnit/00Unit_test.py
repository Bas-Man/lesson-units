import unittest

from context import exceptions as UnitExcpt
from context import student


class UnitTests(unittest.TestCase):

    def setUp(self):
        self.obj = student.UnitStudent()
    def testObjectStartTime(self):
        with self.assertRaises(UnitExcpt.UnitInvalidStartTimeError) as e:
            self.obj.createUnit()
        self.assertEqual(str(e.exception),"startTime is None. Must be 'HH:MM'")

    def testObjectEndTime(self):
        with self.assertRaises(UnitExcpt.UnitInvalidEndTimeError) as e:
            self.obj.createUnit(startTime="07:00")
        self.assertEqual(str(e.exception),"endTime is None. Must be 'HH:MM'")

    def testObjectStartTimeIsNotStr(self):
        with self.assertRaises(UnitExcpt.UnitInvalidStartTimeError) as e:
            self.obj.createUnit(startTime="3:00")
        self.assertEqual(str(e.exception),
                         "Format Error startTime does not conform to 'HH:MM'")

    def testObjectEndTimeIsNotStr(self):
        with self.assertRaises(UnitExcpt.UnitInvalidEndTimeError) as e:
            self.obj.createUnit(startTime="07:00", endTime="7:40")
        self.assertEqual(str(e.exception),
                         "Format Error endTime does not conform to 'HH:MM'")

    def testObectTypeNoneCountIsZero(self):
        self.obj.createUnit(startTime="07:00", endTime="07:40",
                            location="Akasaka")
        self.assertIsNone(self.obj._comment)
        self.assertIs(self.obj._count,1)
        self.assertEqual(self.obj._location,"Akasaka")
