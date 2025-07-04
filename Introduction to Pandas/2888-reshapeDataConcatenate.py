# https://leetcode.com/studyplan/introduction-to-pandas/
# Reshape Data: Concatenate

import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], ignore_index=True)

# By: Fernando Serra
# https://github.com/fernandosserra