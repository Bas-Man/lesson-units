import unittest

from context import unit


class UnitTests(unittest.TestCase):

    def setUp(self):
        self.test = unit.Unit(startTime="07:00", endTime="07:40")
        self.StimeObj = self.test.startTimeForEvent
        self.EtimeObj = self.test.endTimeForEvent

    def testObjectUnitStartTime(self):
        self.assertEqual(self.StimeObj.hour,7)
        self.assertEqual(self.StimeObj.minute,0)

    def testObjectUnitEndTime(self):
        self.assertEqual(self.EtimeObj.hour,7)
        self.assertEqual(self.EtimeObj.minute,40)
