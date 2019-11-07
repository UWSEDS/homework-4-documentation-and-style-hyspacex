'''
This test module extends HW2.

1. (1 pt). Create a python module called test_dataframe.py that 
    has a test that replicates what was done in item (2) for HW2.

2. (5 pt). Add 3 tests to the module that:

    - Check that all columns have values of the corect type.
    - Check for nan values.
    - Verify that the dataframe has at least one row.
3. (1 pt). Provide a screenshot (.png) of successfully running the tests.

'''

import unittest

import dataframe # import modules from hw2

class TestDataFrame(unittest.TestCase):

    def test_expectedcols(self):
        self.assertTrue(dataframe.test_column_names(dataframe.df),
                        msg='DataFrame does not contain expexted columns')

    def test_valuetypes(self):
        self.assertTrue(dataframe.test_datatype(dataframe.df),
                        msg='DataFrame columns are not of expected datatypes')

    def test_no_nan(self):
        self.assertTrue(dataframe.test_nan_values(dataframe.df),
                        msg='DataFrame contains NaN value(s)')

    def test_leastonerow(self):
       self.assertTrue(dataframe.test_least_row_counts(dataframe.df),
                        msg='DataFrame contains less than 1 row')


suite = unittest.TestLoader().loadTestsFromTestCase(TestDataFrame)
_ = unittest.TextTestRunner().run(suite)