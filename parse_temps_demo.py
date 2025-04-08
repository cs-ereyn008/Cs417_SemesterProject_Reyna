#! /usr/bin/env python3

"""
Temperature Data Processor.

This script reads a temperature data file, detects whether it contains labels (+, °C),
performs piecewise linear interpolation, computes a global least squares line,
and writes the results into separate output files for each CPU core.

Sources:
- Concepts based on CS417 Approximation Methods notes, Professor T. Kennedy,
  https://www.cs.odu.edu/~tkennedy/cs417/latest/Public/approximationWhirlwindIntroduction/index.html

Usage:
    python parse_temps_demo.py <input_file>
"""

import sys
import os
from parse_temps import parse_raw_temps
from least_squares import compute_least_squares_coefficients

def detect_labels(filepath: str) -> bool:
    """
    Detect whether the input file contains temperature labels.

    :param filepath: Path to the input file.
    :return: True if labels (+, °C) are detected, False otherwise.
    """
    with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
        for _ in range(10):
            line = file.readline()
            if "+" in line or "°C" in line:
                return True
    return False

def generate_interpolation_lines(timestamps: list, temperatures: list) -> list:
    """
    Generate piecewise linear interpolation lines from temperature data.

    :param timestamps: List of timestamp values.
    :param temperatures: List of corresponding temperature readings.
    :return: List of formatted interpolation strings.
    """
    lines = []
    for i in range(len(timestamps) - 1):
        x0, x1 = timestamps[i], timestamps[i + 1]
        y0, y1 = temperatures[i], temperatures[i + 1]

        if x0 >= x1:
            print(f"Warning: Skipping invalid interval: {x0} to {x1}")
            continue

        slope = (y1 - y0) / (x1 - x0)
        intercept = y0 - slope * x0
        lines.append(f"{int(x0):<5} <= x <= {int(x1):<5}; y = {intercept:8.4f} + {slope:8.4f} x ; interpolation\n")
    return lines

def generate_least_squares_line(timestamps: list, temperatures: list) -> str:
    """
    Generate a least squares approximation line from temperature data.

    :param timestamps: List of timestamp values.
    :param temperatures: List of corresponding temperature readings.
    :return: Formatted least squares approximation string.
    """
    equation = compute_least_squares_coefficients(timestamps, temperatures)
    parts = equation.replace("y =", "").split("+")
    intercept = float(parts[0])
    slope = float(parts[1].replace("x", ""))
    return f"0 <= x <= {int(timestamps[-1]):<5}; y = {intercept:8.4f} + {slope:8.4f} x ; least-squares\n"

def write_output_file(filename: str, interpolation_lines: list, least_squares_line: str) -> None:
    """
    Write interpolation and least squares lines to an output file.

    :param filename: Output file path.
    :param interpolation_lines: List of interpolation strings.
    :param least_squares_line: Least squares approximation string.
    """
    with open(filename, "w") as file:
        file.writelines(interpolation_lines)
        file.write(least_squares_line)
    print(f"Interpolation results saved to: {filename}")

def process_temperature_data(input_file_path: str, output_directory: str = "outputData") -> None:
    """
    Process temperature data and generate output files for each core.

    :param input_file_path: Path to the input temperature data file.
    :param output_directory: Directory to save output files.
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    base_filename = os.path.splitext(os.path.basename(input_file_path))[0]
    output_paths = [os.path.join(output_directory, f"{base_filename}-core-{i:02}.txt") for i in range(4)]

    if not os.path.isfile(input_file_path):
        print(f"Error: File '{input_file_path}' not found.")
        sys.exit(1)

    has_labels = detect_labels(input_file_path)

    timestamps = []
    core_temperatures = [[] for _ in range(4)]

    with open(input_file_path, "r", encoding="utf-8", errors="ignore") as file:
        for timestamp, core_values in parse_raw_temps(file, has_labels=has_labels):
            timestamps.append(timestamp)
            for i in range(4):
                core_temperatures[i].append(core_values[i])

    if len(timestamps) < 2:
        print("Error: Not enough valid data points to process.")
        sys.exit(1)

    for core_index in range(4):
        interpolation_lines = generate_interpolation_lines(timestamps, core_temperatures[core_index])
        least_squares_line = generate_least_squares_line(timestamps, core_temperatures[core_index])
        write_output_file(output_paths[core_index], interpolation_lines, least_squares_line)

def main() -> None:
    """
    Parse command-line arguments and process the input file.
    """
    if len(sys.argv) < 2:
        print("Usage: python parse_temps_demo.py <input_file>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    process_temperature_data(input_file_path)

if __name__ == "__main__":
    main()
