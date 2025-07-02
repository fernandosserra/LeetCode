# https://leetcode.com/studyplan/introduction-to-pandas/
# Create a DataFrame from List

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df

result = createDataframe([
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
])
print(result)

# By: Fernando Serra
# https://github.com/fernandosserra