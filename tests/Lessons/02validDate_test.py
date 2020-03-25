import unittest

from context import lessons


class LessonTests(unittest.TestCase):

    def setUp(self):
        self.lesson = lessons.Lessons(year=2020,month=12,date=1)

    def testObjectCreated(self):
        self.assertEqual(self.lesson._date,1)
        self.assertEqual(self.lesson._month,12)
        self.assertEqual(self.lesson._year,2020)
        self.assertTrue(self.lesson._valid)
