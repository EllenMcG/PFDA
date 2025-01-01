# python_scripts/project_functions.py file contains the functions used in the Jupiter notebooks associated with the project. 
# The functions are used for data cleaning, data preprocessing, and data visualization.

import zipfile
import pandas as pd

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

def add_month_and_season(df):
    # Extract the month from the date in the index and add a new column 'month'
    df['month'] = df.index.strftime('%b')
    
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

def add_year_and_decade(df):
    # Extract the month from the date in the index and add a new column 'month'
    df['year'] = df.index.strftime('%Y')
    # df['year'] = df.index.year.astype(str)
    
    # Define a function to map months to seasons
    # def get_decade(year):
    #     if year in ['1956', '1957', '1958', '1959']:
    #         return '1950s'
    #     elif year in ['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969']:
    #         return '1960s'
    #     elif year in ['1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979']:
    #         return '1970s'
    #     elif year in ['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989']:
    #         return '1980s'
    #     elif year in ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999']:
    #         return '1990s'
    #     elif year in ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009']:
    #         return '2000s'
    #     elif year in ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']:
    #         return '2010s'
    #     elif year in ['2020', '2021', '2022', '2023', '2024', '2025']:
    #         return '2020s'
        
    def get_decade(year):
        if year in [1956, 1957, 1958, 1959]:
            return '1950s'
        elif year in [1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969]:
            return '1960s'
        elif year in [1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979]:
            return '1970s'
        elif year in [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989]:
            return '1980s'
        elif year in [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]:
            return '1990s'
        elif year in [200, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]:
            return '2000s'
        elif year in [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]:
            return '2010s'
        elif year in [2020, 2021, 2022, 2023, 2024]:
            return '2020s'
    
    # Apply the function to create the 'season' column
    df['decade'] = df['year'].apply(get_decade)
