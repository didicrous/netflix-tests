#!/usr/bin/env python3
"""
TestNetflix.py
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
import pickle
from io       import StringIO
from unittest import main, TestCase

from Netflix import netflix_read, predict_rating, load_actual_rating, netflix_eval, netflix_print, netflix_solve

# -----------
# TestCollatz
# -----------

class TestNetflix(TestCase):
    """
    docstring
    """

    # ----
    # setUpClass()
    # ----
    @classmethod
    def setUpClass(Netflix):
        with open('/u/downing/cs/netflix-cs373/cat3238-actual.p', 'rb') as f:
            Netflix.actual_ratings = pickle.load(f)
        with open('/u/downing/cs/netflix-cs373/brb2727-cust_avg.p', 'rb') as f:
            Netflix.cust_avg_rating = pickle.load(f)
        with open('/u/downing/cs/netflix-cs373/brb2727-movie_avg.p', 'rb') as f:
            Netflix.movie_avg_rating = pickle.load(f)

    # ----
    # read
    # ----

    def test_read_1(self):
        """
        Reads a movie id
        """
        temp1 = "12345:\n"
        temp2, temp3, temp4 = netflix_read(temp1, 0)
        self.assertEqual(temp2, 12345)
        self.assertEqual(temp3, 1)
        self.assertEqual(temp4, 12345)

    def test_read_2(self):
        """
        Reads a customer id
        """
        temp1 = "12345\n"
        temp2, temp3, temp4 = netflix_read(temp1, 0)
        self.assertEqual(temp2, 12345)
        self.assertEqual(temp3, 0)
        self.assertEqual(temp4, 0)

    def test_read_3(self):
        """
        Reads a customer id
        """
        temp1 = "30878\n"
        temp2, temp3, temp4 = netflix_read(temp1, 0)
        self.assertEqual(temp2, 30878)
        self.assertEqual(temp3, 0)
        self.assertEqual(temp4, 0)
    
    # ----
    # predict
    # ----

    def test_predict_1(self):
        """
        Predicts a customer id
        """
        arg1 = 30878
        arg2 = 1
        result = predict_rating(arg1, arg2)
        self.assertEqual(result, 3.6)

    def test_predict_2(self):
        """
        Predicts a customer id
        """
        arg1 = 2647871
        arg2 = 1
        result = predict_rating(arg1, arg2)
        self.assertEqual(result, 3.4)

    def test_predict_3(self):
        """
        Predicts a customer id
        """
        arg1 = 2488120
        arg2 = 1
        result = predict_rating(arg1, arg2)
        self.assertEqual(result, 4.2)

    # ----
    # load_actual_rating
    # ----

    def test_load_actual_1(self):
        """
        Loads a value from actual_ratings cache
        """
        arg1 = 30878
        arg2 = 1
        result = load_actual_rating(arg1, arg2)
        self.assertEqual(result, 4)

    def test_load_actual_2(self):
        """
        Loads a value from actual_ratings cache
        """
        arg1 = 2647871
        arg2 = 1
        result = load_actual_rating(arg1, arg2)
        self.assertEqual(result, 4)

    def test_load_actual_3(self):
        """
        Loads a value from actual_ratings cache
        """
        arg1 = 2488120
        arg2 = 1
        result = load_actual_rating(arg1, arg2)
        self.assertEqual(result, 5)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        Evaluates a movie id
        """
        temp1, temp2 = netflix_eval(1, 1, 1)
        self.assertEqual(temp1, 1)
        self.assertEqual(temp2, -1)

    def test_eval_2(self):
        """
        Evaluates a customer id
        """
        temp1, temp2 = netflix_eval(30878, 0, 1)
        self.assertEqual(temp1, 3.6)
        self.assertEqual(temp2, -0.3999999999999999)

    def test_eval_3(self):
        """
        Evaluates a customer id
        """
        temp1, temp2 = netflix_eval(2647871, 0, 1)
        self.assertEqual(temp1, 3.4)
        self.assertEqual(temp2, -0.6000000000000001)


    # -----
    # print
    # -----

    def test_print_1(self):
        """
        Prints a movie id
        """
        temp1 = StringIO()
        netflix_print(1, 1, temp1)
        self.assertEqual(temp1.getvalue(), "1:\n")

    def test_print_2(self):
        """
        Prints a customer rating
        """
        temp1 = StringIO()
        netflix_print(3.6, 0, temp1)
        self.assertEqual(temp1.getvalue(), "3.6\n")

    def test_print_3(self):
        """
        Prints a customer rating
        """
        temp1 = StringIO()
        netflix_print(3.4, 0, temp1)
        self.assertEqual(temp1.getvalue(), "3.4\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """
        Solves for a single movie
        """
        read = StringIO("1:\n30878\n2647871\n1283744\n2488120\n317050\n1904905\n1989766\n14756\n1027056\n1149588\n1394012\n1406595\n2529547\n1682104\n2625019\n2603381\n1774623\n470861\n712610\n1772839\n1059319\n2380848\n548064\n")
        write = StringIO()
        netflix_solve(read, write)
        self.assertEqual(write.getvalue(), "1:\n3.6\n3.4\n3.6\n4.2\n3.6\n3.7\n3.5\n3.6\n3.8\n3.6\n3.3\n3.6\n3.8\n3.8\n3.2\n3.8\n3.6\n4.1\n3.9\n3.9\n3.3\n4.3\n3.6\nRMSE: 0.82\n")

    def test_solve_2(self):
        """
        Solves for a single movie
        """
        read = StringIO("10:\n1952305\n1531863\n")
        write = StringIO()
        netflix_solve(read, write)
        self.assertEqual(write.getvalue(), "10:\n3.2\n3.1\nRMSE: 0.15\n")

    def test_solve_3(self):
        """
        Solves for a single movie
        """
        read = StringIO("10000:\n200206\n523108\n")
        write = StringIO()
        netflix_solve(read, write)
        self.assertEqual(write.getvalue(), "10000:\n3.6\n3.5\nRMSE: 1.05\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
