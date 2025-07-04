# https://leetcode.com/studyplan/introduction-to-pandas/
# Change Data Type

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students

# By: Fernando Serra
# https://github.com/fernandosserra
