# https://leetcode.com/problems/classes-with-at-least-5-students/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Classes With at Least 5 Students

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class').size().reset_index(name='student_count')
    return df[df['student_count'] >= 5][['class']].sort_values('class')

# By: Fernando Serra
# https://github.com/fernandosserra