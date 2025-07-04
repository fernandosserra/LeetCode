# https://leetcode.com/studyplan/introduction-to-pandas/
# Fill Missing Data

import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(0, inplace=True)
    return products

# By: Fernando Serra
# https://github.com/fernandosserra
