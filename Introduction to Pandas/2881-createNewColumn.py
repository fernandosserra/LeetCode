# https://leetcode.com/studyplan/introduction-to-pandas/
# Create a New Column

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees

# By: Fernando Serra
# https://github.com/fernandosserra