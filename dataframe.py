"""Create dataframe and check the quality

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
import pandas as pd

#import the data
DF = pd.read_csv('https://data.seattle.gov/api/views/tw7j-DFaw/rows.csv?accessType=DOWNLOAD')
DF = DF.head(100) # only fetch first 10 rows for testing

def test_datatype(DF):
    """Test if all columns have values of the correct type

    Parameters
    ----------
    DF : Pandas Dataframe
        The dataset imported as Pandas Dataframe
    Returns
    -------
    bool
        a bool value: True if the datatype of each column match
    """
    columns = list(DF)
    for name in columns:
        try:
            tp = (DF[name].map(type) == type(DF[name].iloc[1].item())).any().tolist()
        except AttributeError:
            tp = (DF[name].map(type) == type(DF[name].iloc[1])).any().tolist()
    return tp


def test_column_names(DF):
    """Test if the dataframe has expected columns

    Parameters
    ----------
    DF : Pandas Dataframe
        The dataset imported as Pandas Dataframe
    Returns
    -------
    bool
        a bool value: True if the dataframe has expected columns
    """
    DF_columns = sorted(DF.columns.tolist())
    DF_checklist = ['trip_id',
                    'starttime',
                    'stoptime',
                    'bikeid',
                    'tripduration',
                    'from_station_name',
                    'to_station_name',
                    'from_station_id',
                    'to_station_id',
                    'usertype',
                    'gender',
                    'birthyear']
    if DF_columns == sorted(DF_checklist):
        return True 

def test_nan_values(DF):
    """Test if the dataframe has non value

    Parameters
    ----------
    DF : Pandas Dataframe
        The dataset imported as Pandas Dataframe

    Returns
    -------
    bool
        a bool value: True if the dataframe has non value
    """
    return DF.notnull().values.any()

def test_least_row_counts(DF):
    """Test if the dataframe has at least one row of data

    Parameters
    ----------
    DF : Pandas Dataframe
        The dataset imported as Pandas Dataframe

    Returns
    -------
    bool
        a bool value: True if the dataframe has at least one row of data
    """
    return DF.shape[0]>=1

if __name__ == '__main__':
    """Main function

    Returns
    -------
    bool
        a bool value if the dataframe pass all the tests
    """
    #import the data
    DF = pd.read_csv('https://data.seattle.gov/api/views/tw7j-DFaw/rows.csv?accessType=DOWNLOAD')
    #only fetch first 10 rows for testing
    DF = DF.head(100) 
    print(test_column_names(DF) & test_datatype(DF) & test_least_row_counts(DF) &test_nan_values(DF))