# https://leetcode.com/problems/delete-duplicate-emails/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Delete Duplicate Emails

import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id', ascending=True, inplace=True)
    person.drop_duplicates(subset='email', keep='first', inplace=True)

# By: Fernando Serra
# https://github.com/fernandosserra