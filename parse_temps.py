#! /usr/bin/env python3

"""
Temperature Parsing File. 

This file provides functionality to parse raw CPU temperature data, removing labels (+, °C), and creates a structured output.

Sources:
- String splitting and character cleaning based on W3Schools Python string methods: https://www.w3schools.com/python/ref_string_split.asp

Author: Emily Reyna
Course: CS 417 - Spring 2025
Language: Python 3
"""

from typing import Generator, TextIO

def parse_raw_temps(original_temps: TextIO, has_labels: bool = False, step_size: int = 30) -> Generator[tuple[float, list[float]], None, None]:
    """
    Parse a raw temperature data file, optionally removing labels.

    :param original_temps: Opened input file containing raw temperature data.
    :param has_labels: Flag indicating whether the input contains labels (+, °C).
    :param step_size: Increment for each timestamp (default is 30 seconds).
    :yield: Tuple containing timestamp and a list of core temperatures.
    """
    timestamp = 0
    for line_number, line in enumerate(original_temps, start=1):
        line = line.strip()
        if not line:
            continue

        if has_labels:
            line = line.replace("+", "").replace("°C", "")

        entries = line.split()

        # Clean each entry manually to remove non-numeric characters
        cleaned_entries = []
        for entry in entries:
            cleaned_entry = ''.join(c for c in entry if (c.isdigit() or c == '.' or c == '-'))
            if cleaned_entry:
                cleaned_entries.append(cleaned_entry)

        if len(cleaned_entries) != 4:
            print(f"Warning: Skipping invalid line {line_number}: '{line}' (found {len(cleaned_entries)} entries)")
            continue

        try:
            temperatures = [float(entry) for entry in cleaned_entries]
        except ValueError:
            print(f"Warning: Skipping invalid line {line_number}: '{line}' (non-numeric value found)")
            continue

        yield (timestamp, temperatures)
        timestamp += step_size
