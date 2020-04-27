import unittest

from context import exceptions as UnitExcpt
from context import unit


class UnitTests(unittest.TestCase):

    def setUp(self):
        self.obj = unit.Instructor()

    def testObjectCountisValid(self):
        self.obj.createUnit(startTime="10:00", endTime="12:55")
        self.assertEqual(self.obj.duration,160)
        self.assertEqual(self.obj.count,4)

    def testObjectStartTime(self):
        with self.assertRaises(UnitExcpt.UnitInvalidStartTimeError) as e:
            self.obj.createUnit(startTime="07:40",endTime="07:40")
        self.assertEqual(str(e.exception),"Invalid Start Time provided.")

    def testObjectEndTimeBeforeStartTime(self):
        with self.assertRaises(UnitExcpt.UnitInvalidEndTimeError) as e:
            self.obj.createUnit(startTime="07:45",endTime="07:46")
        self.assertEqual(str(e.exception),"Invalid End Time provided.")

    def testObjectTimeEndTimeBeforeStartTime(self):
        with self.assertRaises(
            UnitExcpt.UnitCountInvalidStartEndTimeError
            ) as e:
            self.obj.createUnit(startTime="08:30",endTime="07:40")
        self.assertEqual(str(e.exception),
                         "self._endTime: 07:40 is before self.startTime 08:30")
