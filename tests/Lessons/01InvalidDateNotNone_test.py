import unittest

from context import lessons


class LessonTests(unittest.TestCase):

    def setUp(self):
        self.lesson = lessons.Lessons(year=2020,month=13,date=1)

    def testObjectCreated(self):
        self.assertEqual(self.lesson._date,1)
        self.assertEqual(self.lesson._month,13)
        self.assertEqual(self.lesson._year,2020)
        self.assertFalse(self.lesson._valid)
