# https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Actors and Directors Who Cooperated At Least Three Times

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    return actor_director.groupby(['actor_id', 'director_id']).filter(lambda x: len(x) >= 3)[['actor_id', 'director_id']].drop_duplicates().reset_index(drop=True)


# By: Fernando Serra
# https://github.com/fernandosserra