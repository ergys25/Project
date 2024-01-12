# CSVProcessor Documentation

## Introduction

The CSVProcessor class is designed to read and combine data from multiple CSV files. It provides methods to manipulate and save the combined data.

## Constructor

### `__init__(self, file_paths)`

Initialize the CSVProcessor.

- **Parameters:**
  - `file_paths` (list): List of file paths to CSV files.

## Methods

### `read_and_combine(self)`

Read and combine data from multiple CSV files.

### `save_combined_data(self, output_file)`

Save the combined data to a CSV file.

- **Parameters:**
  - `output_file` (str): Path to the output CSV file.

### `retrieve_score_by_name(self, name)`

Retrieve the score by name from the combined data.

- **Parameters:**
  - `name` (str): Name to retrieve the score for.
- **Returns:**
  - `int` or `None`: Score for the specified name or `None` if not found.

## Example Usage

```python
# Example usage of CSVProcessor
file_paths = ["data1.csv", "data2.csv"]
csv_processor = CSVProcessor(file_paths)
csv_processor.read_and_combine()
csv_processor.save_combined_data("output_combined_data.csv")
score = csv_processor.retrieve_score_by_name("John Doe")






```

# CSV Data Generator Documentation

## Function: generate_csv

Generate a CSV file with random data using the Faker library.

### Parameters

- `file_name` (str): The name of the output CSV file.
- `num_entries` (int): The number of entries to generate.

### Usage

```python
generate_csv(file_name, num_entries)




```

# CSVProcessor Unit Test Documentation

## Import Statements

```python
import unittest
from randomCSV import generate_csv
from CSVProcessor import CSVProcessor
import os
```
