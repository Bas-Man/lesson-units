import unittest

from context import lessons


class LessonTests(unittest.TestCase):

    def setUp(self):
        self.lesson = lessons.Lessons(year=2020,month=12 ,date=1)

    def testStringInputDate(self):
        with self.assertRaises(TypeError) as e:
            self.lesson.date = "2"
        self.assertEqual(str(e.exception),"Not Integer")

    def testIntInputInvalidDate(self):
        with self.assertRaises(ValueError) as e:
            self.lesson.date = 0
        self.assertEqual(str(e.exception), "Not within range 1 ~ 31")

    def testIntInputValidDate(self):
        self.lesson.date = 1
        self.assertEqual(self.lesson.date,1)

    def testStringInputMonth(self):
        with self.assertRaises(TypeError) as e:
            self.lesson.month = "2"
        self.assertEqual(str(e.exception), "Not Integer")

    def testIntInputInvalidMonth(self):
        with self.assertRaises(ValueError) as e:
            self.lesson.month = 0
        self.assertEqual(str(e.exception), "Not within range 1 ~ 12")

    def testIntInputValidMonth(self):
        self.lesson.month = 1
        self.assertEqual(self.lesson.month,1)

    def testStringInputYear(self):
        with self.assertRaises(TypeError) as e:
            self.lesson.year = "2020"
        self.assertEqual(str(e.exception), "Not Integer")

    def testIntInputInvalidYear(self):
        with self.assertRaises(ValueError) as e:
            self.lesson.year = 139
        self.assertEqual(str(e.exception), "Must be four digits.")

    def testIntInputValid(self):
        self.lesson.year = 2020
        self.assertEqual(self.lesson.year,2020)
