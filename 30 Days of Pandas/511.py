# https://leetcode.com/problems/game-play-analysis-i/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Game Play Analysis I

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.groupby('player_id')['event_date'].min().reset_index().rename(columns={'event_date': 'first_login'})

# By: Fernando Serra
# https://github.com/fernandosserra