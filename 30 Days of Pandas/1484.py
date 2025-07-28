# https://leetcode.com/problems/group-sold-products-by-the-date/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Group Sold Products by The Date

import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    return activities.groupby('sell_date')['product'].agg(
        num_sold='nunique',
        products=lambda x: ','.join(sorted(x.unique()))
    ).reset_index()

# By: Fernando Serra
# https://github.com/fernandosserra