# https://leetcode.com/problems/sales-person/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Sales Person

import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_company_id = company[company['name'] == 'RED']['com_id']
    
    salesperson_red_orders = orders[orders['com_id'].isin(red_company_id)]['sales_id'].unique()
    
    return sales_person[~sales_person['sales_id'].isin(salesperson_red_orders)][['name']]

# By: Fernando Serra
# https://github.com/fernandosserra