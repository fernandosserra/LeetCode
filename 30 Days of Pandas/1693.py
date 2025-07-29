# https://leetcode.com/problems/daily-leads-and-partners/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Daily Leads and Partners

import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return daily_sales.groupby(['date_id', 'make_name']).agg(
        unique_leads=('lead_id', 'nunique'),
        unique_partners=('partner_id', 'nunique')
    ).reset_index()

# By: Fernando Serra
# https://github.com/fernandosserra