import numpy as np


def calculate(list_mtrx):
    # The input of the function should be a list containing 9 digits.
    if len(list_mtrx) != 9:
        raise ValueError("List must contain nine numbers.")

    # The function should convert the list into a 3 x 3 Numpy array
    mtrx = np.array(list_mtrx).reshape(3, 3)

    # Return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.
    calculations = {
        'mean': [list(mtrx.mean(axis=0)), list(mtrx.mean(axis=1)), mtrx.mean()],
        'variance': [list(mtrx.var(axis=0)), list(mtrx.var(axis=1)), mtrx.var()],
        'standard deviation': [list(mtrx.std(axis=0)), list(mtrx.std(axis=1)), mtrx.std()],
        'max': [list(mtrx.max(axis=0)), list(mtrx.max(axis=1)), mtrx.max()],
        'min': [list(mtrx.min(axis=0)), list(mtrx.min(axis=1)), mtrx.min()],
        'sum': [list(mtrx.sum(axis=0)), list(mtrx.sum(axis=1)), mtrx.sum()]
    }

    print(calculations)

    return calculations
