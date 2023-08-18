def study_schedule(permanence_period, target_time):
    saida = 0
    n = len(permanence_period)  # N será a quantidade de elementos da lista
    for index in range(0, n):  # vamos iterar a lista completa
        if permanence_period[index] == target_time:
            saida += 1

    return saida
    raise NotImplementedError


print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 2))
