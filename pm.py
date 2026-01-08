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

    # encode the first array where just the array of states is used
    arg_count = states_array_count
    pm_array[0] = encode_col(func_count, arg_count, row_count)
    # force to use the array of states
    # because the array of subexpr is empty at the beginning
    pm_array[0, 3] = 0
    # now the subexpression array is not empty (has one element)
    subexpr_array_count = 1
    for i in range(1, col_count):
        # which argument array to use
        # 0-the states and qs array
        # 1-the subexpression array
        pm_array[i, 3] = randint(0, 1)
        if pm_array[i, 3] == 0:  # array of states
            arg_count = states_array_count
            pm_array[i, 0:2] = encode_col(func_count, arg_count, row_count)
        else:
            arg_count = subexpr_array_count
            pm_array[i, 0:2] = encode_col(func_count, arg_count, row_count)
        subexpr_array_count += 1
