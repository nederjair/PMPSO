import numpy as np
from random import randint


def encode_col(func_count, arg_count, row_count):
    # arg_count is the length of the argument array
    col = np.zeros(row_count, dtype=int)
    # function of two arguments
    col[0] = randint(0, func_count)
    # first argument
    # there is no skip feature for the arguments,
    # because of that we don't start from 0 the random numbers
    col[1] = randint(1, arg_count)
    # second argument
    col[2] = randint(1, arg_count)
    return col


def encode_array(func_count, row_count, col_count, recursion_level):
    states_array_count = 3 * 2 * (recursion_level + 1)
    pm_array = np.zeros((row_count, col_count), dtype=int)

    # encode the first col where just the array of states is used
    pm_array[0, 0] = randint(0, func_count)
    pm_array[0, 1] = randint(0, states_array_count)
    pm_array[0, 2] = randint(0, states_array_count)
    # force to use the array of states
    # because the array of subexpr is empty at the beginning
    pm_array[0, 3] = 0
    pm_array[0, 4] = 0
    # now the subexpression array is not empty (has one element)
    subexpr_array_count = 1
    for i in range(1, col_count):
        pm_array[i, 0] = randint(0, func_count)
        # which argument array to use
        # 0-the states and qs array
        # 1-the subexpression array
        pm_array[i, 3] = randint(0, 1)
        pm_array[i, 4] = randint(0, 1)
        if pm_array[i, 3] == 0:  # array of states
            pm_array[i, 1] = randint(0, states_array_count)
        else:
            pm_array[i, 1] = randint(0, subexpr_array_count)
        if pm_array[i, 4] == 0:  # array of states
            pm_array[i, 2] = randint(0, states_array_count)
        else:
            pm_array[i, 2] = randint(0, subexpr_array_count)
        subexpr_array_count += 1


def decode(x, q, n, array, col_count, recursion_level):
    states_array_count = 3 * 2 * (recursion_level + 1)
    states_array = np.zeros(states_array_count, dtype=np.float64)
    # assembly the states
    for k in range(recursion_level):
        states_array[k * 3 : (k + 1) * 3] = x[:, n - k]
    states_array[(recursion_level + 1) * 3] = q
    for i in range(col_count):
        col = array[:, i]
        func_index = col[0]
        a1_index = col[1]
        a2_index = col[2]
        arg1_selection_index = col[3]
        arg2_selection_index = col[4]

        func = func_array[func_index]
        if arg1_selection_index == 0:
            a1 = states_array[a1_index]
        else:
            a1 = subexpr_array[a1_index]
        if arg2_selection_index == 0:
            a2 = states_array[a2_index]
        else:
            a2 = subexpr_array[a2_index]

        col_value = func(a1, a2)
