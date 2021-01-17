# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(user_csvpath, qualifying_loans):
        """Writes the CSV file in path provided.

    Args:
       csvpath (Path): The csv file path.
       a header for the list of qualifying loans
       data (list of lists): a list of rows with values for the CSV file

    Returns:
       A list of qualifying loans that contains the rows of data from the CSV file.

    """
        with open(user_csvpath, "w", newline="") as csv_file: 
            csvwriter = csv.writer(csv_file, delimiter=',')

        # Write header row first
            header = ["Lender","Max Loan Amount","Max LTV","MYax DTI","Min Credit Score","Interest Rate"]
            csvwriter.writerow(header)

        # Write the data rows
            csvwriter.writerows(qualifying_loans)

        return qualifying_loans