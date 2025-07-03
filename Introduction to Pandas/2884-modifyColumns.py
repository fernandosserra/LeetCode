# https://leetcode.com/studyplan/introduction-to-pandas/
# Modify Columns

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees

# By: Fernando Serra
# https://github.com/fernandosserra