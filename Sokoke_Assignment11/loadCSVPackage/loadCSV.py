# File Name : loadCSV.py
# Student Name: Chrystie Cadet
#               Joseph Adcock
# email: cadetce@mail.uc.edu
#        adcockjb@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date: 4/17/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: The project takes a .csv file and cleans the data

# Brief Description of what this module does: This module creates a new .csv with data from the program
# Citations: ChatGPT

# Anything else that's relevant: N/A

import csv
import os

class loadCSVFromList:
    def convertToCSV(self, data, filePath):
        """
        Convert a python List to CSV
        @param data List: The list of data
        @param filePath String: The desired file name(.csv)
        @return CSV file
        """

        fieldNames = set()
        for row in data:
            fieldNames.update(row.keys())
        fieldNames = list(fieldNames)

        # Write the data
        with open(filePath, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldNames)
            writer.writeheader()
            writer.writerows(data)