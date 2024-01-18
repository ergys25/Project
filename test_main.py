import unittest
from randomCSV import generate_csv
from CSVProcessor import CSVProcessor
import os


# Define a test class for CSVProcessor
class TestCSVProcessor(unittest.TestCase):
    def setUp(self):
        # Generate a random CSV file
        self.file_names = [f"random_data_{i}.csv" for i in range(0, 10)]
        for file_name in self.file_names:
            if not os.path.exists(file_name):
                generate_csv(file_name, 1_000)

        # Create a new instance of CSVProcessor
        self.new_csv = CSVProcessor(self.file_names)

    def tearDown(self):
        # Clean up the generated CSV files
        for file_name in self.file_names:
            if os.path.exists(file_name):
                os.remove(file_name)

    def test_read_and_combine(self):
        self.new_csv.read_and_combine()

    def test_save_combined_data(self):
        self.new_csv.read_and_combine()
        self.new_csv.save_combined_data("test_combined_data.csv")

    def test_retrieve_score_by_name(self):
        self.new_csv.read_and_combine()
        self.new_csv.retrieve_score_by_name("Monica Robinson")


if __name__ == "__main__":
    unittest.main()
