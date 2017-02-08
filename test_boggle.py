import unittest
import boggle

class TestBoggle(unittest.TestCase):
    def test_is_this_thing_on(self):
        self.assertEqual(1, boggle.check())

    def test_can_create_an_empty_grid(self):
        grid = boggle.make_grid(2,3)
        self.assertEqual(len(grid), 6)

    def test_grid_coordinates(self):
        grid = boggle.make_grid(2,2)
        self.assertTrue((0,0) in grid)
        self.assertTrue((0,1) in grid)
        self.assertTrue((1,0) in grid)
        self.assertTrue((1,1) in grid)
        self.assertTrue((2,2) not in grid)


