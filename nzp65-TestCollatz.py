#!/usr/bin/env python3
"""
This file is used to perform the unit testing of the Collatz class
"""
# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz(TestCase):
    """
    Class to perform the unit testing of Collatz file
    """
    # ----
    # read
    # ----

    def test_read(self):
        """
        Test if read method will work
        """
        non_split_input = "1 10\n"
        start, end = collatz_read(non_split_input)
        self.assertEqual(start, 1)
        self.assertEqual(end, 10)

    def test_read1(self):
        """
        Test if read method will work
        """
        non_split_input = "34 75\n"
        start, end = collatz_read(non_split_input)
        self.assertEqual(start, 34)
        self.assertEqual(end, 75)

    def test_read2(self):
        """
        Test if read method will work
        """
        non_split_input = "1257 1637\n"
        start, end = collatz_read(non_split_input)
        self.assertEqual(start, 1257)
        self.assertEqual(end, 1637)

    def test_read3(self):
        """
        Test if read method will work
        """
        non_split_input = "90 34\n"
        start, end = collatz_read(non_split_input)
        self.assertEqual(start, 90)
        self.assertEqual(end, 34)

    def test_read4(self):
        """
        Test if read method will work
        """
        non_split_input = "156 245\n"
        start, end = collatz_read(non_split_input)
        self.assertEqual(start, 156)
        self.assertEqual(end, 245)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        Test if eval method will work
        """
        max_cycle_length = collatz_eval(1, 10)
        self.assertEqual(max_cycle_length, 1)

    def test_eval_2(self):
        """
        Test if eval method will work
        """
        max_cycle_length = collatz_eval(100, 200)
        self.assertEqual(max_cycle_length, 1)

    def test_eval_3(self):
        """
        Test if eval method will work
        """
        max_cycle_length = collatz_eval(201, 210)
        self.assertEqual(max_cycle_length, 1)

    def test_eval_4(self):
        """
        Test if eval method will work
        """
        max_cycle_length = collatz_eval(900, 1000)
        self.assertEqual(max_cycle_length, 1)

    def test_eval_5(self):
        """
        Test if eval method will work
        """
        max_cycle_length = collatz_eval(345, 537)
        self.assertEqual(max_cycle_length, 20)

    def test_eval_6(self):
        """
        Test if eval method will work
        """
        max_cycle_length = collatz_eval(428, 736)
        self.assertEqual(max_cycle_length, 125)

    def test_eval_7(self):
        """
        Test if eval method will work
        """
        max_cycle_length = collatz_eval(149, 235)
        self.assertEqual(max_cycle_length, 89)

    def test_eval_8(self):
        """
        Test if eval method will work
        """
        max_cycle_length = collatz_eval(1474, 1305)
        self.assertEqual(max_cycle_length, 174)

    # -----
    # print
    # -----

    def test_print(self):
        """
        Test if print method will work
        """
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print1(self):
        """
        Test if print method will work
        """
        writer = StringIO()
        collatz_print(writer, 234, 156, 128)
        self.assertEqual(writer.getvalue(), "234 156 128\n")

    def test_print2(self):
        """
        Test if print method will work
        """
        writer = StringIO()
        collatz_print(writer, 648, 783, 171)
        self.assertEqual(writer.getvalue(), "648 783 171\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """
        Test if solve method will work
        """
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1(self):
        """
        Test if solve method will work
        """
        reader = StringIO("347 582\n649 825\n159 193\n394 647\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "347 582 142\n649 825 171\n159 193 125\n394 647 142\n")

    def test_solve_2(self):
        """
        Test if solve method will work
        """
        reader = StringIO("493 729\n382 541\n163 427\n348 629\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "493 729 171\n382 541 142\n163 427 144\n348 629 142\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
