# https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Replace Employee ID With The Unique Identifier

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(employees, employee_uni, on='id', how='left')[['unique_id', 'name']].rename(columns={'unique_id': 'unique_id'})

# By: Fernando Serra
# https://github.com/fernandosserra