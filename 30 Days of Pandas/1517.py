# https://leetcode.com/problems/find-users-with-valid-e-mails/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Find Users With Valid E-Mails

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    valid_email = users['mail'].str.match(r'^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\.com$')
    return users[valid_email][['user_id', 'name', 'mail']]
    
# By: Fernando Serra
# https://github.com/fernandosserra