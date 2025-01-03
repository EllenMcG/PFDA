# python_scripts/project_functions.py file contains the functions used in the Jupiter notebooks associated with the project. 
# The functions are used for data cleaning, data preprocessing, and data visualization.

import zipfile
import pandas as pd
import re 
from datetime import datetime

def extract_zip(zip_file, extract_dir):
    '''
    Extracts a zip file to a specified directory using the zipfile module.

    args:
        zip_file: str, path to the zip file to be extracted
        extract_dir: str, path to the directory where the zip file will be extracted
    
    returns:
        Extracts the zip file to the specified directory called extract_dir (no return value)
    '''

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)


def capitalize_month(date_str):
    '''
    Function to capitalize the month in a date string.

    Args:
        date_str: str, date string in the format 'dd-mmm-yyyy HH:MM'

    Returns:
        str, date string with the month capitalized
    '''

    return pd.to_datetime(date_str, format='%d-%b-%Y %H:%M').strftime('%d-%b-%Y %H:%M')

# def add_month_and_season(df):
#     # Extract the month from the date in the index and add a new column 'month'
#     df['month'] = df.index.strftime('%b')
    
#     # Define a function to map months to seasons
#     def get_season(month):
#         if month in ['Dec', 'Jan', 'Feb']:
#             return 'Winter'
#         elif month in ['Mar', 'Apr', 'May']:
#             return 'Spring'
#         elif month in ['Jun', 'Jul', 'Aug']:
#             return 'Summer'
#         elif month in ['Sep', 'Oct', 'Nov']:
#             return 'Autumn'
    
#     # Apply the function to create the 'season' column
#     df['season'] = df['month'].apply(get_season)
    
#     return df


def extract_month(date_str):
    '''
    Extracts the three-letter month from a date string.

    Args:
        date_str: str, date string in the format 'dd-MMM-yyyy'

    Returns:
        str, the three-letter month
    '''
    # Regular expression to match the three-letter month
    match = re.search(r'-([A-Za-z]{3})-', date_str)
    if match:
        return match.group(1)
    else:
        return None

def add_month_and_season(df):
    # Extract the month from the date column and add a new column 'month'
    df['month'] = df['date'].apply(extract_month)
    
    # Define a function to map months to seasons
    def get_season(month):
        if month in ['Dec', 'Jan', 'Feb']:
            return 'Winter'
        elif month in ['Mar', 'Apr', 'May']:
            return 'Spring'
        elif month in ['Jun', 'Jul', 'Aug']:
            return 'Summer'
        elif month in ['Sep', 'Oct', 'Nov']:
            return 'Autumn'
    
    # Apply the function to create the 'season' column
    df['season'] = df['month'].apply(get_season)
    
    return df

def extract_year(date_str):
    '''
    Extracts the year from a date string.

    Args:
        date_str: str, date string in the format 'dd-MMM-yyyy HH:MM'

    Returns:
        int, the year
    '''
    # Parse the date string to a datetime object
    date_obj = datetime.strptime(date_str, '%d-%b-%Y %H:%M')
    # Extract the year from the datetime object
    return date_obj.year

def add_year_and_decade(df):
    '''
    Extract the year from the date column and add a new column 'year' to the dataframe.
    Using this year column, create a new column 'decade' that groups the years into decades.

    Args:
        df: pd.DataFrame, dataframe containing a date column

    Returns:
        pd.DataFrame, dataframe with new columns 'year' and 'decade'
    '''
    # Extract the year from the date column and add a new column 'year'
    df['year'] = df['date'].apply(extract_year)
    
    # Create the 'decade' column by grouping the years into decades
    df['decade'] = (df['year'] // 10) * 10
    df['decade'] = df['decade'].astype(str) + 's'
    
    return df



# def add_year_and_decade(df):
#     '''
#     Extract the year from the date in the index and add a new column 'year' to the dataframe.
#     Using this year column, create a new column 'decade' that groups the years into decades.

#     Ags:
#         df: pd.DataFrame, dataframe containing a datetime index

#     Returns:
#         pd.DataFrame, dataframe with new columns 'year' and 'decade'
#     '''

#     df['year'] = df.index.year #. strftime('%Y') could hbave been used, year is already an integer so no need to 
#     # convert to string and then back to integer

#     df['decade'] = ((df['year'] // 10) * 10).astype(str) + 's'
#     return df

# def extract_year(date_str):
#     '''
#     Extracts the year from a date string.

#     Args:
#         date_str: str, date string in the format 'dd-MMM-yyyy HH:MM'

#     Returns:
#         int, the year
#     '''
#     # Regular expression to match the year
#     match = re.search(r'(\d{4})', date_str)
#     if match:
#         return int(match.group(1))
#     else:
#         return None

# def add_year_and_decade(df):
#     '''
#     Extract the year from the date column and add a new column 'year' to the dataframe.
#     Using this year column, create a new column 'decade' that groups the years into decades.

#     Args:
#         df: pd.DataFrame, dataframe containing a date column

#     Returns:
#         pd.DataFrame, dataframe with new columns 'year' and 'decade'
#     '''
#     # Extract the year from the date column and add a new column 'year'
#     df['year'] = df['date'].apply(extract_year)
    
#     # Create the 'decade' column by grouping the years into decades
#     df['decade'] = ((df['year'] // 10) * 10).astype(str) + 's'
#     # df['decade'] = df['year'].apply(lambda x: (x // 10) * 10 if x is not None else None).astype(str) + 's'
    

#     return df

def calculate_power(windspeed_knots):
    ''''
    Function to calculate the power (P in watts) generated using the windspeed (wdsp in kt) of the dataframe. As the windspeed is measured in knots, 
    the formula used to calculate the power needs to convert the windspeed to m/s. The formula used to calculate the power generated 
    is P = 0.5 * rho * A * Cp * V^3, where rho is the air density in kilograms per cubic meter (1.225 kg/m^3), A is the swept area in 
    square meters (assumed to be 1 m^2), Cp is the power coefficient (assumed to be 0.4), and V is the windspeed in m/s.
    
    Args:
        windspeed_knots: float, windspeed in knots

    Returns:
        float, power generated in watts
    '''

    # Conversion factor from knots to m/s (1 knot = 0.514444 m/s)
    windspeed_mps = windspeed_knots * 0.514444
    rho = 1.225
    A = 1
    Cp = 0.4
    power = 0.5 * rho * A * Cp * windspeed_mps**3
    return power