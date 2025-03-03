##CPU Temperature Analysis Project


Emily Reyna
Course: CS 417 - 23091
Semester Project

## Overview

This project processes CPU temperature data using Python, performing piecewise linear interpolation and least squares approximation to analyze trends. The processed data is saved in structured output files for further analysis.

## Project Structure

project-root/        
│-- inputData/                # Contains raw temperature data files        
│-- outputData/               # Stores processed output files per core        
│-- parse_temps.py            # Parses raw CPU temperature readings        
│-- parse_temps_demo.py       # Main driver script for processing temperature data        
│-- interpolation.py          # Implements piecewise linear interpolation        
│-- least_squares.py          # Computes least squares approximation        
│-- README.md                 # Project documentation        

## Requirements

- Python 3.x
- NumPy

## Installation

Clone the repository and install dependencies:
pip install numpy

## Parsing Temperature Data 

Run the main script with an input data file:
python parse_temps_demo.py inputData/sample_temperature_data.tx


This will:

1. Parse temperature readings.
2. Perform interpolation and least squares approximation.
3. Save processed data into `outputData/`.

## Interpolation Module
from interpolation import perform_piecewise_linear_interpolation

timestamps = [0, 30, 60, 90]
temperatures = [40.0, 42.5, 43.0, 41.8]
interpolated_equations = perform_piecewise_linear_interpolation(timestamps, temperatures)
for equation in interpolated_equations:
    print(equation)

## Least Squares Approximation Module
from least_squares import compute_least_squares_coefficients

timestamps = [0, 30, 60, 90]
temperatures = [40.0, 42.5, 43.0, 41.8]
print(compute_least_squares_coefficients(timestamps, temperatures))

Output Format
Each core's data is saved in separate files, named using the input filename with `-00`, `-01`, etc. Example:

outputData/sample_temperature_data-00.txt
outputData/sample_temperature_data-01.txt
outputData/sample_temperature_data-02.txt
outputData/sample_temperature_data-03.txt

Each file contains formatted interpolation and least squares equations:

0 <= x < 30; y = 40.1234 + 0.5678x ; interpolation
30 <= x < 60; y = 41.2345 + 0.6789x ; interpolation
y = 39.8765 + 0.4321x ; least-squares

## Notes

- Ensure the input data is formatted correctly before processing.
- The project is modular for easy expansion.



