import numpy as np

def mmr_formula_1(rank):
    return -448.45658 * np.log(9264.01245 * rank) + 17242.22337

ranks1_values = [1, 40, 55, 90, 131, 362, 460]

mmr1_calculated = [mmr_formula_1(rank) for rank in ranks1_values]

mmr1_provided = [12800, 11860, 11686, 11400, 11077, 10152, 10000]

for i in range(len(ranks1_values)):
    deviation = mmr1_calculated[i] - mmr1_provided[i]
    print(f"Ранг: {ranks1_values[i]}, Рассчитанный MMR: {mmr1_calculated[i]:.2f}, Предоставленный MMR: {mmr1_provided[i]}, Погрешность: {deviation:.2f}")
