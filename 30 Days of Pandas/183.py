# https://leetcode.com/problems/customers-who-never-order/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Customers Who Never Order

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    nOrder = customers[~customers.id.isin(orders.customerId)]
    
    result_df = nOrder[['name']]
    result_df = nOrder.rename(columns={'name': 'Customers'})
    
    return result_df[['Customers']]


# By: Fernando Serra
# https://github.com/fernandosserra