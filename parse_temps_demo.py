#! /usr/bin/env python3

import sys
import os
from parse_temps import parse_temperature_data
from interpolation import interpolate_piecewise
from least_squares import least_squares_fit

def process_temperature_data(input_file_path: str, output_directory: str = "outputData"): 
    """
    Processes a temperature data file, parses it, and saves structured data to text files per core.

    Args:
        input_file_path (str): Path to the input file.
        output_directory (str): Directory where processed data will be stored.
    """
    """
    Reads a temperature data file, parses it, and saves structured data to text files per core.

    Args:
        input_filename (str): Path to the input file.
        output_folder (str): Folder where processed data will be stored.
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_folder)

    base_filename = os.path.splitext(os.path.basename(input_file_path))[0]
    output_files = [os.path.join(output_directory, f"{base_filename}-{i:02}.txt") for i in range(4)]
    
    file_handles = [open(file, "w") for file in output_files]

    with open(input_file_path, "r") as temperature_file:
        previous_timestamp = None
        previous_core_temperatures = None
        timestamps = []
        core_temperatures_list = [[] for _ in range(4)]
        
        for timestamp, core_temperatures in parse_temperature_data(temperature_file):
            if prev_time is not None:
                for core_index, (previous_value, current_value) in enumerate(zip(previous_core_temperatures, core_temperatures)):
                    file_handles[core_index].write(f"{previous_timestamp} <= x < {timestamp}; y{core_index} = c0 + c1x ; interpolation
")
            
            prev_time = time
            prev_core_data = core_data
            timestamps.append(timestamp)
            for core_index in range(4):
                core_temperatures_list[core_index].append(core_temperatures[core_index])
    
    # Perform interpolation and least squares approximation
    for core_index in range(4):
        interpolation_results = interpolate_piecewise(timestamps, core_temperatures_list[core_index])
        least_squares_equation = least_squares_fit(timestamps, core_temperatures_list[core_index])
        
        with open(output_files[core_index], "a") as output_file:
            for equation in interpolation_results:
                output_file.write(equation + "
")
            output_file.write(least_squares_equation + "
")
    
    for file in file_handles:
        file.close()
    
    print(f"Processed data saved to: {output_directory}")

def main():
    """
    Main function to parse command-line arguments and initiate temperature data processing.
    """
    if len(sys.argv) < 2:
        print("Usage: python parse_temps_demo.py <input_file>")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    
    if not os.path.isfile(input_file_path):
        print(f"Error: File '{input_file_path}' not found.")
        sys.exit(1)
    
    process_temperature_data(input_file_path)

if __name__ == "__main__":
    main()
