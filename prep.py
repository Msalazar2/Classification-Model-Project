#Import libraries and functions.
import pandas as pd

from sklearn.model_selection import train_test_split
from acquire import get_telco_data


#function to drop columns in preparation phase.
def drop_cols(df):
    
    df = df.drop(columns = ['customer_id', 'internet_service_type_id', 'contract_type_id', 'payment_type_id', 'churn_month', 
                            'signup_date'])
    
    return df


#function to cast object type to float.
def change_dtype(df):

    df.total_charges = df.total_charges.replace(' ', 0)
    df.total_charges = df.total_charges.astype(float)
    
    return df
    

#function to split data into train, val, test
def train_val_test(df, strat, seed = 42):

    train, val_test = train_test_split(df, train_size = 0.7,
                                       random_state = seed,
                                       stratify = df[strat])
    
    val, test = train_test_split(val_test, train_size = 0.5,
                                 random_state = seed,
                                 stratify = val_test[strat])
    
    return train, val, test
        
    
    return df


#this function combines other functions for data preparation
def telco_pipeline():
    
    df = get_telco_data()
    
    df = drop_cols(df)
    
    df = change_dtype(df)
    
    train, val, test = train_val_test(df, 'churn')
    
    return train, val, test