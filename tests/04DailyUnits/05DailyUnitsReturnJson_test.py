import unittest

from context import dailyunits
from context import unit

class UnitTimesTests(unittest.TestCase):

    def setUp(self):
        self.obj = dailyunits.DailyUnits(2020,4,6)

    def testObjectJsonStr(self):
        obj1 = unit.Unit()
        obj1.createUnit(startTime="07:00", endTime="07:40")
        self.obj.appendUnit(obj1)
        lines = self.obj.json
        self.assertTrue('"_startTime": "07:00"' in lines)

    def testObjectJsonStrLocation(self):
        obj1 = unit.Unit()
        obj1.createUnit(startTime="07:00", endTime="07:40")
        self.obj.appendUnit(obj1)
        obj2 = unit.Student()
        obj2.createUnit(startTime="08:30", endTime="09:55",location="Akasaka")
        lines = obj2.json
        self.assertTrue('"_startTime": "08:30"' in lines)
        self.assertTrue('"_endTime": "09:55"' in lines)
        self.assertTrue('"_location": "Akasaka"' in lines)
        self.obj.appendUnit(obj2)
