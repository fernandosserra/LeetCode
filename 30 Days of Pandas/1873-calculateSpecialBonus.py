# https://leetcode.com/problems/calculate-special-bonus/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Calculate Special Bonus

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    cond = (employees['employee_id'] % 2 != 0) & (~employees['name'].str.startswith('M'))
    employees['bonus'] = employees['salary'].where(cond, 0)
    return employees[['employee_id', 'bonus']].sort_values('employee_id')
    
# By: Fernando Serra
# https://github.com/fernandosserra