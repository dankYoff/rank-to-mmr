import numpy as np
from scipy.optimize import curve_fit

def log_function(x, a, b, c):
    return a * np.log(b * x) + c

ranks1 = np.array([1, 40, 55, 90, 131, 362, 460])
mmr1 = np.array([12800, 11860, 11686, 11400, 11077, 10152, 10000])

popt1, pcov1 = curve_fit(log_function, ranks1, mmr1)

a1, b1, c1 = popt1

print(f"Формула (набор 1): MMR = {a1:.5f} * ln({b1:.5f} * rank) + {c1:.5f}")
