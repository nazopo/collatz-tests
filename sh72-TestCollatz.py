#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

""" This module tests functions found in Collatz.py """

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    """ tests the functions in Collatz.py """
    # ----
    # read
    # ----

    def test_read_1(self):
        """
        Tests the read function
        """
        string = "1 10\n"
        start, end = collatz_read(string)
        self.assertEqual(start, 1)
        self.assertEqual(end, 10)

    def test_read_2(self):
        """
        Tests the read function
        """
        string = "17345 3458\n"
        start, end = collatz_read(string)
        self.assertEqual(start, 17345)
        self.assertEqual(end, 3458)

    def test_read_3(self):
        """
        Tests the read function
        """
        string = "645 1935\n"
        start, end = collatz_read(string)
        self.assertEqual(start, 645)
        self.assertEqual(end, 1935)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        Evaluates collatz from 1 to 10
        Cycle length will be 20
        """
        value = collatz_eval(1, 10)
        self.assertEqual(value, 20)

    def test_eval_2(self):
        """
        Evaluates collatz from 100 to 200
        Cycle length will be 125
        """
        value = collatz_eval(100, 200)
        self.assertEqual(value, 125)

    def test_eval_3(self):
        """
        Evaluates collatz from 201 to 210
        Cycle length will be 89
        """
        value = collatz_eval(201, 210)
        self.assertEqual(value, 89)

    def test_eval_4(self):
        """
        Evaluates collatz from 900 to 1000
        Cycle length will be 174
        """
        value = collatz_eval(900, 1000)
        self.assertEqual(value, 174)

    def test_eval_5(self):
        """
        Evaluates collatz from 17345 to 3458
        Cycle length will be 276
        """
        value = collatz_eval(17345, 3458)
        self.assertEqual(value, 276)

    def test_eval_6(self):
        """
        Evaluates collatz from 2500 to 2600
        Cycle length will be 178
        """
        value = collatz_eval(2500, 4500)
        self.assertEqual(value, 238)

    def test_eval_7(self):
        """
        Evaluates collatz from 2500 to 2600
        Cycle length will be 178
        """
        value = collatz_eval(2500, 4500)
        self.assertEqual(value, 238)

    # -----
    # print
    # -----

    def test_print_1(self):
        """
        Test the print
        """
        write = StringIO()
        collatz_print(write, 1, 10, 20)
        self.assertEqual(write.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """
        Test the print
        """
        write = StringIO()
        collatz_print(write, 310, 1240, 182)
        self.assertEqual(write.getvalue(), "310 1240 182\n")

    def test_print_3(self):
        """
        Test the print
        """
        write = StringIO()
        collatz_print(write, 854261, 855194, 357)
        self.assertEqual(write.getvalue(), "854261 855194 357\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """
        Tests solve write read
        """
        read = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(
            write.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """
        Tests solve write read
        """
        read = StringIO("2500 4500\n310 1240\n927 3708\n462 1386\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(
            write.getvalue(), "2500 4500 238\n310 1240 182\n927 3708 217\n462 1386 182\n")

    def test_solve_3(self):
        """
        Tests solve write read
        """
        read = StringIO(
            "854261 855194\n827665 827456\n806129 805322\n276791 280194\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(write.getvalue(
        ), "854261 855194 357\n827665 827456 419\n806129 805322 375\n276791 280194 389\n")

    # -----
    # cycle_length
    # -----

    def test_cycle_length_1(self):
        """
        Tests cycle length
        """
        value = cycle_length(5)
        self.assertEqual(value, 6)

    def test_cycle_length_2(self):
        """
        Tests cycle length
        """
        value = cycle_length(27)
        self.assertEqual(value, 112)

    def test_cycle_length_3(self):
        """
        Tests cycle length
        """
        value = cycle_length(1000)
        self.assertEqual(value, 112)

# ----
# main
# ----

if __name__ == "__main__":
    main()
