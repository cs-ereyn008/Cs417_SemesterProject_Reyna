# CPU Temperature Analysis Project


Emily Reyna  
Course: CS 417 - 23091  
Semester Project  

## Overview

This project processes CPU temperature data using Python, performing piecewise linear interpolation and least squares approximation to analyze trends. The processed data is saved in structured output files for further analysis.

## Project Structure

```
project-root/        
│-- inputData/                # Contains raw temperature data files        
│-- outputData/               # Stores processed output files per core        
│-- README.md                 # Project documentation               
│-- parse_temps.py            # Parses raw CPU temperature readings        
│-- parse_temps_demo.py       # Main driver script for processing temperature data        
│-- interpolation.py          # Implements piecewise linear interpolation        
│-- least_squares.py          # Computes least squares approximation        
```
 
## Requirements

- Python 3.x  
- NumPy  

## Installation

Clone the repository and install dependencies:
```sh
pip install numpy
```

## Parsing Temperature Data

The program reads temperature data from an input file, extracts numerical values, and processes core temperatures at regular time intervals. The extracted data is then used for interpolation and least squares approximation. The parser is designed to handle formatted sensor readings while ensuring compatibility with various input structures.

### Parsing Function
The `parse_raw_temps` function:
- Extracts CPU temperature readings at each timestep.
- Uses a regex pattern to split and parse numerical values.
- Outputs structured data as a tuple containing the timestamp and a list of core temperatures.

## Main Driver
Run the main script with an input data file:
```sh
python parse_temps_demo.py inputData/sample_temperature_data.txt #Change the sample_temperature_data.txt file to match your file name
```

This will:

1. Parse temperature readings.
2. Perform interpolation and least squares approximation.
3. Save processed data into `outputData/`.

## Interpolation Module

The interpolation module is responsible for performing piecewise linear interpolation on parsed temperature data. It computes interpolation equations for different time intervals and saves the results to structured text files for further analysis.

### Interpolation Function Behavior:
- Processes time-series temperature data by computing linear interpolation equations.
- Formats output to align equations properly for readability.
- Saves results to structured text files per core in `outputData/`.
- Follows the `{basename}-core-{i}.txt` naming convention.


## Least Squares Approximation Module (To be implemented)
```python
from least_squares import compute_least_squares_coefficients

timestamps = [0, 30, 60, 90]
temperatures = [40.0, 42.5, 43.0, 41.8]
print(compute_least_squares_coefficients(timestamps, temperatures))
```

## Output Format
Each core's data is saved in separate files, named using the input filename with `-core-0`, `-core-1`, etc. Example:
```
outputData/sample_temperature_data-core-0.txt
outputData/sample_temperature_data-core-1.txt
outputData/sample_temperature_data-core-2.txt
outputData/sample_temperature_data-core-3.txt
```

Each file contains formatted interpolation and least squares equations:
```
 0  <= x <=  30   ;   y =  40.1234    +   0.5678 x   ; interpolation
30  <= x <=  60   ;   y =  41.2345    +   0.6789 x   ; interpolation
y =  39.8765    +   0.4321 x   ; least-squares
```
