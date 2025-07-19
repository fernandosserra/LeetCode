# https://leetcode.com/problems/rank-scores/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Rank Scores

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    return scores.sort_values('score', ascending=False)[['score', 'rank']].astype({'rank': int})

# By: Fernando Serra
# https://github.com/fernandosserra