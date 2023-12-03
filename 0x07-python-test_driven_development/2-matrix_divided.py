#!/usr/bin/python3
"""

This is 2-matrix_divided module

"""


def matrix_divided(matrix, div):
    """_summary_

    Args:
        matrix (_type_): _description_
        div (_type_): _description_

    Raises:
        TypeError: _description_
        ZeroDivisionError: _description_
        TypeError: _description_
        TypeError: _description_

    Returns:
        _type_: _description_
    """
    result = [[]]
    row_size = 0
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        new_row = []
        for column in row:
            if not isinstance(column, int) and not isinstance(column, float):
                raise TypeError("matrix must be a matrix (list of lists)"
                                "of integers/floats")
            else:
                new_row.append(float("{:.2f}".format(column / div)))
        if row_size == 0:
            row_size = len(new_row)
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        result.append(new_row)
    return result
