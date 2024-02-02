import numpy as np

def mmr_formula_1(rank):
    return -1248.02749 * np.log(1861.20536 * rank) + 27052.29973

ranks1_values = [523, 540, 644, 717, 750, 950, 1674, 2300, 5000]

mmr1_calculated = [mmr_formula_1(rank) for rank in ranks1_values]

mmr1_provided = [9836, 9783, 9643, 9551, 9430, 9000, 8245, 8000, 7100]

for i in range(len(ranks1_values)):
    deviation = mmr1_calculated[i] - mmr1_provided[i]
    print(f"Ранг: {ranks1_values[i]}, Рассчитанный MMR: {mmr1_calculated[i]:.2f}, Предоставленный MMR: {mmr1_provided[i]}, Погрешность: {deviation:.2f}")
