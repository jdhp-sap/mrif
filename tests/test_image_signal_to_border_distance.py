#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Jérémie DECOCK (http://www.jdhp.org)

# This script is provided under the terms and conditions of the MIT license:
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
This module contains unit tests for the "image.signal_to_border_distance" module.
"""

from datapipe.image.signal_to_border_distance import signal_to_border
from datapipe.image.signal_to_border_distance import signal_to_border_distance

import numpy as np

import unittest

class TestSignalToBorderDistance(unittest.TestCase):
    """
    Contains unit tests for the "image.signal_to_border_distance" module.
    """

    # Test the "signal_to_border" function ####################################

    def test_signal_to_border_example1(self):
        """Check the output of the signal_to_border function."""

        # Input image #################

        input_img = np.array([[0, 0, 0, 0],
                              [0, 1, 1, 0],
                              [0, 1, 1, 0],
                              [0, 0, 0, 0]])

        # Output image ################

        output_list = signal_to_border(input_img)

        # Expected output image #######

        expected_output_list = [4, 4]

        np.testing.assert_array_equal(output_list, expected_output_list)

    def test_signal_to_border_example2(self):
        """Check the output of the signal_to_border function."""

        # Input image #################

        input_img = np.array([[1, 1, 1, 1],
                              [1, 0, 0, 1],
                              [1, 0, 0, 1],
                              [1, 1, 1, 1]])

        # Output image ################

        output_list = signal_to_border(input_img)

        # Expected output image #######

        expected_output_list = [12, 0]

        np.testing.assert_array_equal(output_list, expected_output_list)

    def test_signal_to_border_example3(self):
        """Check the output of the signal_to_border function."""

        # Input image #################

        input_img = np.array([[1, 0, 0, 0],
                              [0, 1, 0, 0],
                              [0, 0, 1, 0],
                              [0, 0, 0, 1]])

        # Output image ################

        output_list = signal_to_border(input_img)

        # Expected output image #######

        expected_output_list = [4, 2]

        np.testing.assert_array_equal(output_list, expected_output_list)

    def test_signal_to_border_example4(self):
        """Check the output of the signal_to_border function."""

        # Input image #################

        input_img = np.array([[0, 0, 0, 0],
                              [0, 0, 0, 0],
                              [0, 0, 0, 0],
                              [0, 0, 0, 0]])

        # Output image ################

        output_list = signal_to_border(input_img)

        # Expected output image #######

        expected_output_list = [0, 0]

        np.testing.assert_array_equal(output_list, expected_output_list)

    def test_signal_to_border_example5(self):
        """Check the output of the signal_to_border function."""

        # Input image #################

        input_img = np.array([[0, 0, 0, 0, 0, 0],
                              [0, 0, 1, 1, 0, 0],
                              [0, 0, 1, 1, 0, 0],
                              [0, 0, 0, 0, 0, 0]])

        # Output image ################

        output_list = signal_to_border(input_img)

        # Expected output image #######

        expected_output_list = [4, 4]

        np.testing.assert_array_equal(output_list, expected_output_list)

    def test_signal_to_border_example6(self):
        """Check the output of the signal_to_border function."""

        # Input image #################

        input_img = np.array([[0, 1, 1, 1, 1, 0],
                              [0, 1, 0, 0, 1, 0],
                              [0, 1, 0, 0, 1, 0],
                              [0, 1, 1, 1, 1, 0]])

        # Output image ################

        output_list = signal_to_border(input_img)

        # Expected output image #######

        expected_output_list = [12, 4]

        np.testing.assert_array_equal(output_list, expected_output_list)

    def test_signal_to_border_example7(self):
        """Check the output of the signal_to_border function."""

        # Input image #################

        input_img = np.array([[0, 1, 0, 0, 0, 0],
                              [0, 0, 1, 0, 0, 0],
                              [0, 0, 0, 1, 0, 0],
                              [0, 0, 0, 0, 1, 0]])

        # Output image ################

        output_list = signal_to_border(input_img)

        # Expected output image #######

        expected_output_list = [4, 2]

        np.testing.assert_array_equal(output_list, expected_output_list)

    def test_signal_to_border_example8(self):
        """Check the output of the signal_to_border function."""

        # Input image #################

        input_img = np.array([[0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0]])

        # Output image ################

        output_list = signal_to_border(input_img)

        # Expected output image #######

        expected_output_list = [0, 0]

        np.testing.assert_array_equal(output_list, expected_output_list)

    # Test the "signal_to_border_distance" function ###########################

    def test_signal_to_border_distance_example1(self):
        """Check the output of the signal_to_border function."""

        # Input image #################

        input_img = np.array([[0, 0, 0, 0],
                              [0, 1, 1, 0],
                              [0, 1, 1, 0],
                              [0, 0, 0, 0]])

        # Output image ################

        output = signal_to_border_distance(input_img)

        # Expected output image #######

        expected_output = 1

        self.assertEqual(output, expected_output)

    def test_signal_to_border_distance_example2(self):
        """Check the output of the signal_to_border function."""

        # Input image #################

        input_img = np.array([[0, 0, 0, 0, 0, 0],
                              [0, 0, 1, 1, 0, 0],
                              [0, 0, 1, 1, 0, 0],
                              [0, 0, 0, 0, 0, 0]])

        # Output image ################

        output = signal_to_border_distance(input_img)

        # Expected output image #######

        expected_output = 1

        self.assertEqual(output, expected_output)

    def test_signal_to_border_distance_example3(self):
        """Check the output of the signal_to_border function."""

        # Input image #################

        input_img = np.array([[0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 1, 1, 0, 0],
                              [0, 0, 1, 1, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0]])

        # Output image ################

        output = signal_to_border_distance(input_img)

        # Expected output image #######

        expected_output = 2

        self.assertEqual(output, expected_output)

    def test_signal_to_border_distance_example4(self):
        """Check the output of the signal_to_border function."""

        # Input image #################

        input_img = np.array([[0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0]])

        # Output image ################

        output = signal_to_border_distance(input_img)

        # Expected output image #######

        expected_output = 2     # TODO should the function return a different result for this special case ???

        self.assertEqual(output, expected_output)

    def test_signal_to_border_distance_example5(self):
        """Check the output of the signal_to_border function."""

        # Input image #################

        input_img = np.array([[0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 1, 0, 0, 0]])

        # Output image ################

        output = signal_to_border_distance(input_img)

        # Expected output image #######

        expected_output = 0

        self.assertEqual(output, expected_output)

    def test_signal_to_border_distance_example6(self):
        """Check the output of the signal_to_border function."""

        # Input image #################

        input_img = np.array([[0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 1, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0]])

        # Output image ################

        output = signal_to_border_distance(input_img)

        # Expected output image #######

        expected_output = 1

        self.assertEqual(output, expected_output)

    def test_signal_to_border_distance_example7(self):
        """Check the output of the signal_to_border function."""

        # Input image #################

        input_img = np.array([[0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 1, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0]])

        # Output image ################

        output = signal_to_border_distance(input_img)

        # Expected output image #######

        expected_output = 2

        self.assertEqual(output, expected_output)
    

if __name__ == '__main__':
    unittest.main()
