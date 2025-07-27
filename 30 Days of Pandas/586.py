# https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Customer Placing the Largest Number of Orders

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    if orders.empty:
        return pd.DataFrame(columns=['customer_number'])
    
    customer_counts = orders['customer_number'].value_counts()
    
    if customer_counts.empty:
        return pd.DataFrame(columns=['customer_number'])
    
    
    max_count = customer_counts.max()
    top_customers = customer_counts[customer_counts == max_count].index.tolist()
    
    return pd.DataFrame({'customer_number': [top_customers[0]]})


# By: Fernando Serra
# https://github.com/fernandosserra