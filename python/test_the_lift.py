import unittest


from the_lift import *


class TestClass(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_name(self):
        pass 

    def test_lift(self):
        # Floors:    G     1      2        3     4      5      6         Answers:
        tests = [\
                 [ ( (),   (),    (5,5,5), (),   (),    (),    () ),     [0, 2, 5, 0]          ],
                 [ ( (),   (),    (1,1),   (),   (),    (),    () ),     [0, 2, 1, 0]          ],
                 [ ( (),   (3,),  (4,),    (),   (5,),  (),    () ),     [0, 1, 2, 3, 4, 5, 0] ],
                 [ ( (),   (0,),  (),      (),   (2,),  (3,),  () ),     [0, 5, 4, 3, 2, 1, 0] ],
                 [ ( (),   (0,1),  (),      (),   (2,),  (3,),  () ),    [0, 5, 4, 3, 2, 1, 0] ]
                ]

        for queues, answer in tests:
            lift = Dinglemouse(queues, 5)
            self.assertEqual(lift.theLift(), answer)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
