# tests/test_posture.py
import unittest
import numpy as np
from src.utils import calculate_angle

class TestPostureUtils(unittest.TestCase):
    def test_calculate_angle(self):
        # Test with known points.
        a = [1, 0]
        b = [0, 0]
        c = [0, 1]
        angle = calculate_angle(a, b, c)
        # The angle between the positive x-axis and y-axis is 90 degrees.
        self.assertAlmostEqual(angle, 90, delta=1)

if __name__ == '__main__':
    unittest.main()
