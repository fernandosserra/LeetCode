# https://leetcode.com/problems/department-highest-salary/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Department Highest Salary

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    highest = employee.groupby('departmentId')['salary'].transform(max) == employee['salary']
    return pd.merge(employee[highest], department, left_on='departmentId', right_on='id')[['name_y', 'name_x', 'salary']].rename(columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})

# By: Fernando Serra
# https://github.com/fernandosserra