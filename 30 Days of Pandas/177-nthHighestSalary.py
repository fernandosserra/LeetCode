# https://leetcode.com/problems/nth-highest-salary/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Nth Highest Salary

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    if not isinstance(N, int) or N <= 0:
        # Se N é inválido, o LeetCode espera um "null" (NaN em Pandas)
        return pd.DataFrame({f"getNthHighestSalary({N})": [np.nan]})
    

    # Passo 1: Remover duplicatas e ordenar os salários em ordem decrescente.
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)

    # Passo 2: Tentar pegar o N-ésimo salário.
    try:
        nth_highest_val = unique_salaries.iloc[N - 1]
    except IndexError:
        nth_highest_val = None

    # Passo 3: Criar o DataFrame de resultado com o nome da coluna correto.
    result_df = pd.DataFrame({f"getNthHighestSalary({N})": [nth_highest_val]})

    return result_df

# By: Fernando Serra
# https://github.com/fernandosserra