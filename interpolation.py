#! /usr/bin/env python3

"""
Piecewise Linear Interpolation Module.

This module generates piecewise linear interpolation equations from parsed CPU temperature data.

Sources:
- Concepts based on CS417 Approximation Methods notes, Professor T. Kennedy,
  https://www.cs.odu.edu/~tkennedy/cs417/latest/Public/approximationWhirlwindIntroduction/index.html

"""

from typing import List

def perform_piecewise_linear_interpolation(timestamps: List[float], temperatures: List[float], output_file: str) -> None:
    """
    Perform piecewise linear interpolation and write equations to a file.

    :param timestamps: List of x-coordinate values (time values).
    :param temperatures: List of y-coordinate values (temperature readings).
    :param output_file: Path to the output file for interpolation results.
    :raises ValueError: If input lists are of different lengths or contain fewer than two points.
    """
    if len(timestamps) != len(temperatures) or len(timestamps) < 2:
        raise ValueError("Timestamps and temperatures must have the same length and at least two points.")

    with open(output_file, "w") as file:
        for i in range(len(timestamps) - 1):
            x0, x1 = timestamps[i], timestamps[i + 1]
            y0, y1 = temperatures[i], temperatures[i + 1]

            slope = (y1 - y0) / (x1 - x0)
            intercept = y0 - slope * x0

            equation = f"{int(x0):<5} <= x <= {int(x1):<5}; y = {intercept:8.4f} + {slope:8.4f} x ; interpolation"
            file.write(equation + "\n")
