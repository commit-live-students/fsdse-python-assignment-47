from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution
        import os

        res = solution('./files/testfile.txt')

        self.assertEqual(res, 717)
