#! /usr/bin/env python3

"""
Interpolation Module for CPU Temperature Analysis.

This module provides functions to perform piecewise linear interpolation
on parsed temperature data.
"""

import numpy as np
from typing import List

def perform_piecewise_linear_interpolation(timestamps: List[float], temperatures: List[float]) -> List[str]:
    """
    Perform piecewise linear interpolation on given data points.

    Args:
        timestamps (List[float]): The x-coordinates (time values).
        temperatures (List[float]): The y-coordinates (temperature readings).

    Returns:
        List[str]: Formatted interpolation equations.
    """
    interpolation_equations = []

    for index in range(len(timestamps) - 1):
        lower_bound_time, upper_bound_time = timestamps[index], timestamps[index + 1]
        lower_bound_temp, upper_bound_temp = temperatures[index], temperatures[index + 1]
        
        # Calculate linear interpolation coefficients
        slope = (upper_bound_temp - lower_bound_temp) / (upper_bound_time - lower_bound_time)
        intercept = lower_bound_temp - slope * lower_bound_time

        interpolation_equations.append(
            f"{lower_bound_time} <= x < {upper_bound_time}; y = {intercept:.4f} + {slope:.4f}x ; interpolation"
        )

    return interpolation_equations

    
