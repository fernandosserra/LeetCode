# https://leetcode.com/studyplan/introduction-to-pandas/
# Reshape Data: Pivot

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', columns='city', values='temperature', aggfunc='max')

# By: Fernando Serra
# https://github.com/fernandosserra