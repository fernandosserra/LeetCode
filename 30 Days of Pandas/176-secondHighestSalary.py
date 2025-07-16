# https://leetcode.com/problems/second-highest-salary/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Second Highest Salary

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employeeSorted=employee.sort_values(by='salary',ascending=False)
    
    uniqueSalary=employee['salary'].drop_duplicates().nlargest(2)
    
    if len(uniqueSalary) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    else:
        return pd.DataFrame({'SecondHighestSalary': [uniqueSalary.iloc[1]]})

# By: Fernando Serra
# https://github.com/fernandosserra