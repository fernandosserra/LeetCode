# https://leetcode.com/problems/students-and-examinations/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Students and Examinations

import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    all_combinations = pd.merge(
        students, subjects, how='cross'
    ).sort_values(
        by=['student_id', 'subject_name']
    )

    exam_counts = examinations.groupby(
        ['student_id', 'subject_name'],
    ).agg(
        attended_exams=('subject_name', 'count')
    ).reset_index()

    merged_df = pd.merge(
        left=all_combinations,
        right=exam_counts,
        how='left',
        on=['student_id', 'subject_name'],
    )

    merged_df['attended_exams'] = merged_df['attended_exams'].fillna(0)

    return merged_df[[
        'student_id', 'student_name', 'subject_name', 'attended_exams'
    ]]
    
# By: Fernando Serra
# https://github.com/fernandosserra