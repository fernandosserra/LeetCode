# https://leetcode.com/problems/find-total-time-spent-by-each-employee/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Find Total Time Spent by Each Employee

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    return employees.groupby(['emp_id', 'event_day'])['total_time'].sum().reset_index().rename(columns={'event_day': 'day'})

# By: Fernando Serra
# https://github.com/fernandosserra