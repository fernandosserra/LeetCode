# https://leetcode.com/studyplan/introduction-to-pandas/
# Drop Duplicate Rows
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=['email'])

# By: Fernando Serra
# https://github.com/fernandosserra