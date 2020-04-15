import unittest

from context import unit


class UnitTests(unittest.TestCase):

    def setUp(self):
        self.unit = unit.Instructor()

    def testObjectCreatedGetProperies(self):
        self.unit.createUnit(startTime="07:00", endTime="07:40")
        self.assertEqual(self.unit.startTime,"07:00")
        self.assertEqual(self.unit.endTime,"07:40")
        self.assertEqual(self.unit.comment,"")
        self.assertEqual(self.unit.count,1)
        self.assertEqual(self.unit.countToStr,"1")
        self.assertIsNone(self.unit._material)
        self.assertEqual(self.unit.material,"")
        self.assertEqual(self.unit.type,"")
        self.assertIsNone(self.unit._bonus)

    def testObjectCreatedGetProperies(self):
        self.unit.createUnit(startTime="07:00", endTime="07:40",
                             material="BE3")
        self.assertTrue(self.unit.hasMaterial)
        self.assertEqual(self.unit.material,"BE3")
        self.assertIsNone(self.unit._type)

    def testObjectType(self):
        self.unit.createUnit(startTime="08:30",endTime="09:10", type="Private")
        self.assertTrue(self.unit.hasType)
        self.assertEqual(self.unit.type,"Private")
