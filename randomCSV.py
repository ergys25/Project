import csv
from faker import Faker
import random

fake = Faker()


def generate_csv(file_name, num_entries):
    """
    Generate a CSV file with random data.

    Args:
        file_name (str): The name of the output CSV file.
        num_entries (int): The number of entries to generate.

    Returns:
        None
    """
    # Open the CSV file in write mode
    with open(file_name, "w", newline="") as csvfile:
        # Define the field names for the CSV
        fieldnames = ["id", "name", "score"]
        
        # Create a CSV writer object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header row to the CSV file
        writer.writeheader()

        # Generate and write the data rows to the CSV file
        for i in range(1, num_entries + 1):
            # Generate random data for each row
            row_data = {
                "id": i,
                "name": fake.name(),
                "score": random.randint(1, 100)
            }
            
            # Write the row to the CSV file
            writer.writerow(row_data)
