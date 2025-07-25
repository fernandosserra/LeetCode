# https://leetcode.com/problems/article-views-i/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Article Views I

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views[views.author_id == views.viewer_id][['author_id']].drop_duplicates().sort_values('author_id').rename(columns={'author_id': 'id'})

# By: Fernando Serra
# https://github.com/fernandosserra