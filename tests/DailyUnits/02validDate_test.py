import unittest

from context import dailyunits


class LessonTests(unittest.TestCase):

    def setUp(self):
        self.lesson = dailyunits.DailyUnits(year=2020,month=12,date=1)

    def testObjectCreated(self):
        self.assertEqual(self.lesson._date,1)
        self.assertEqual(self.lesson._month,12)
        self.assertEqual(self.lesson._year,2020)
        self.assertTrue(self.lesson._valid)

    def testObjectDateValues(self):
        self.assertEqual(self.lesson.date,1)
        self.assertEqual(self.lesson.month,12)
        self.assertEqual(self.lesson.year,2020)

    def testObjectDateStrings(self):
        self.assertEqual(self.lesson.dateToStr,"1")
        self.assertEqual(self.lesson.monthToStr,"12")
        self.assertEqual(self.lesson.yearToStr,"2020")
