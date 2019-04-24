import unittest

from builder_of_things import *


class TestClass(unittest.TestCase):
    def testName(self):
        jane = Thing('Jane')
        self.assertEqual(jane.name, 'Jane')
        self.assertEqual(jane.is_a_woman, True)
        self.assertEqual(jane.is_a_man, False)


    def testArms(self):
        jane = Thing('Jane')
        self.assertEqual(isinstance(jane.arms, tuple), True)
        self.assertEqual(len(jane.arms), 2)
        self.assertEqual(all(isinstance(v, Thing) for v in jane.arms), True)
        self.assertEqual(all(v.name=="arm" for v in jane.arms), True)
        self.assertEqual(all(v.is_arm for v in jane.arms), True)

        self.assertEqual(len(jane.arms), 2)
        self.assertEqual(all(isinstance(v, Thing) for v in jane.arms), True)

    def testHead(self):
        jane = Thing('Jane')
        self.assertEqual(isinstance(jane.head, Thing), True)
        self.assertEqual(jane.head.name, "head")

    def testEyes(self):
        jane = Thing('Jane')
        self.assertEqual(len(jane.head.eyes), 2)
        self.assertEqual(all(isinstance(v, Thing) for v in jane.head.eyes), True)
        self.assertEqual(all(v.name=='eye' for v in jane.head.eyes), True)


    def testFingers(self):
        jane = Thing('Jane')
        self.assertEqual(all(len(v.fingers)==5 for v in jane.arms), True)


    def testParent(self):
        jane = Thing('Jane')
        self.assertEqual(jane.parent_of, "joe")


    def testEyeColor(self):
        jane = Thing('Jane')
        self.assertEqual(all(v.color=='blue' for v in jane.head.eyes), True)

    def testEyeShape(self):
        jane = Thing('Jane')
        self.assertEqual(all(v.color=='blue' for v in jane.eyes), True)
        self.assertEqual(all(v.shape=='round' for v in jane.eyes), True)

    def testEyesColor(self):
        jane = Thing('Jane')
        self.assertEqual(all(v.color=='green' for v in jane.eyes), True)
        self.assertEqual(all(v.pupil.color=='black' for v in jane.eyes), True)


    # def testSpeech(self):
    #     jane = Thing('Jane')
    #     def fnc(phrase): 
    #         return "%s says: %s" % (name, phrase)
    #     jane.can.speak(fnc)
    #     self.assertEqual(jane.speak('hi'), "Jane says: hi")

    # def testSpeech2(self):
    #     jane = Thing('Jane')
    #     fnc = lambda phrase: "%s says: %s" % (name, phrase)
    #     jane.can.speak(fnc, 'spoke')
    #     jane.speak('hi')
    #     self.assertEqual(jane.spoke, ["Jane says: hi"])
    #     jane.speak('goodbye')
    #     self.assertEqual(jane.spoke, ["Jane says: hi", "Jane says: goodbye"])

def main():
    unittest.main()

if __name__ == '__main__':
    main()
