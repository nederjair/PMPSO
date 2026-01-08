import numpy as np
from random import randint


def encode_col(func_count, arg_count, use_just_states_array):
    # arg_count is the length of the argument array
    col = np.zeros(4, dtype=np.float64)
    # function of two arguments
    col[0] = randint(0, func_count)
    # first argument
    # there is no skip feature for the arguments,
    # because of that we don't start from 0 the random numbers
    col[1] = randint(1, arg_count)
    # second argument
    col[2] = randint(1, arg_count)
    # which argument array to use
    # 0-the states and qs array
    # 1-the subexpression array
    if use_just_states_array:
        col[3] = 0
    else:
        col[3] = randint(0, 1)
    return col


def encode_array(func_count, arg_count, subexpr_count, col_count, recursion_level):
    states_array_count = 3 * 2 * (recursion_level + 1)
    subexpr_array_count = 0
    for i in range(col_count):
        col = encode_col(func_count, arg_count, subexpr_count)

    pass
