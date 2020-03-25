import unittest

from context import lessons


class LessonTests(unittest.TestCase):

    def testObjectCreated(self):
        with self.assertRaises(ValueError) as e:
            self.unit = lessons.Lessons()
