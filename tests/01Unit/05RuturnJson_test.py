import unittest

from context import exceptions as UnitExcpt
from context import unit

class UnitTimesTests(unittest.TestCase):

    def testObjectJsonStr(self):
        obj = unit.Unit(startTime="07:00", endTime="07:40")
        lines = obj.jsonStr
        self.assertTrue('"_startTime": "07:00"' in lines)

    def testObjectJsonStrLocation(self):
        obj = unit.Unit(startTime="07:00", endTime="07:40",location="Akasaka")
        lines = obj.jsonStr
        self.assertTrue('"_location": "Akasaka"' in lines)
