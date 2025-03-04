#! /usr/bin/env python3

"""
Interpolation Module for CPU Temperature Analysis.

This module provides functions to perform piecewise linear interpolation
on parsed temperature data and saves output to text files.
"""

import os
from typing import List

def perform_piecewise_linear_interpolation(timestamps: List[float], temperatures: List[float], output_file: str):
    """
    Perform piecewise linear interpolation on given data points and save the results to a file.

    Args:
        timestamps (List[float]): The x-coordinates (time values).
        temperatures (List[float]): The y-coordinates (temperature readings).
        output_file (str): Path to the output file where the results will be saved.
    """
    if len(timestamps) != len(temperatures) or len(timestamps) < 2:
        raise ValueError("Timestamps and temperatures must have the same length and at least two points.")

    with open(output_file, "w") as file:
        for i in range(len(timestamps) - 1):
            x_k, x_k1 = timestamps[i], timestamps[i + 1]
            y_k, y_k1 = temperatures[i], temperatures[i + 1]

            # Compute slope and intercept
            slope = (y_k1 - y_k) / (x_k1 - x_k)
            intercept = y_k - slope * x_k

            # Format the interpolation equation with better spacing for alignment
            equation = f"{x_k:5}  <= x <=  {x_k1:5}  ;   y = {intercept:10.4f}    +   {slope:10.4f} x   ; interpolation"
            file.write(equation + "\n")

    print(f"Interpolation results saved to: {output_file}")

if __name__ == "__main__":
    """
    Example usage for testing the interpolation function.
    """
    sample_timestamps = [0, 30, 60, 90]
    sample_temperatures = [40.0, 42.5, 43.0, 41.8]
    output_file = "outputData/sample_interpolation_output.txt"

    if not os.path.exists("outputData"):
        os.makedirs("outputData")
    
    perform_piecewise_linear_interpolation(sample_timestamps, sample_temperatures, output_file)
    print(f"Interpolation results saved to {output_file}")
    
