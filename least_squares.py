#! /usr/bin/env python3

"""
Least Squares Approximation Module.

This module computes a least squares linear approximation (best-fit line). 

Sources:
- Concepts based on CS417 Approximation Methods notes, Professor T. Kennedy, 
  https://www.cs.odu.edu/~tkennedy/cs417/latest/Public/approximationWhirlwindIntroduction/index.html

"""

from typing import List

def compute_least_squares_coefficients(timestamps: List[float], temperatures: List[float]) -> str:
    """
    Compute the least squares linear approximation from given data points.

    :param timestamps: List of x-coordinate values (time values).
    :param temperatures: List of y-coordinate values (temperature readings).
    :return: Formatted least squares approximation string.
    """
    n = len(timestamps)

    sum_x = sum(timestamps)
    sum_x2 = sum(x * x for x in timestamps)
    sum_y = sum(temperatures)
    sum_xy = sum(x * y for x, y in zip(timestamps, temperatures))

    a = n
    b = sum_x
    c = sum_x
    d = sum_x2
    e = sum_y
    f = sum_xy

    det = a * d - b * c
    if det == 0:
        raise ValueError("Determinant is zero, cannot compute least squares line.")

    inv_a = d / det
    inv_b = -b / det
    inv_c = -c / det
    inv_d = a / det

    intercept = inv_a * e + inv_b * f
    slope = inv_c * e + inv_d * f

    return f"y = {intercept:.4f} + {slope:.4f}x"
