#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------
"""
docstring
"""

from io import StringIO
from unittest import main, TestCase

from Collatz import (collatz_read, collatz_eval, cycle_length,
                     collatz_print, collatz_solve)

# -----------
# TestCollatz
# -----------

class TestCollatz(TestCase):
    # ----
    # read
    # ----
    """
    docstring
    """

    def test_read(self):
        """
        docstring
        """
        svar = "1 10\n"
        ivar, jvar = collatz_read(svar)
        self.assertEqual(ivar, 1)
        self.assertEqual(jvar, 10)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        standard test
        """
        vvar = collatz_eval(1, 10)
        self.assertEqual(vvar, 20)

    def test_eval_2(self):
        """
        reverse
        """
        vvar = collatz_eval(2444, 772)
        self.assertEqual(vvar, 183)

    def test_eval_3(self):
        """
        equal
        """
        vvar = collatz_eval(2, 2)
        self.assertEqual(vvar, 2)

    def test_cycle_length_1(self):
        """
        test cycle length
        """
        vvar = cycle_length(2)
        self.assertEqual(vvar, 2)

    def test_cycle_length_2(self):
        """
        test cycle length
        """
        vvar = cycle_length(1)
        self.assertEqual(vvar, 1)

    def test_cycle_length_3(self):
        """
        test cycle length
        """
        vvar = cycle_length(38585)
        self.assertEqual(vvar, 125)


    # -----
    # print
    # -----

    def test_print_1(self):
        """
        test print func
        """
        wvar = StringIO()
        collatz_print(wvar, 20, 10, 20)
        self.assertEqual(wvar.getvalue(), '20 10 20\n')

    def test_print_2(self):
        """
        test print func
        """
        wvar = StringIO()
        collatz_print(wvar, 1, 10, 20)
        self.assertEqual(wvar.getvalue(), '1 10 20\n')

    def test_print_3(self):
        """
        test print func
        """
        wvar = StringIO()
        collatz_print(wvar, 0, 0, 0)
        self.assertEqual(wvar.getvalue(), '0 0 0\n')

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """
        normal
        """
        rvar = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        wvar = StringIO()
        collatz_solve(rvar, wvar)
        self.assertEqual(wvar.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """
        reversed
        """
        rvar = StringIO("999 1\n")
        wvar = StringIO()
        collatz_solve(rvar, wvar)
        self.assertEqual(wvar.getvalue(), "999 1 179\n")

    def test_solve_3(self):
        """
        equal
        """
        rvar = StringIO("2 2\n")
        wvar = StringIO()
        collatz_solve(rvar, wvar)
        self.assertEqual(wvar.getvalue(), "2 2 2\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
