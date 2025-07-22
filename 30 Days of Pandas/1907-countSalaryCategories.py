# https://leetcode.com/problems/count-salary-categories/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Count Salary Categories

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = accounts['income'] < 20000
    high = accounts['income'] > 50000
    average = ~low & ~high
    
    return pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [sum(low), sum(average), sum(high)]
    })
    
# By: Fernando Serra
# https://github.com/fernandosserra