import numpy as np
from scipy.optimize import curve_fit

def log_function(x, a, b, c):
    return a * np.log(b * x) + c

ranks2 = np.array([523, 540, 644, 717, 750, 950, 1674, 2300, 5000])
mmr2 = np.array([9836, 9783, 9643, 9551, 9430, 9000, 8245, 8000, 7100])

popt2, pcov2 = curve_fit(log_function, ranks2, mmr2)

a2, b2, c2 = popt2

print(f"Формула (набор 2): MMR = {a2:.5f} * ln({b2:.5f} * rank) + {c2:.5f}")
