# https://leetcode.com/studyplan/introduction-to-pandas/
# Reshape Data: Melt

import pandas as pd

def meltTable(products: pd.DataFrame) -> pd.DataFrame:
    return products.melt(id_vars=['category'], var_name='store', value_name='price')

# By: Fernando Serra
# https://github.com/fernandosserra