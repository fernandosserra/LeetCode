# https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Managers with at Least 5 Direct Reports

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    manager_counts = employee['managerId'].value_counts()
    managers = manager_counts[manager_counts >= 5].index.tolist()
    
    return pd.DataFrame({'name': employee[employee['id'].isin(managers)]['name']}).sort_values('name')
    
# By: Fernando Serra
# https://github.com/fernandosserra