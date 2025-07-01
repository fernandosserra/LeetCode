# https://leetcode.com/studyplan/introduction-to-pandas/
# Display the First Three Rows

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

# By: Fernando Serra
# https://github.com/fernandosserra