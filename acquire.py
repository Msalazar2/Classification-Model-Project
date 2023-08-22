#Import libraries and functions
import os

import pandas as pd

from env import get_connection
    
#function that reads telco.csv file if it exists already. If not it retrieves telco data from MySQL and stores it as a csv.    
def get_telco_data():

    filename = 'telco.csv'
    
    if os.path.isfile(filename):
        
        print('found data')
    
        return pd.read_csv(filename)

    else:
        
        print('retrieving data')
        
        url = get_connection('telco_churn')
        
        query = '''
                SELECT 
                customers.customer_id,
                customers.gender,
                customers.senior_citizen,
                customers.partner,
                customers.dependents,
                customers.tenure,
                customers.phone_service,
                customers.multiple_lines,
                customers.internet_service_type_id,
                customers.online_security,
                customers.online_backup,
                customers.device_protection,
                customers.tech_support,
                customers.streaming_tv,
                customers.streaming_movies,
                customers.contract_type_id,
                customers.paperless_billing,
                customers.payment_type_id,
                customers.monthly_charges,
                customers.total_charges,
                customers.churn,
                customer_signups.signup_date,
                customer_churn.churn_month,
                payment_types.payment_type,
                contract_types.contract_type,
                internet_service_types.internet_service_type
                FROM
                customers
                LEFT JOIN customer_details ON customer_details.customer_id =
                customers.customer_id
                LEFT JOIN customer_contracts ON customer_contracts.customer_id =
                customer_details.customer_id
                LEFT JOIN customer_payments ON customer_payments.customer_id =
                customer_contracts.customer_id
                LEFT JOIN
                customer_signups ON customer_signups.customer_id = 
                customer_payments.customer_id
                LEFT JOIN
                customer_subscriptions ON customer_subscriptions.customer_id =
                customer_signups.customer_id
                LEFT JOIN
                customer_churn ON customer_churn.customer_id = 
                customer_subscriptions.customer_id
                LEFT JOIN
                payment_types ON payment_types.payment_type_id = 
                customers.payment_type_id
                LEFT JOIN
                contract_types ON contract_types.contract_type_id = 
                customer_contracts.contract_type_id
                LEFT JOIN
                internet_service_types ON 
                internet_service_types.internet_service_type_id = 
                customers.internet_service_type_id;
                '''
        
        df = pd.read_sql(query, url)
        
        df.to_csv(filename, index = 0)
        
        return df
    