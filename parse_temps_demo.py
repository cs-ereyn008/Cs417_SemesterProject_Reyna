#! /usr/bin/env python3

import sys
import os
from parse_temps import parse_raw_temps
import interpolation  # Import as a module to avoid circular import issues

def process_temperature_data(input_file_path: str, output_directory: str = "outputData"): 
    """
    Processes a temperature data file, parses it, and saves structured data to text files per core.

    Args:
        input_file_path (str): Path to the input file.
        output_directory (str): Directory where processed data will be stored.
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    base_filename = os.path.splitext(os.path.basename(input_file_path))[0]
    output_files = [os.path.join(output_directory, f"{base_filename}-core-{i:02}.txt") for i in range(4)]
    
    # Ensure files are overwritten if they already exist
    for file in output_files:
        if os.path.exists(file):
            os.remove(file)
    
    file_handles = [open(file, "w") for file in output_files]

    with open(input_file_path, "r") as temperature_file:
        previous_timestamp = None
        previous_core_temperatures = None
        timestamps = []
        core_temperatures_list = [[] for _ in range(4)]
        
        for timestamp, core_temperatures in parse_raw_temps(temperature_file):
            if previous_timestamp is not None:
                for core_index in range(4):
                    file_handles[core_index].write(
                        f"{previous_timestamp:<6} <= x < {timestamp:<6};   y{core_index} = {core_temperatures[core_index]:>10.4f}  + {0.0000:>10.4f} x  ; interpolation\n"
                    )
            
            previous_timestamp = timestamp
            previous_core_temperatures = core_temperatures
            timestamps.append(timestamp)
            for core_index in range(4):
                core_temperatures_list[core_index].append(core_temperatures[core_index])
    
    # Perform interpolation
    for core_index in range(4):
        interpolation.perform_piecewise_linear_interpolation(timestamps, core_temperatures_list[core_index], output_files[core_index])
    
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
