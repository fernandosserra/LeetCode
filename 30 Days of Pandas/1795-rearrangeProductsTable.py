# https://leetcode.com/problems/rearrange-products-table/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Rearrange Products Table

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    products = products.melt(id_vars=['product_id'], var_name='store', value_name='price')
    return products.dropna().sort_values('product_id')

# By: Fernando Serra
# https://github.com/fernandosserra