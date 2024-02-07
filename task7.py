import numpy as np
import pandas as pd

N = 1000000

c1 = np.random.randint(1, 7, N)
c2 = np.random.randint(1, 7, N)

sums = c1 + c2

sum_counts = pd.value_counts(sums)

probabilities = sum_counts / N

results_df = pd.DataFrame({'Сума': range(2, 13),
                           'Імовірність, %': (probabilities * 100).reindex(range(2, 13)).values})

print(results_df)
