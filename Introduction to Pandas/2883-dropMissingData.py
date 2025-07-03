# https://leetcode.com/studyplan/introduction-to-pandas/
# Drop Missing Data

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'])

# By: Fernando Serra
# https://github.com/fernandosserra