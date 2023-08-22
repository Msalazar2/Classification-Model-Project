from scipy import stats
import pandas as pd


def xy_split(df):
    
    df['churn'] = df['churn'].map({'Yes': 1, 'No': 0})
    df = df.drop(columns= ['phone_service', 'multiple_lines', 'gender', 'streaming_movies'])
    
    return df.drop(columns= 'churn'), df.churn
    
    
def dummies(df):
    
    df = pd.get_dummies(df)
    df = df.drop(columns = ['online_security_No internet service', 'online_backup_No internet service', 'device_protection_No internet service', 'tech_support_No internet service', 'streaming_tv_No internet service'])
    
    return df