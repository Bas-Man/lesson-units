import unittest

from context import exceptions as UnitExcpt
from context import student

class UnitTimesTests(unittest.TestCase):

    def setUp(self):
        self.obj = student.UnitStudent()

    def testObjectJsonStr(self):
        self.obj.createUnit(startTime="07:00", endTime="07:40")
        lines = self.obj.json
        self.assertTrue('"_startTime": "07:00"' in lines)

    def testObjectJsonStrLocation(self):
        self.obj.createUnit(startTime="07:00", endTime="07:40",
                            comment="Akasaka", location="Akasaka")
        lines = self.obj.json
        self.assertTrue('"_comment": "Akasaka"' in lines)
        self.assertTrue('"_location": "Akasaka"' in lines)
