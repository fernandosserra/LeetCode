# https://leetcode.com/problems/big-countries/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# 595. Big Countries

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    bCountries = world[(world.area >= 3000000) | (world.population >= 25000000)]
    return bCountries[['name','population','area']]

# By: Fernando Serra
# https://github.com/fernandosserra