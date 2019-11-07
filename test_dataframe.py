""" Test if dataframe.py works properly

This script downloads a dataset from Seattle Open Data Portal and imports
as a Pandas Dataframe.
This tool checks if the dataframe:

1. Has at least 10 rows of data
2. Contains only the columns that specified as the second argument
3. Values in each column have the same python type

This script requires that `pandas` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:
    * test_column_names - returns bool if the column name match
    * test_nan_values - returns bool if the dataframe has nan value
    * test_least_row_counts - returns bool if the dataframe has at least one row of data
    * main - the main function of the script
"""

import unittest
# import modules from hw2
import dataframe


class TestDataFrame(unittest.TestCase):
    """A class used to test the dataframe module"""

    def test_expectedcols(self):
        """A function to test if the test_column_names function works properly"""
        self.assertTrue(dataframe.test_column_names(dataframe.DATAFRAMES),
                        msg='DataFrame does not contain expexted columns')

    def test_valuetypes(self):
        """A function to test if the test_datatype function works properly"""
        self.assertTrue(dataframe.test_datatype(dataframe.DATAFRAMES),
                        msg='DataFrame columns are not of expected datatypes')

    def test_no_nan(self):
        """A function to test if the test_nan_values function works properly"""
        self.assertTrue(dataframe.test_nan_values(dataframe.DATAFRAMES),
                        msg='DataFrame contains NaN value(s)')

    def test_leastonerow(self):
        """A function to test if the test_least_row_counts function works properly"""
        self.assertTrue(dataframe.test_least_row_counts(dataframe.DATAFRAMES),
                        msg='DataFrame contains less than 1 row')


SUITE = unittest.TestLoader().loadTestsFromTestCase(TestDataFrame)
_ = unittest.TextTestRunner().run(SUITE)
