# https://leetcode.com/studyplan/introduction-to-pandas/
# Method Chaining

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight'] > 100].sort_values('weight', ascending=False)[['name']]

# By: Fernando Serra
# https://github.com/fernandosserra