# https://leetcode.com/problems/patients-with-a-condition/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Patients With a Condition

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    db1Patients = patients[(patients['conditions'].str.startswith('DIAB1')) | (patients['conditions'].str.contains(' DIAB1'))]
    return db1Patients

# By: Fernando Serra
# https://github.com/fernandosserra