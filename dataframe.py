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

DATAFRAMES = pd.read_csv(
    'https://data.seattle.gov/api/views/tw7j-df_importaw/rows.csv?accessType=DOWNLOAD')

def test_datatype(df_import):
    """Test if all columns have values of the correct type

    Parameters
    ----------
    df_import : Pandas Dataframe
        The dataset imported as Pandas Dataframe
    Returns
    -------
    bool
        a bool value: True if the datatype of each column match
    """
    columns = list(df_import)
    for name in columns:
        try:
            tp_name = (
                isinstance(
                    df_import[name].iloc[1].item(),
                    df_import[name].map(type))).any().tolist()
        except AttributeError:
            tp_name = (
                isinstance(
                    df_import[name].iloc[1],
                    df_import[name].map(type))).any().tolist()
    return tp_name


def test_column_names(df_import):
    """Test if the dataframe has expected columns

    Parameters
    ----------
    df_import : Pandas Dataframe
        The dataset imported as Pandas Dataframe
    Returns
    -------
    bool
        a bool value: True if the dataframe has expected columns
    """
    df_import_columns = sorted(df_import.columns.tolist())
    df_import_checklist = ['trip_id',
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
    if df_import_columns == sorted(df_import_checklist):
        return True


def test_nan_values(df_import):
    """Test if the dataframe has non value

    Parameters
    ----------
    df_import : Pandas Dataframe
        The dataset imported as Pandas Dataframe

    Returns
    -------
    bool
        a bool value: True if the dataframe has non value
    """
    return df_import.notnull().values.any()


def test_least_row_counts(df_import):
    """Test if the dataframe has at least one row of data

    Parameters
    ----------
    df_import : Pandas Dataframe
        The dataset imported as Pandas Dataframe

    Returns
    -------
    bool
        a bool value: True if the dataframe has at least one row of data
    """
    return df_import.shape[0] >= 1


if __name__ == '__main__':
    """Main function

    Returns
    -------
    bool
        a bool value if the dataframe pass all the tests
    """
    DATAFRAME = pd.read_csv(
        'https://data.seattle.gov/api/views/tw7j-df_importaw/rows.csv?accessType=DOWNLOAD')
    # only fetch first 10 rows for testing
    DATAFRAME = DATAFRAME.head(10)
    print(test_column_names(DATAFRAME) & test_datatype(DATAFRAME) &
          test_least_row_counts(DATAFRAME) & test_nan_values(DATAFRAME))
