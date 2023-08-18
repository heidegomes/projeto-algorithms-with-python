def study_schedule(permanence_period, target_time):
    saida = 0
    if not target_time:
        return None
    for i in permanence_period:
        if not isinstance(i[0], int) or not isinstance(i[1], int):
            return None
        if i[0] <= target_time <= i[1]:
            saida += 1

    return saida


print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 2))
