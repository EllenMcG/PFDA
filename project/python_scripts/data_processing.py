# python classes used as part of this project

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

class DataProcessor:
    '''
    DataProcessor class for data cleaning and preprocessing operations on a Pandas dataframe.
    '''
    def __init__(self, dataframe):
        self.df = dataframe
    
    def drop_missing_values(self):
        '''
        Drops rows with missing values from the dataframe.
        
        Args:
            Pandas dataframe

        Returns:
            drops rows with missing values from the dataframe (no return value)
        '''
        self.df = self.df.dropna(inplace=True)
    
    def drop_duplicates(self):
        '''
        Drops duplicate rows from the dataframe.
        
        Args:
            Pandas dataframe

        Returns:
            drops duplicate rows from the dataframe
        '''
        self.df = self.df.drop_duplicates(inplace=True)
        return self.df
    
    def fill_missing_values(self, value):
        '''
        Fills missing values in the dataframe with a specified value.
        
        Args:
            value: value to fill missing values with

        Returns:
            fills missing values in the dataframe with the specified value (no return value)
        '''
        self.df = self.df.fillna(value, inplace=True)
        return self.df
    
    def convert_to_datetime(self, column):
        '''
        Converts a column in the dataframe to datetime format, and sets this column to be the dataframe
        index. Lastly, it sorts the dataframe by the index.
        
        Args:
            column_name: str, name of the column to convert to datetime
        
        Returns:
            converts the specified column to datetime format 
        '''

        self.df[column] = pd.to_datetime(self.df[column])
        self.df.set_index(column, inplace=True)
        
        
        # self.df = self.df.sort_index()
        # return self.df

    def get_summary_statistics(self):
        '''
        Returns summary statistics for the dataframe.
        
        Args:
            Pandas dataframe

        Returns:
            summary statistics for the dataframe
        '''
        return self.df.describe()
    
    def convert_to_float(self, column_name):
        '''
        Converts a dataframe column to float type.
        
        Args:
            column_name: name of the column to convert

        Returns:
            converts the specified column to float type (no return value)
        '''
        self.df[column_name] = self.df[column_name].astype(float)
    
    def convert_to_int(self, column_name):
        '''
        Converts a dataframe column to int type.
        
        Args:
            column_name: name of the column to convert

        Returns:
            converts the specified column to int type (no return value)
        '''
        self.df[column_name] = self.df[column_name].astype(int)

    # def remove_rows_with_whitespace(self, columns):
    #     '''
    #     Removes rows that contain whitespace in any of the specified columns.
        
    #     Args:
    #         columns: list of column names to check for whitespace

    #     Returns:
    #         removes rows with whitespace in the specified columns (no return value)
    #     '''
    #     for column in columns:
    #         self.df = self.df[~self.df[column].str.contains(' ', na=False)]

    def remove_rows_with_whitespace(self, columns):
        '''
        Removes rows that contain whitespace in any column of the dataframe.
        
        Returns:
            removes rows with whitespace in any column (no return value)
        '''
        #self.df = self.df[~self.df.apply(lambda row: row.astype(str).str.contains(' ').any(), axis=1)]
        # self.df = self.df[~self.df.apply(lambda row: row.astype(str).str.contains(r' ').any(), axis=1)]
    
        for column in columns:
            self.df = self.df[~self.df[column].str.contains(r'\s', na=False)]

    def remove_rows_with_whitespace_or_nan(self, columns):
        '''
        Removes rows that contain whitespace or NaN in any of the specified columns of the dataframe.
    
        Args:
            columns (list): List of column names to check for whitespace or NaN.
    
        Returns:
            None
        '''
        for column in columns:
            self.df = self.df[~self.df[column].astype(str).str.startswith(' ')]
            self.df = self.df.dropna(subset=[column])

class BinaryLogisticRegression:
    '''
    Class for training and evaluating a binary logistic regression model using the scikit-learn library.
    '''
    def __init__(self, dataframe, target_column):
        self.df = dataframe
        self.target_column = target_column
        self.model = LogisticRegression(solver='lbfgs', max_iter=1000)

    def preprocess_data(self):
        '''
        Preprocesses the data by splitting it into features and target variables, and then
        splitting the data into training and testing sets (82/20 split).
        
        Args:
            Pandas dataframe

        Returns:
            X_train, X_test, y_train, y_test: training and testing sets for features and target variables
        '''
        X = self.df.drop(self.target_column, axis=1)
        y = self.df[self.target_column]
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
    
    def standardize_data(self):
        '''
        Standardizes the training and testing data using the StandardScaler.
        
        Args:
            None

        Returns:
            Standardizes the training and testing data (no return value)
        '''
        scaler = StandardScaler()
        self.X_train = scaler.fit_transform(self.X_train)
        self.X_test = scaler.transform(self.X_test)

    def train_model(self):
        '''
        Trains the logistic regression model using the training data.
        
        Args:
            None

        Returns:
            Trains the logistic regression model (no return value)
        '''
        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        '''
        Evaluates the logistic regression model using the testing data.
        
        Args:
            None

        Returns:
            accuracy: float, accuracy of the model
            confusion_matrix: confusion matrix of the model
            classification_report: classification report of the model
        '''
        y_pred = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        conf_matrix = confusion_matrix(self.y_test, y_pred)
        class_report = classification_report(self.y_test, y_pred)
        
        print(f'Accuracy: {accuracy}')
        print(f'Confusion Matrix:\n{conf_matrix}')
        print(f'Classification Report:\n{class_report}')
    

    def print_model_summary(self):
        '''
        Prints the summary of the logistic regression model including coefficients and intercepts.
        
        Args:
            None

        Returns:
            Prints the model summary (no return value)
        '''
        # print(f'Model Intercept:{self.model.intercept_}')
        # print(f'Model Coefficients:\n{self.model.coef_}')
        print("Model Coefficients:")
        for feature, coef in zip(self.df.drop(self.target_column, axis=1).columns, self.model.coef_[0]):
            print(f'{feature}: {coef}')
        print("Model Intercept:")
        print(self.model.intercept_)