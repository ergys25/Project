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
    with open(file_name, "w", newline="") as csvfile:
        fieldnames = ["id", "name", "score"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(1, num_entries + 1):
            writer.writerow(
                {"id": i, "name": fake.name(), "score": random.randint(1, 100)}
            )
