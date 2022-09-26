from unittest import TestCase, main

from whiteboard import consec_ind

class MatchTestCase(TestCase):
    def test_1_empty_match(self):
        self.assertTrue(consec_ind([1, 6, 9, -3, 4, -78, 0], -3, 4))
    def test_2_empty_match(self):
        self.assertTrue(consec_ind([3,1,0,19], 19, 0))
    def test_2_empty_match(self):
        self.assertFalse(consec_ind([3,1,0,5,19], 19, 0))

if __name__ == '__main__':
    main()