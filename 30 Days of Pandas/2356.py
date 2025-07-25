# https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Number of Unique Subjects Taught by Each Teacher

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return teacher.groupby('teacher_id')['subject_id'].nunique().reset_index().rename(columns={'subject_id': 'cnt'}).sort_values('teacher_id')

# By: Fernando Serra
# https://github.com/fernandosserra