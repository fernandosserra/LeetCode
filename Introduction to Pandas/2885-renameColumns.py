# https://leetcode.com/studyplan/introduction-to-pandas/
# Rename Columns

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(columns={'id': 'student_id','first': 'first_name', 'last': 'last_name' , 'age': 'age_in_years'}, inplace=True)
    return students

# By: Fernando Serra
# https://github.com/fernandosserra