from speedsense.tc_estimator import compute_complexity
import inspect
import itertools


def all_combinations(n):
    elements = list(range(1, n + 1))
    all_combinations_list = []
    for r in range(1, n + 1):
        for combination in itertools.combinations(elements, r):
            all_combinations_list.append(combination)
    return all_combinations_list



