# https://leetcode.com/problems/big-countries/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Recyclable and Low Fat Products

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products.low_fats == 'Y') & (products.recyclable == 'Y')][['product_id']]

# By: Fernando Serra
# https://github.com/fernandosserra