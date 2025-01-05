# Testing BinaryLogisticRegression class contained in data_processing.py
# Change to the python_scripts directory first then run the script woth the following commands:
# $ cd project/python_scripts
# $ python log_reg_test.py

import numpy as np
import pandas as pd
import data_processing as dp

def create_dataframe(num_rows):
    '''Create a DataFrame with random data for testing purposes.

        Args:
            num_rows (int): The number of rows in the DataFrame.

        Returns:
            df: A DataFrame with random data used for testig.

    '''
    # Create a dictionary with random data
    data = {
        'X1': np.random.rand(num_rows),
        'X2': np.random.rand(num_rows),
        'X3': np.random.rand(num_rows),
    }
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Add the 'target' column with random 0s and 1s
    df['target'] = np.random.randint(0, 2, size=num_rows)
    
    return df

df = create_dataframe(250)

# Create a BinaryLogisticRegression object and test the methods
log_reg = dp.BinaryLogisticRegression(df, 'target')
log_reg.preprocess_data()
log_reg.train_model()
log_reg.standardize_data()
log_reg.evaluate_model()
log_reg.print_model_summary()