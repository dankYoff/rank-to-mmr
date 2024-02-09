import numpy as np
from scipy.optimize import curve_fit

def log_function(x, a, b, c):
    return a * np.log(b * x) + c

def mmr_formula_1(rank):
    return -1248.02749 * np.log(1861.20536 * rank) + 27052.29973

ranks1 = np.array([1, 40, 55, 90, 131, 362, 460])
mmr1_provided = np.array([12800, 11860, 11686, 11400, 11077, 10152, 10000])

popt1, pcov1 = curve_fit(log_function, ranks1, mmr1_provided)
a1, b1, c1 = popt1

print(f"Формула (набор 1): MMR = {a1:.5f} * ln({b1:.5f} * rank) + {c1:.5f}")

mmr1_calculated = [mmr_formula_1(rank) for rank in ranks1]

for i in range(len(ranks1)):
    deviation = mmr1_calculated[i] - mmr1_provided[i]
    print(f"Ранг: {ranks1[i]}, Рассчитанный MMR: {mmr1_calculated[i]:.2f}, Предоставленный MMR: {mmr1_provided[i]}, Погрешность: {deviation:.2f}")

ranks2 = np.array([523, 540, 644, 717, 750, 950, 1674, 2300, 5000])
mmr2_provided = np.array([9836, 9783, 9643, 9551, 9430, 9000, 8245, 8000, 7100])

popt2, pcov2 = curve_fit(log_function, ranks2, mmr2_provided)
a2, b2, c2 = popt2

print(f"\nФормула (набор 2): MMR = {a2:.5f} * ln({b2:.5f} * rank) + {c2:.5f}")

mmr2_calculated = [mmr_formula_1(rank) for rank in ranks2]

for i in range(len(ranks2)):
    deviation = mmr2_calculated[i] - mmr2_provided[i]
    print(f"Ранг: {ranks2[i]}, Рассчитанный MMR: {mmr2_calculated[i]:.2f}, Предоставленный MMR: {mmr2_provided[i]}, Погрешность: {deviation:.2f}")