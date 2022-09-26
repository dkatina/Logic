from unittest import TestCase, main

from north import simply_direct

class MatchTestCase(TestCase):
    def test_1(self):
        self.assertEqual(simply_direct(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']), ["WEST"])
    def test_2(self):
        self.assertEqual(simply_direct([]),[])
    def test_3(self):
        self.assertEqual(simply_direct(['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'NORTH']),['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH'])



if __name__ == '__main__':
    main()