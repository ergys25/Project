import csv
from collections import defaultdict


class CSVProcessor:
    def __init__(self, file_paths):
        self.file_paths = file_paths
        self.data = defaultdict(dict)

    def read_and_combine(self):
        """
        Read and combine data from multiple CSV files
        """
        new_id_counter = 1  # Counter for generating new IDs
        for file_path in self.file_paths:
            with open(file_path, "r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    id = str(new_id_counter)  # Generate new ID
                    new_id_counter += 1  # Increment the counter
                    full_name = row["name"]
                    score = int(row["score"])
                    if id not in self.data:
                        self.data[id] = {
                            "name": full_name,
                            "score": score,
                            "combine": score,
                        }
                    else:
                        if self.data[id]["name"] == full_name:
                            self.data[id]["score"] += score
                            self.data[id]["combine"] += score
                        else:
                            new_id = (
                                id + "_" + full_name
                            )  # Generate a new ID for different names
                            if new_id not in self.data:
                                self.data[new_id] = {
                                    "name": full_name,
                                    "score": score,
                                    "combine": score,
                                }
                            else:
                                self.data[new_id]["score"] += score
                                self.data[new_id]["combine"] += score

    def save_combined_data(self, output_file):
        """
        Save the combined data to a CSV file
        """
        with open(output_file, "w", newline="") as csvfile:
            fieldnames = ["id", "name", "score", "combine"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for id, values in self.data.items():
                writer.writerow(
                    {
                        "id": id,
                        "name": values["name"],
                        "score": values["score"],
                        "combine": values["combine"],
                    }
                )

    def retrieve_score_by_name(self, name):
        """
        Retrieve the score by name from the combined data
        """
        for values in self.data.values():
            if values["name"] == name:
                return values["score"]
        return None
