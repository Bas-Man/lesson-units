import unittest

from context import dailyunits
from context import unit


class LessonTests(unittest.TestCase):

    def setUp(self):
        self.lesson = dailyunits.DailyUnits(year=2020,month=12 ,date=1)
        self.unit = unit.Unit(startTime="07:00",endTime="07:40",count=1)

    def testObjectsCreated(self):
        self.assertEqual(self.lesson.year,2020)
        self.assertEqual(self.unit.startTime,"07:00")
        self.assertTrue(isinstance(self.unit,unit.Unit))
        self.assertEqual(self.lesson.numberOfunits,0)

    def testappendInvalidObject(self):
        with self.assertRaises(TypeError) as e:
            self.lesson.appendUnit("test")
        self.assertEqual(str(e.exception),"Invalid Object passed")

    def testAppendUnitToLesson(self):
        self.lesson.appendUnit(self.unit)
        self.assertEqual(self.lesson.numberOfunits,1)
        self.assertEqual(self.lesson.units[0].startTime,"07:00")
